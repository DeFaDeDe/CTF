# information

![image.png](images/image.png)

We can first check the file type, and we can confirm that it is indeed a JPG file

```bash
└─$ file cat.jpg 
cat.jpg: JPEG image data, JFIF standard 1.02, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 2560x1598, components 3
```

We can then extract the metadata in the JPG, and the License seems weird

```bash
└─$ exiftool cat.jpg 
ExifTool Version Number         : 13.36
File Name                       : cat.jpg
Directory                       : .
File Size                       : 878 kB
File Modification Date/Time     : 2025:12:12 14:21:14-05:00
File Access Date/Time           : 2026:01:12 10:47:10-05:00
File Inode Change Date/Time     : 2026:01:12 10:47:10-05:00
File Permissions                : -rw-rw-r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.02
Resolution Unit                 : None
X Resolution                    : 1
Y Resolution                    : 1
Current IPTC Digest             : 7a78f3d9cfb1ce42ab5a3aa30573d617
Copyright Notice                : PicoCTF
Application Record Version      : 4
XMP Toolkit                     : Image::ExifTool 10.80
License                         : cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9
Rights                          : PicoCTF                                                                                                                                                                                                  
Image Width                     : 2560                                                                                                                                                                                                     
Image Height                    : 1598                                                                                                                                                                                                     
Encoding Process                : Baseline DCT, Huffman coding                                                                                                                                                                             
Bits Per Sample                 : 8                                                                                                                                                                                                        
Color Components                : 3                                                                                                                                                                                                        
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)                                                                                                                                                                                         
Image Size                      : 2560x1598                                                                                                                                                                                                
Megapixels                      : 4.1      
```

Decoding it using base 64 will give us the flag

```bash
└─$ echo cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9|base64 -d
picoCTF{the_m3tadata_1s_modified}
```

Flag: `picoCTF{the_m3tadata_1s_modified}`
