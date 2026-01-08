# Codebook

![image.png](images/image.png)

If you run the code with the codebook present, we can get the flag

```bash
└─$ python original_code.py 
picoCTF{c0d3b00k_455157_197a982c}
```

The code just extract some characters from the codebook and then apply XOR on the encrypted flag

```python
flag_enc = chr(0x13) + chr(0x01) + chr(0x17) + chr(0x07) + chr(0x2c) + chr(0x3a) + chr(0x2f) + chr(0x1a) + chr(0x0d) + chr(0x53) + chr(0x0c) + chr(0x47) + chr(0x0a) + chr(0x5f) + chr(0x5e) + chr(0x02) + chr(0x3e) + chr(0x5a) + chr(0x56) + chr(0x5d) + chr(0x45) + chr(0x5d) + chr(0x58) + chr(0x31) + chr(0x58) + chr(0x58) + chr(0x59) + chr(0x02) + chr(0x51) + chr(0x4c) + chr(0x5a) + chr(0x0c) + chr(0x13)
.
.
.
  try:
    codebook = open('codebook.txt', 'r').read()
    
    password = codebook[4] + codebook[14] + codebook[13] + codebook[14] +\
               codebook[23]+ codebook[25] + codebook[16] + codebook[0]  +\
               codebook[25]
               
    flag = str_xor(flag_enc, password)
    print(flag)
```

Which we can simplify the entire code using the xor function from pwntools

```python
from pwn import xor
    
try:
    codebook = open('codebook.txt', 'r').read()
    
    password = codebook[4] + codebook[14] + codebook[13] + codebook[14] +\
               codebook[23]+ codebook[25] + codebook[16] + codebook[0]  +\
               codebook[25]
    flag_enc = chr(0x13) + chr(0x01) + chr(0x17) + chr(0x07) + chr(0x2c) + chr(0x3a) + chr(0x2f) + chr(0x1a) + chr(0x0d) + chr(0x53) + chr(0x0c) + chr(0x47) + chr(0x0a) + chr(0x5f) + chr(0x5e) + chr(0x02) + chr(0x3e) + chr(0x5a) + 	    chr(0x56) + chr(0x5d) + chr(0x45) + chr(0x5d) + chr(0x58) + chr(0x31) + chr(0x58) + chr(0x58) + chr(0x59) + chr(0x02) + chr(0x51) + chr(0x4c) + chr(0x5a) + chr(0x0c) + chr(0x13)
    flag = xor(flag_enc,password).decode('utf-8')           
    print(flag)
    
except FileNotFoundError:
    print('Couldn\'t find codebook.txt. Did you download that file into the same directory as this script?')
```

Either way, we can get the flag

```bash
└─$ python solve.py                                                                                                                                                                                                                        
.
.
.
picoCTF{c0d3b00k_455157_197a982c}
```

Flag: `picoCTF{c0d3b00k_455157_197a982c}`
