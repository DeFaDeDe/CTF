# Investigative Reversing 0

![image.png](images/image.png)

## PNG Inspection

We are given two files, a PNG file and a binary file.

```bash
└─$ ls
mystery  mystery.png
```

The image wrote ‘Where’d the flag go!’ in a very artistical style

![image.png](images/image%201.png)

I try to inspect the png file, and found that there is some trailer data suggested by `exiftool`

```bash
└─$ file mystery.png 
mystery.png: PNG image data, 1411 x 648, 8-bit/color RGB, non-interlaced

└─$ exiftool mystery.png 
ExifTool Version Number         : 13.50
File Name                       : mystery.png
Directory                       : .
File Size                       : 125 kB
File Modification Date/Time     : 2025:11:08 03:37:22+08:00
File Access Date/Time           : 2026:05:12 19:57:26+08:00
File Inode Change Date/Time     : 2026:05:12 19:57:26+08:00
File Permissions                : -rw-rw-r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 1411
Image Height                    : 648
Bit Depth                       : 8
Color Type                      : RGB
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
SRGB Rendering                  : Perceptual
Gamma                           : 2.2
Pixels Per Unit X               : 5669
Pixels Per Unit Y               : 5669
Pixel Units                     : meters
Warning                         : [minor] Trailer data after PNG IEND chunk
Image Size                      : 1411x648
Megapixels                      : 0.914             
```

Using tail, we can find a flag-like string at the very end, but seems to be encoded by the binary file

```bash
└─$ strings mystery.png|tail
777[[[WW
^^^...
.]JHH8
###G
?NOO
%IIIo
!33S
IEND
picoCTK
k5zsid6q_f0a9b767}
```

## Binary Inspection

Checking the binary, we can see that it requires flag.txt and mystery.png to execute

```bash
─$ file mystery
mystery: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=34b772a4f30594e2f30ac431c72667c3e10fa3e9, not stripped

└─$ strings mystery
/lib64/ld-linux-x86-64.so.2
libc.so.6
exit
fopen
puts
__stack_chk_fail
fputc
fclose
fread
__cxa_finalize
__libc_start_main
GLIBC_2.4
GLIBC_2.2.5
_ITM_deregisterTMCloneTable
__gmon_start__
_ITM_registerTMCloneTable
u/UH
[]A\A]A^A_
flag.txt
mystery.png
No flag found, please make sure this is run on the server
mystery.png is missing, please run this on the server
at insert

```

Open up in Ghidra and rename the variables, it appears that some characters are incremented by `0x05` 

![image.png](images/image%202.png)

We can use `xxd` to extract the hex or the string

```bash
└─$ xxd mystery.png|tail -n 2                                                                                                                                                                 
0001e870: 4260 8270 6963 6f43 544b 806b 357a 7369  B`.picoCTK.k5zsi
0001e880: 6436 715f 6630 6139 6237 3637 7d         d6q_f0a9b767}
```

Then we can write a python script to solve this, notice that the 7th character is `\x80`, which is not printable.

We also don’t have the 15th character as it is sandwiched between the two ranges, so just represent it using `?` first

```python
#enc_flag='picoCTK'+''+'k5zsi' + 'd6q_f0a9b767}'
enc_flag=bytes.fromhex('7069636f43544b806b357a73696436715f66306139623736377d')

print(enc_flag[0:6].decode(), end='')
for i in range(6,15):
    print(chr(enc_flag[i]-5), end='')
    
print('?', end='')
print(enc_flag[16::].decode())
```

Executing it will gives us the flag, and because the middle part seems to be resemble `it`, I believe the remaining character will be `t`

```bash
└─$ python exploit.py                                                                                                                                                                           
picoCTF{f0und_1?_f0a9b767}
```

Flag: `picoCTF{f0und_1t_f0a9b767}`
