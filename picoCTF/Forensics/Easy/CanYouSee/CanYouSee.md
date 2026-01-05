# CanYouSee

![image.png](images/image.png)

We are given an image called ukn_reality.jpg

![image.png](images/image%201.png)

Using `exiftool`, we can see the metadata of the image

```bash
└─$ exiftool ukn_reality.jpg 
ExifTool Version Number         : 13.36
File Name                       : ukn_reality.jpg
Directory                       : .
File Size                       : 2.3 MB
File Modification Date/Time     : 2024:03:11 20:05:51-04:00
File Access Date/Time           : 2026:01:04 21:24:04-05:00
File Inode Change Date/Time     : 2026:01:04 21:24:04-05:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 72
Y Resolution                    : 72
XMP Toolkit                     : Image::ExifTool 11.88
Attribution URL                 : cGljb0NURntNRTc0RDQ3QV9ISUREM05fM2I5MjA5YTJ9Cg==
Image Width                     : 4308
Image Height                    : 2875
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 4308x2875
Megapixels                      : 12.4

```

We can see that the Attribution URL is an base64 encoded string, therefore we can try to base 64 decode it, and we can find the flag

```bash
└─$ echo 'cGljb0NURntNRTc0RDQ3QV9ISUREM05fM2I5MjA5YTJ9Cg=='|base64 -d
picoCTF{ME74D47A_HIDD3N_3b9209a2}
```

Alternatively, we can use `strings` to find the base 64 string

```bash
└─$ strings ukn_reality.jpg|head
JFIF
7http://ns.adobe.com/xap/1.0/
<?xpacket begin='
' id='W5M0MpCehiHzreSzNTczkc9d'?>
<x:xmpmeta xmlns:x='adobe:ns:meta/' x:xmptk='Image::ExifTool 11.88'>
<rdf:RDF xmlns:rdf='http://www.w3.org/1999/02/22-rdf-syntax-ns#'>
 <rdf:Description rdf:about=''
  xmlns:cc='http://creativecommons.org/ns#'>
  <cc:attributionURL rdf:resource='cGljb0NURntNRTc0RDQ3QV9ISUREM05fM2I5MjA5YTJ9Cg=='/>
 </rdf:Description>
```

Flag: `picoCTF{ME74D47A_HIDD3N_3b9209a2}`
