# Loop

## Challenge

> Source: `https://github.com/kablaa/CTF-Workshop/blob/master/Reversing/Challenges/Loop/loop`
> 


## gdb-pwndbg

We should first look at the main function

```bash
pwndbg> info fun
All defined functions:

Non-debugging symbols:
0x08048294  _init
0x080482d0  printf@plt
0x080482e0  __gmon_start__@plt
0x080482f0  __libc_start_main@plt
0x08048300  _start
0x08048330  __x86.get_pc_thunk.bx
0x08048340  deregister_tm_clones
0x08048370  register_tm_clones
0x080483b0  __do_global_dtors_aux
0x080483d0  frame_dummy
0x080483fb  main
0x08048440  __libc_csu_init
0x080484a0  __libc_csu_fini
0x080484a4  _fini
pwndbg> 

```

## main

Here is the main function

```bash
pwndbg> disass main
Dump of assembler code for function main:
   0x080483fb <+0>:     lea    ecx,[esp+0x4]
   0x080483ff <+4>:     and    esp,0xfffffff0
   0x08048402 <+7>:     push   DWORD PTR [ecx-0x4]
   0x08048405 <+10>:    push   ebp
   0x08048406 <+11>:    mov    ebp,esp
   0x08048408 <+13>:    push   ecx
   0x08048409 <+14>:    sub    esp,0x14
   0x0804840c <+17>:    mov    DWORD PTR [ebp-0xc],0x0
   0x08048413 <+24>:    jmp    0x804842c <main+49>
   0x08048415 <+26>:    sub    esp,0x8
   0x08048418 <+29>:    push   DWORD PTR [ebp-0xc]
   0x0804841b <+32>:    push   0x80484c0
   0x08048420 <+37>:    call   0x80482d0 <printf@plt>
   0x08048425 <+42>:    add    esp,0x10
   0x08048428 <+45>:    add    DWORD PTR [ebp-0xc],0x1
   0x0804842c <+49>:    cmp    DWORD PTR [ebp-0xc],0x13
   0x08048430 <+53>:    jle    0x8048415 <main+26>
   0x08048432 <+55>:    mov    eax,0x0
   0x08048437 <+60>:    mov    ecx,DWORD PTR [ebp-0x4]
   0x0804843a <+63>:    leave
   0x0804843b <+64>:    lea    esp,[ecx-0x4]
   0x0804843e <+67>:    ret
End of assembler dump.

```

We should read from main+17, and we will see `[ebp-0xc]` is initiated as `0x0`, and it will compare to `0x13`, and jump to `main+26` if it is less than or equal to `0x13`

```bash
0x0804840c <+17>:    mov    DWORD PTR [ebp-0xc],0x0
0x08048413 <+24>:    jmp    0x804842c <main+49>
   .
   .
   .
0x0804842c <+49>:    cmp    DWORD PTR [ebp-0xc],0x13
0x08048430 <+53>:    jle    0x8048415 <main+26>

```

We can then take a look at what is after the jump, I found this to be a bit complicated at first due to not familiar with stack, so I will break down step by step

```bash
0x08048415 <+26>:    sub    esp,0x8
0x08048418 <+29>:    push   DWORD PTR [ebp-0xc]
0x0804841b <+32>:    push   0x80484c0
0x08048420 <+37>:    call   0x80482d0 <printf@plt>
0x08048425 <+42>:    add    esp,0x10
0x08048428 <+45>:    add    DWORD PTR [ebp-0xc],0x1

```

To know how it works, I set a breakpoint at `main+29` using `b *main+29`, and then use `r` to run, if we check the value of `[ebp-0xc]`, it is `0`

