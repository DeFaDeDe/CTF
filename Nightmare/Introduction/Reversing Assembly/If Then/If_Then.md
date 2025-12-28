# If_Then

## Challenge

> Installation link: `https://github.com/kablaa/CTF-Workshop/blob/master/Reversing/Challenges/IfThen/if_then`
> 

## GDB

Same as before, we can first take a look at the main function

```bash
pwndbg> info func
All defined functions:

Non-debugging symbols:
0x08048290  _init
0x080482d0  puts@plt
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
pwndbg> disass main
Dump of assembler code for function main:
   0x080483fb <+0>:     lea    ecx,[esp+0x4]
   0x080483ff <+4>:     and    esp,0xfffffff0
   0x08048402 <+7>:     push   DWORD PTR [ecx-0x4]
   0x08048405 <+10>:    push   ebp
   0x08048406 <+11>:    mov    ebp,esp
   0x08048408 <+13>:    push   ecx
   0x08048409 <+14>:    sub    esp,0x14
   0x0804840c <+17>:    mov    DWORD PTR [ebp-0xc],0xa
   0x08048413 <+24>:    cmp    DWORD PTR [ebp-0xc],0xa
   0x08048417 <+28>:    jne    0x8048429 <main+46>
   0x08048419 <+30>:    sub    esp,0xc
   0x0804841c <+33>:    push   0x80484c0
   0x08048421 <+38>:    call   0x80482d0 <puts@plt>                                                                                                                                                                                       
   0x08048426 <+43>:    add    esp,0x10                                                                                                                                                                                                   
   0x08048429 <+46>:    mov    eax,0x0                                                                                                                                                                                                    
   0x0804842e <+51>:    mov    ecx,DWORD PTR [ebp-0x4]                                                                                                                                                                                    
   0x08048431 <+54>:    leave                                                                                                                                                                                                             
   0x08048432 <+55>:    lea    esp,[ecx-0x4]                                                                                                                                                                                              
   0x08048435 <+58>:    ret                                                                                                                                                                                                               
End of assembler dump.       pwndbg> info func
All defined functions:

Non-debugging symbols:
0x08048290  _init
0x080482d0  puts@plt
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
pwndbg> disass main
Dump of assembler code for function main:
   0x080483fb <+0>:     lea    ecx,[esp+0x4]
   0x080483ff <+4>:     and    esp,0xfffffff0
   0x08048402 <+7>:     push   DWORD PTR [ecx-0x4]
   0x08048405 <+10>:    push   ebp
   0x08048406 <+11>:    mov    ebp,esp
   0x08048408 <+13>:    push   ecx
   0x08048409 <+14>:    sub    esp,0x14
   0x0804840c <+17>:    mov    DWORD PTR [ebp-0xc],0xa
   0x08048413 <+24>:    cmp    DWORD PTR [ebp-0xc],0xa
   0x08048417 <+28>:    jne    0x8048429 <main+46>
   0x08048419 <+30>:    sub    esp,0xc
   0x0804841c <+33>:    push   0x80484c0
   0x08048421 <+38>:    call   0x80482d0 <puts@plt>                                                                                                                                                                                       
   0x08048426 <+43>:    add    esp,0x10                                                                                                                                                                                                   
   0x08048429 <+46>:    mov    eax,0x0                                                                                                                                                                                                    
   0x0804842e <+51>:    mov    ecx,DWORD PTR [ebp-0x4]                                                                                                                                                                                    
   0x08048431 <+54>:    leave                                                                                                                                                                                                             
   0x08048432 <+55>:    lea    esp,[ecx-0x4]                                                                                                                                                                                              
   0x08048435 <+58>:    ret                                                                                                                                                                                                               
End of assembler dump.       
```

We can see it will jump to main+46 if the content of the stack address in `ebp-0xc` is equal to `0xa`(10 in decimal). We know that because of the `jne` (jump not equal) operation

```bash
0x08048413 <+24>:    cmp    DWORD PTR [ebp-0xc],0xa
   0x08048417 <+28>:    jne    0x8048429 <main+46>
```

We can see that it will then exit the program

```bash
   0x08048429 <+46>:    mov    eax,0x0                                                                                                                                                                                                    
   0x0804842e <+51>:    mov    ecx,DWORD PTR [ebp-0x4]                                                                                                                                                                                    
   0x08048431 <+54>:    leave 
```

However, if it is equal, it will print something

```bash
   0x08048419 <+30>:    sub    esp,0xc
   0x0804841c <+33>:    push   0x80484c0
   0x08048421 <+38>:    call   0x80482d0 <puts@plt> 
```

What is the string? We can use `x` to print it out 

```bash
**pwndbg> x/s 0x80484c0                                                                                                                                                                                                                    
0x80484c0:      "x = ten"**
```

Great, so now we know that it will always output this string when we execute, as before the comparison, we already set it to be 10

```bash
0x0804840c <+17>:    mov    DWORD PTR [ebp-0xc],0xa
```

We can confirm our deduction is correct by running the code

```bash
└─$ ./if_then                                                                                                                                                                                                                             
x = ten
```
