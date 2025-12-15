# Compiled

![image.png](image.png)

## Strings

It is a common practice to use a utility called `strings` to discover printable characters in the files in CTF.

https://linux.die.net/man/1/strings

The Utility strings can be installed on Linux machines using the command `sudo apt install binutils`

We can use strings in the format of `strings <-filename->`, below are the result

```bash
└─$ strings Compiled
/lib64/ld-linux-x86-64.so.2
jKUhR
__cxa_finalize
__libc_start_main
strcmp
stdout
__isoc99_scanf
fwrite
printf
libc.so.6
GLIBC_2.7
GLIBC_2.2.5
GLIBC_2.34
_ITM_deregisterTMCloneTable
__gmon_start__
_ITM_registerTMCloneTable
PTE1
u+UH
StringsIH
sForNoobH
Password:
DoYouEven%sCTF
__dso_handle
_init
Correct!
Try again!
;*3$"
GCC: (Debian 11.3.0-5) 11.3.0
Scrt1.o
__abi_tag
crtstuff.c
deregister_tm_clones
__do_global_dtors_aux
completed.0
__do_global_dtors_aux_fini_array_entry
frame_dummy
__frame_dummy_init_array_entry
zzz.c
__FRAME_END__
_DYNAMIC
__GNU_EH_FRAME_HDR
_GLOBAL_OFFSET_TABLE_
__libc_start_main@GLIBC_2.34
_ITM_deregisterTMCloneTable
stdout@GLIBC_2.2.5
_edata
_fini
printf@GLIBC_2.2.5
__data_start
strcmp@GLIBC_2.2.5
__gmon_start__
__dso_handle
_IO_stdin_used
_end
__bss_start
main
__isoc99_scanf@GLIBC_2.7
fwrite@GLIBC_2.2.5
__TMC_END__
_ITM_registerTMCloneTable
__cxa_finalize@GLIBC_2.2.5
_init
.symtab
.strtab
.shstrtab
.interp
.note.gnu.property
.note.gnu.build-id
.note.ABI-tag
.gnu.hash
.dynsym
.dynstr
.gnu.version
.gnu.version_r
.rela.dyn
.rela.plt
.init
.plt.got
.text
.fini
.rodata
.eh_frame_hdr
.eh_frame
.init_array
.fini_array
.dynamic
.got.plt
.data
.bss
.comment
```

## Analysis

We can see there is a verification part:

```bash
StringsIH
sForNoobH
Password:
DoYouEven%sCTF
__dso_handle
_init
Correct!
Try again!
```

Is the password `DoYouEven%sCTF`? We can try to execute the ELF file

```bash
└─$ ./Compiled
Password: DoYouEven%sCTF
Try again!
```

In most programming languages, `%s` is a format specifier of strings, that is, a placeholder for a string. In this case, the answer should be `DoYouEven__dso_handleCTF`, right?

```bash
└─$ ./Compiled
Password: DoYouEven__dso_handleCTF
Try again!
```

Welp, how about `DoYouEven_initCTF`?

```bash
└─$ ./Compiled
Password: DoYouEven_initCTF
Correct!
```

Welp, the answer is `DoYouEven_init`

```bash
└─$ ./Compiled
Password: DoYouEven_init
Correct!
```

Why? Because Strings aren’t that reliable when you try to understand the code. 

## Ghidra

To analyze, we can use a tool called Ghidra. Once we open the ELF with Ghidra, everything seems to be clear

![image.png](image%201.png)

Still confused? We can rename the variables for clarity

![image.png](image%202.png)

Once `DoYouEven` is typed, the remainder of the input is stored in the buffer. The function `strcmp` then checks this buffer against specific strings, returning zero only when they are an exact match. If the buffer contains `__dso_handle`, the check fails; the only case that succeeds is when the buffer equals `_init`.

Therefore the answer is `DoYouEven_init`

## Finished

![image.png](image%203.png)