```bash
pwndbg> r
Starting program: /home/kali/CTF/Nightmare/Introduction/Reversing Assembly/Loop/loop 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/usr/lib/x86_64-linux-gnu/libthread_db.so.1".

Breakpoint 2, 0x08048418 in main ()
LEGEND: STACK | HEAP | CODE | DATA | WX | RODATA
──────────────────────────────────────────────────────────────────────────────────────────[ REGISTERS / show-flags off / show-compact-regs off ]───────────────────────────────────────────────────────────────────────────────────────────
 EAX  0x80483fb (main) ◂— lea ecx, [esp + 4]
 EBX  0xf7f96e14 ◂— 0x233d0c /* '\x0c=#' */
 ECX  0xffffcc90 ◂— 1
 EDX  0xffffccb0 —▸ 0xf7f96e14 ◂— 0x233d0c /* '\x0c=#' */
 EDI  0xf7ffcc60 (_rtld_global_ro) ◂— 0
 ESI  0x8048440 (__libc_csu_init) ◂— push ebp
 EBP  0xffffcc78 ◂— 0
 ESP  0xffffcc58 ◂— 0xffffffff
 EIP  0x8048418 (main+29) ◂— push dword ptr [ebp - 0xc]
────────────────────────────────────────────────────────────────────────────────────────────────────[ DISASM / i386 / set emulate on ]─────────────────────────────────────────────────────────────────────────────────────────────────────
 ► 0x8048418 <main+29>    push   dword ptr [ebp - 0xc]
   0x804841b <main+32>    push   0x80484c0
   0x8048420 <main+37>    call   printf@plt                  <printf@plt>
 
   0x8048425 <main+42>    add    esp, 0x10
   0x8048428 <main+45>    add    dword ptr [ebp - 0xc], 1
   0x804842c <main+49>    cmp    dword ptr [ebp - 0xc], 0x13
   0x8048430 <main+53>    jle    main+26                     <main+26>
 
   0x8048432 <main+55>    mov    eax, 0                       EAX => 0
   0x8048437 <main+60>    mov    ecx, dword ptr [ebp - 4]
   0x804843a <main+63>    leave  
   0x804843b <main+64>    lea    esp, [ecx - 4]
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────[ STACK ]─────────────────────────────────────────────────────────────────────────────────────────────────────────────────
00:0000│ esp 0xffffcc58 ◂— 0xffffffff
01:0004│-01c 0xffffcc5c —▸ 0xf7d74b10 ◂— 0x93e /* '>\t' */
02:0008│-018 0xffffcc60 —▸ 0xf7fbc400 —▸ 0xf7d63000 ◂— 0x464c457f
03:000c│-014 0xffffcc64 ◂— 0
... ↓        3 skipped
07:001c│-004 0xffffcc74 —▸ 0xffffcc90 ◂— 1
───────────────────────────────────────────────────────────────────────────────────────────────────────────────[ BACKTRACE ]───────────────────────────────────────────────────────────────────────────────────────────────────────────────
 ► 0 0x8048418 main+29
   1 0xf7d88ec3 None
   2 0xf7d88f88 __libc_start_main+136
   3 0x8048321 _start+33
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
pwndbg> x/d $ebp-0xc
0xffffcc6c:     0
```

But what is `0x80484c0` in `main+32`? Well, it is just a format specifier for decimal. Because we push `ebp-0xc` at the last instruction(recall stack is Last-In-First-Out), `%d` will specify it, which is - at this moment.

```bash
pwndbg> x/s  0x80484c0
0x80484c0:      "%d "
```

We can then type `c` to continue, and it will reach the breakpoint again, and if we check the value of `[ebp-0xc]`, we will see it is incremented by 1, it is because of the line `0x08048428 <+45>:    add    DWORD PTR [ebp-0xc],0x1`

```bash
pwndbg> x/d $ebp-0xc
0xffffcc6c:     1
```

That means that it will loop until it is greater than `0x13`, which stops when `[ebp-0xc]` = 20 in decimal.

## Run the program

To verify, we can run the program, and it is the same as what we expected

```bash
└─$   ./loop
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
```
