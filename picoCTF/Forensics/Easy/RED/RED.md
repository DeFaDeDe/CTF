# RED

![image.png](images/image.png)

Using `strings`, we find a weird poem

```bash
└─$ strings red.png 
IHDR
tEXtPoem
Crimson heart, vibrant and bold,
Hearts flutter at your sight.
Evenings glow softly red,
Cherries burst with sweet life.
Kisses linger with your warmth.
Love deep as merlot.
Scarlet leaves falling softly,
Bold in every stroke.x
IDATx
IEND
```

IDHR, IDAT, and IEND are headers for a PNG file. For more info, refer to this(https://www.libpng.org/pub/png/spec/1.2/PNG-Chunks.html)

In simple words:

- IDHR: control metadata(e.g. dimension, color)
- IDAT: image data. Notice there can be multiple IDATs in a PNG file.
- IEND: marks the end of the image

then I try to read the IDAT, but I have no idea except confusion 

```bash
└─$ xxd -er red.png 
00000000: 474e5089 0a1a0a0d 0d000000 52444849  .PNG........IHDR
00000010: 80000000 80000000 00000608 613ec300  ..............>a
00000020: 000000cb 584574e7 656f5074 7243006d  .....tEXtPoem.Cr
00000030: 6f736d69 6568206e 2c747261 62697620  imson heart, vib
00000040: 746e6172 646e6120 6c6f6220 480a2c64  rant and bold,.H
00000050: 74726165 6c662073 65747475 74612072  earts flutter at
00000060: 756f7920 69732072 2e746867 6576450a   your sight..Eve
00000070: 676e696e 6c672073 7320776f 6c74666f  nings glow softl
00000080: 65722079 430a2c64 72726568 20736569  y red,.Cherries 
00000090: 73727562 69772074 73206874 74656577  burst with sweet
000000a0: 66696c20 4b0a2e65 65737369 696c2073   life..Kisses li
000000b0: 7265676e 74697720 6f792068 77207275  nger with your w
000000c0: 746d7261 4c0a2e68 2065766f 70656564  armth..Love deep
000000d0: 20736120 6c72656d 0a2e746f 72616353   as merlot..Scar
000000e0: 2074656c 7661656c 66207365 696c6c61  let leaves falli
000000f0: 7320676e 6c74666f 420a2c79 20646c6f  ng softly,.Bold 
00000100: 65206e69 79726576 72747320 2e656b6f  in every stroke.
00000110: 159d9578 f0010000 54414449 d2ed9c78  x.......IDATx...
00000120: 3102724b 29510300 ca333ff7 22921ec2  Kr.1..Q).?3...."
00000130: dbf741b9 8cfe3050 bed5f74d 92dd34b2  .A..P0..M....4..
00000140: dd9ac936 c935929f b64d2492 9d9a6934  6.....5..$M.4i..
00000150: 7f7ac727 4b8cf64f d66b2ddb 97c33ba4  '.z.O..K.-k..;..
00000160: 3bf8cfae 24ba4d39 faf7b65d fadf3dbf  ...;9M.$]....=..
00000170: 1ef34dbc ced976bf 72959fb3 8f966917  .M...v.....r.i..
00000180: e7e99ed5 79e7df3d f5e77bce ee97f5bf  ....=..y.{......
00000190: 4e7a5f8c d9597bdb f78fbf99 fc73bb5f  ._zN.{Y....._.s.
000001a0: 21ee79e7 7ddcfdef 3bbf67da efbef72d  .y.!...}.g.;-...
000001b0: e752fbfc b37ef778 ebf6fd9f e079fa6e  ..R.x.~.....n.y.
000001c0: ddcd6fe7 fcf9db38 24503bfa 00670006  .o..8....;P$..g.
000001d0: 67000670 00067000 06700067 70006700  p..g.p..g.p..g.p
000001e0: 00670006 67000670 00067000 06700067  ..g.p..g.p..g.p.
000001f0: 70006700 00670006 67000670 00067000  .g.p..g.p..g.p..
00000200: 06700067 70006700 00670006 67000670  g.p..g.p..g.p..g
00000210: 00067000 06700067 70006700 00670006  .p..g.p..g.p..g.
00000220: 67000670 00067000 06700067 70006700  p..g.p..g.p..g.p
00000230: 00670006 67000670 00067000 06700067  ..g.p..g.p..g.p.
00000240: 70006700 00670006 67000670 00067000  .g.p..g.p..g.p..
00000250: 06700067 70006700 00670006 67000670  g.p..g.p..g.p..g
00000260: 00067000 06700067 70006700 00670006  .p..g.p..g.p..g.
00000270: 67000670 00067000 06700067 70006700  p..g.p..g.p..g.p
00000280: 00670006 67000670 00067000 06700067  ..g.p..g.p..g.p.
00000290: 70006700 00670006 67000670 00067000  .g.p..g.p..g.p..
000002a0: 06700067 70006700 00670006 67000670  g.p..g.p..g.p..g
000002b0: 00067000 06700067 70006700 00670006  .p..g.p..g.p..g.
000002c0: 67000670 00067000 06700067 70006700  p..g.p..g.p..g.p
000002d0: 00670006 67000670 00067000 06700067  ..g.p..g.p..g.p.
000002e0: 70006700 00670006 67000670 00067000  .g.p..g.p..g.p..
000002f0: 06700067 70006700 00670006 67000670  g.p..g.p..g.p..g
00000300: 00067000 df700067 ff76fbb1 91d69b26  .p..g.p...v.&...
00000310: 00000000 444e4549 826042ae           ....IEND.B`.
```

There seems no hidden file beneath the PNG, as it only has zlib compression

```bash
└─$ binwalk red.png 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 128 x 128, 8-bit/color RGBA, non-interlaced
284           0x11C           Zlib compressed data, default compression
```

I also tried to use Stegsolve, and I found there is something hiding in the alpha layer.

![image.png](images/image%201.png)

I thought it is a barcode and try to scan it. Failed of course

For most barcode, it is Interleaved 2 of 5 (https://en.wikipedia.org/wiki/Interleaved_2_of_5). Which i failed to recognized that it is not ITF and wasted my time. 

The solution is quite simple, use a tool called zsteg(https://github.com/zed-0xff/zsteg). It is a tool that used to detect data in png and bmp files.

```bash
└─$ zsteg red.png 
meta Poem           .. text: "Crimson heart, vibrant and bold,\nHearts flutter at your sight.\nEvenings glow softly red,\nCherries burst with sweet life.\nKisses linger with your warmth.\nLove deep as merlot.\nScarlet leaves falling softly,\nBold in every stroke."
b1,rgba,lsb,xy      .. text: "cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ=="
b1,rgba,msb,xy      .. file: OpenPGP Public Key
b2,g,lsb,xy         .. text: "ET@UETPETUUT@TUUTD@PDUDDDPE"
b2,rgb,lsb,xy       .. file: OpenPGP Secret Key
b2,bgr,msb,xy       .. file: OpenPGP Public Key
b2,rgba,lsb,xy      .. file: OpenPGP Secret Key
b2,rgba,msb,xy      .. text: "CIkiiiII"
b2,abgr,lsb,xy      .. file: OpenPGP Secret Key
b2,abgr,msb,xy      .. text: "iiiaakikk"
b3,rgba,msb,xy      .. text: "#wb#wp#7p"
b3,abgr,msb,xy      .. text: "7r'wb#7p"
b4,b,lsb,xy         .. file: 0421 Alliant compact executable not stripped
                    .. 
                    
└─$ echo 'cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ=='|base64 -d
picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355_}picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355_}picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355_}picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355_}

```

Flag: `picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355_}`
