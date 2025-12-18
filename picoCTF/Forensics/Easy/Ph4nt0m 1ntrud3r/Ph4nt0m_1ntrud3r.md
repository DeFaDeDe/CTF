# Ph4nt0m 1ntrud3r

![image.png](Ph4nt0m%201ntrud3r/image.png)

Using strings, we can determine that there are base64 strings. We can try to decode them but they are invalid. 

```bash
└─$ strings myNetworkTraffic.pcap 
6wDoT88=A
bnRfdGg0dA==A
fQ==A
+TH2RiA=A
ZTFmZjA2Mw==A
KiZP+uA=A
mUKl4q4=A
BbzQg10=A
XzM0c3lfdA==A
ezF0X3c0cw==A
Qj9atMY=A
cGljb0NURg==A
UJddNj4=A
u1n7aWg=A
okKTBr8=A
ZDQkP3U=A
UBcZPyY=A
y88/pdA=A
MwbMYqQ=A
+RV8NVY=A
YmhfNHJfMg==A
lwFp5w0=
```

We can then take a look in Wireshark, we can see the time is very weird. TCP should send packets one by one, but apparent they are out of order

![image.png](Ph4nt0m%201ntrud3r/image%201.png)

Maybe then we need to sort by time? It is available on Wireshark, but I feel like tshark is a better tool in this case. In this case, we read(`-r`) the pcap file, Filter(`-Y`) outputs with tcp, show partial information instead of the whole packet(`-T`), with the `frame.time` and `tcp.segement_data` field selected(`-e`), then we can use sort to do the sorting. Finally, use sed to print the results after tab, which are the `tcp.segment_data`.

Feel free to play with tshark and sed for a better view. I did tried several times and reached to the full command

```bash
└─$ tshark -r myNetworkTraffic.pcap -Y tcp -T fields -e frame.time -e tcp.segment_data|sort|sed 's/.*\t//'                                                                                                                               
6f6b4b544272383d
7938382f7064413d
5a44516b5033553d
4d77624d5971513d
4b695a502b75413d
6d554b6c3471343d
2b5256384e56593d
5542635a5079593d
554a64644e6a343d
2b5448325269413d
3677446f5438383d
75316e376157673d
6c7746703577303d
42627a516731303d
516a3961744d593d
63476c6a62304e5552673d3d
657a46305833633063773d3d
626e52666447673064413d3d
587a4d3063336c6664413d3d
596d68664e484a664d673d3d
5a54466d5a6a41324d773d3d
66513d3d

```

We can then pipe the output to CyberChef, and the flag is right there

![image.png](Ph4nt0m%201ntrud3r/image%202.png)

Flag: `picoCTF{1t_w4snt_th4t_34sy_tbh_4r_2e1ff063}`