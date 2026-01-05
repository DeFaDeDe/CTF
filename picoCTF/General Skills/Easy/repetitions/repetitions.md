# repetitions

![image.png](images/image.png)

Upon reading the `enc_flag` file, I realize it is a base 64 string, and maybe encoded multiple times

```bash
└─$ cat enc_flag 
VmpGU1EyRXlUWGxTYmxKVVYwZFNWbGxyV21GV1JteDBUbFpPYWxKdFVsaFpWVlUxWVZaS1ZWWnVh
RmRXZWtab1dWWmtSMk5yTlZWWApiVVpUVm10d1VWZFdVa2RpYlZaWFZtNVdVZ3BpU0VKeldWUkNk
MlZXVlhoWGJYQk9VbFJXU0ZkcVRuTldaM0JZVWpGS2VWWkdaSGRXCk1sWnpWV3hhVm1KRk5XOVVW
VkpEVGxaYVdFMVhSbFpSV0VKWVZGVmtNRTVHV2tWU2JYUlVDbUpXV25sVWJGcHZWbGRHZEdWRlZs
aGkKYlRrelZERldUMkpzUWxWTlJYTkxDZz09Cg==
```

Turns out it is encoded six times, so we can just decode it until we reach the flag

```bash
└─$ cat enc_flag|base64 -d
VjFSQ2EyTXlSblJUV0dSVllrWmFWRmx0TlZOalJtUlhZVVU1YVZKVVZuaFdWekZoWVZkR2NrNVVX
bUZTVmtwUVdWUkdibVZXVm5WUgpiSEJzWVRCd2VWVXhXbXBOUlRWSFdqTnNWZ3BYUjFKeVZGZHdW
MlZzVWxaVmJFNW9UVVJDTlZaWE1XRlZRWEJYVFVkME5GWkVSbXRUCmJWWnlUbFpvVldGdGVFVlhi
bTkzVDFWT2JsQlVNRXNLCg==

└─$ cat enc_flag|base64 -d|base64 -d
V1RCa2MyRnRTWGRVYkZaVFltNVNjRmRXYUU5aVJUVnhWVzFhYVdGck5UWmFSVkpQWVRGbmVWVnVR
bHBsYTBweVUxWmpNRTVHWjNsVgpXR1JyVFdwV2VsUlZVbE5oTURCNVZXMWFVQXBXTUd0NFZERmtT
bVZyTlZoVWFteEVXbm93T1VOblBUMEsK

└─$ cat enc_flag|base64 -d|base64 -d|base64 -d
WTBkc2FtSXdUbFZTYm5ScFdWaE9iRTVxVW1aaWFrNTZaRVJPYTFneVVuQlpla0pyU1ZjME5GZ3lV
WGRrTWpWelRVUlNhMDB5VW1aUApWMGt4VDFkSmVrNVhUamxEWnowOUNnPT0K

└─$ cat enc_flag|base64 -d|base64 -d|base64 -d|base64 -d
Y0dsamIwTlVSbnRpWVhObE5qUmZiak56ZEROa1gyUnBZekJrSVc0NFgyUXdkMjVzTURSa00yUmZP
V0kxT1dJek5XTjlDZz09Cg==

└─$ cat enc_flag|base64 -d|base64 -d|base64 -d|base64 -d|base64 -d
cGljb0NURntiYXNlNjRfbjNzdDNkX2RpYzBkIW44X2Qwd25sMDRkM2RfOWI1OWIzNWN9Cg==

└─$ cat enc_flag|base64 -d|base64 -d|base64 -d|base64 -d|base64 -d|base64 -d
picoCTF{base64_n3st3d_dic0d!n8_d0wnl04d3d_9b59b35c}
```

Flag: `picoCTF{base64_n3st3d_dic0d!n8_d0wnl04d3d_9b59b35c}`
