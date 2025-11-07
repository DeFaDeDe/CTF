# Corrupted file

![image.png](images/image.png)

It is stated that a few bytes is corrupted

```jsx
└─$ file file 
file: data
```

We can try to use xxd to check the hex. use the `-e` for little-endian dump and `-r` for reverse operation

Checking the hex, we can confirm it is a jpg file. The magic bytes are corrupted

```jsx
└─$ xxd -er file |head                                                                                                                                                                                                                     
00000000: e0ff785c 464a1000 01004649 01000001  \x....JFIF......
00000010: 00000100 4300dbff 06060800 08050607  .......C........
00000020: 09070707 0c0a0809 0b0c0d14 12190c0b  ................
00000030: 1d140f13 1d1e1f1a 201c1c1a 20272e24  ........... $.' 
00000040: 1c232c22 2937281c 3431302c 271f3434  ",#..(7),01444.'
00000050: 32383d39 34332e3c 00dbff32 09090143  9=82<.342...C...
00000060: 0c0b0c09 180d0d18 211c2132 32323232  ........2!.!2222
00000070: 32323232 32323232 32323232 32323232  2222222222222222
00000080: 32323232 32323232 32323232 32323232  2222222222222222
00000090: 32323232 32323232 32323232 c0ff3232  22222222222222..
```

To correct the jpg to the correct magic bytes, we can refer to this Wikipedia: https://en.wikipedia.org/wiki/List_of_file_signatures

Change these 12 bits in a hex editor(e.g. ghex) to fix the magic bytes. Notice that we use little endian here, so we are fixing the `5c 78` to `FF D8`

![image.png](images/image%201.png)

After saving the changes, open the file to see the flag:

![image.png](images/image%202.png)

Flag: `picoCTF{r3st0r1ng_th3_by73s_2326ca93}`
