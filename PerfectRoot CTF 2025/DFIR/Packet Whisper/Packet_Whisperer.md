# Packet Whisperer

![image.png](Packet%20Whisperer/image.png)

Using `strings` on the pcap file, we can find some base64 strings

```bash
(AJABwAbm90ZXMudHh0VVQJAAPPGCdpzxgnaXV4Cw       hackerman
(AJABwAbm90ZXMudHh0VVQJAAPPGCdpzxgnaXV4Cw       hackerman
v=spf1 -all
'i}}
(ABBOgDAAAE6AMAAFNvbWUgcmFuZG9t
IGRhdGEsI       hackerman
(ABBOgDAAAE6AMAAFNvbWUgcmFuZG9t
IGRhdGEsI       hackerman
(HlvdSBhcmUgY2xvc2UgdGhvdWdoIApQSwECHgMKA       hackerman
(HlvdSBhcmUgY2xvc2UgdGhvdWdoIApQSwECHgMKA       hackerman
v=spf1 -all
(AAAAABykXpbDvPsBhsAAAAbAAAA
CAAYAAAAAAAB    hackerman
(AAAAABykXpbDvPsBhsAAAAbAAAA
CAAYAAAAAAAB    hackerman
gFMI
(AAAAtIEAAAAAZmxhZy50eHRVVAUAA6cYJ2l1eAsA       hackerman
'iDt
(AAAAtIEAAAAAZmxhZy50eHRVVAUAA6cYJ2l1eAsA       hackerman
v=spf1 -all
(AQToAwAABOgDAABQSwECHgMK
AAAAAACIkXpbt25 hackerman
(AQToAwAABOgDAABQSwECHgMK
AAAAAACIkXpbt25 hackerman
gFMal
(XdigAAAAoAAAACQAYAAAAAAABAAAAtIFdAAAAbm9       hackerman
(XdigAAAAoAAAACQAYAAAAAAABAAAAtIFdAAAAbm9       hackerman
v=spf1 -all
(0ZXMudHh0VVQFAAPPGCdp
dXgLAAEE6AMAAAToAw      hackerman
vK}Y
(0ZXMudHh0VVQFAAPPGCdp
dXgLAAEE6AMAAAToAw      hackerman
"AAUEsFBgAAAAACAAIAnQAAAMgAAAAAAA==     hackerman
"AAUEsFBgAAAAACAAIAnQAAAMgAAAAAAA==     hackerman
```

Remove the duplicated strings carefully and we can try to decode the base64 string: 

`UEsDBAoAAAAAAHKRelsO8+wGGwAAABsAAAAIABwAZmxhZy50eHRVVAkAA6cYJ2mnGCdpdXgLAAEE6AMAAAToAwAAcjAwdHsxdHNfNGx3NHk1X0ROU19yMWdodH0KUEsDBAoAAAAAAIiRelu3bld2KAAAACgAAAAJABwAbm90ZXMudHh0VVQJAAPPGCdpzxgnaXV4CwABBOgDAAAE6AMAAFNvbWUgcmFuZG9tIGRhdGEsIHlvdSBhcmUgY2xvc2UgdGhvdWdoIApQSwECHgMKAAAAABykXpbDvPsBhsAAAAbAAAACAAYAAAAAAABAAAAtIEAAAAAZmxhZy50eHRVVAUAA6cYJ2l1eAsAAQToAwAABOgDAABQSwECHgMKAAAAAACIkXpbt25XdigAAAAoAAAACQAYAAAAAAABAAAAtIFdAAAAbm90ZXMudHh0VVQFAAPPGCdpdXgLAAEE6AMAAAToAwAAUEsFBgAAAAACAAIAnQAAAMgAAAAAAA==`

It seems to be a random string at first, but then I located the flag

![image.png](Packet%20Whisperer/image%201.png)

Using the detect file type feature in Cyberchef, we can see it is a zip file. We can also verify by checking the magic bytes(https://en.wikipedia.org/wiki/List_of_file_signatures), we will reach the same answer

![image.png](Packet%20Whisperer/image%202.png)

We can also get the flag by extracting it from the zip, We can copy the base64 string and then decode it and save in a zip file 

```bash
└─$ echo 'UEsDBAoAAAAAAHKRelsO8+wGGwAAABsAAAAIABwAZmxhZy50eHRVVAkAA6cYJ2mnGCdpdXgLAAEE6AMAAAToAwAAcjAwdHsxdHNfNGx3NHk1X0ROU19yMWdodH0KUEsDBAoAAAAAAIiRelu3bld2KAAAACgAAAAJABwAbm90ZXMudHh0VVQJAAPPGCdpzxgnaXV4CwABBOgDAAAE6AMAAFNvbWUgcmFuZG9tIGRhdGEsIHlvdSBhcmUgY2xvc2UgdGhvdWdoIApQSwECHgMKAAAAABykXpbDvPsBhsAAAAbAAAACAAYAAAAAAABAAAAtIEAAAAAZmxhZy50eHRVVAUAA6cYJ2l1eAsAAQToAwAABOgDAABQSwECHgMKAAAAAACIkXpbt25XdigAAAAoAAAACQAYAAAAAAABAAAAtIFdAAAAbm90ZXMudHh0VVQFAAPPGCdpdXgLAAEE6AMAAAToAwAAUEsFBgAAAAACAAIAnQAAAMgAAAAAAA=='|base64 -d > flag.zip
base64: invalid input

└─$ unzip flag.zip 
Archive:  flag.zip
  End-of-central-directory signature not found.  Either this file is not
  a zipfile, or it constitutes one disk of a multi-part archive.  In the
  latter case the central directory and zipfile comment will be found on
  the last disk(s) of this archive.
unzip:  cannot find zipfile directory in one of flag.zip or
        flag.zip.zip, and cannot find flag.zip.ZIP, period.

```

However, it is still possible to unzip using the GUI

![image.png](Packet%20Whisperer/image%203.png)

Inside the flag directory, we can find the flag

```bash
└─$ tree flag
flag
├── flag.txt
└── notes.txt

1 directory, 2 files

└─$ cat flag/flag.txt 
r00t{1ts_4lw4y5_DNS_r1ght}

└─$ cat flag/notes.txt 
Some random data, you are close though 
```

Flag: `r00t{1ts_4lw4y5_DNS_r1ght}`