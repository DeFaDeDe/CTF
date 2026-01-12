# Wave a flag

![image.png](images/image.png)

This challenge can be solved using `strings` directly on the ELF file

```bash
└─$ file warm 
warm: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=9e46ec8729d2f2aa8ffc4b1cdc058081bddcfe67, for GNU/Linux 3.2.0, with debug_info, not stripped

└─$ strings warm 
.
.
.
Hello user! Pass me a -h to learn what I can do!
Oh, help? I actually don't do much, but I do have this flag here: picoCTF{b1scu1ts_4nd_gr4vy_ac5832c}

```

The intended way is to execute the ELF with `-h` flag

```bash
└─$ ./warm                                                                                                                                                                                                                                 
bash: ./warm: Permission denied

└─$ chmod +x warm                                                                                                                                                                                                                          

└─$ ./warm                                                                                                                                                                                                                                 
Hello user! Pass me a -h to learn what I can do!

└─$ ./warm -h                                                                                                                                                                                                                              
Oh, help? I actually don't do much, but I do have this flag here: picoCTF{b1scu1ts_4nd_gr4vy_ac5832c}

```

Flag: `picoCTF{b1scu1ts_4nd_gr4vy_ac5832c}`
