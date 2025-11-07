# Riddle Registry

![image.png](images/image.png)

[confidential.pdf](images/confidential.pdf)

Here is how the PDF looks like:

![image.png](images/image%201.png)

Upon viewing the PDF, we can see that some texts are blocked. To view them, we can try to highlight them, but we will realized it will do us no good

![image.png](images/image%202.png)

We can then do some basic file inspection. We can find the name of the author is quite weird in Strings.

```bash
└─$ strings confidential.pdf|head
%PDF-1.7
1 0 obj
/Type /Pages
/Count 1
/Kids [ 4 0 R ]
endobj
2 0 obj
/Producer (PyPDF2)
/Author (**cGljb0NURntwdXp6bDNkX20zdGFkYXRhX2YwdW5kIV9jYTc2YmJiMn0\075**)
endobj

```

It can also be found in the properties under the Linux GUI file inspector or exiftool

```bash
└─$ exiftool confidential.pdf 
ExifTool Version Number         : 13.25
File Name                       : confidential.pdf
Directory                       : .
File Size                       : 183 kB
File Modification Date/Time     : 2025:09:29 17:29:21-04:00
File Access Date/Time           : 2025:11:06 01:10:05-05:00
File Inode Change Date/Time     : 2025:11:06 01:09:38-05:00
File Permissions                : -rw-rw-r--
File Type                       : PDF
File Type Extension             : pdf
MIME Type                       : application/pdf
PDF Version                     : 1.7
Linearized                      : No
Page Count                      : 1
Producer                        : PyPDF2
Author                          : cGljb0NURntwdXp6bDNkX20zdGFkYXRhX2YwdW5kIV9jYTc2YmJiMn0=

```

We can try to decode it using base64. And we can get the flag

```bash
└─$ echo 'cGljb0NURntwdXp6bDNkX20zdGFkYXRhX2YwdW5kIV9jYTc2YmJiMn0='|base64 -d
picoCTF{puzzl3d_m3tadata_f0und!_ca76bbb2}
```

Flag: `picoCTF{puzzl3d_m3tadata_f0und!_ca76bbb2}`
