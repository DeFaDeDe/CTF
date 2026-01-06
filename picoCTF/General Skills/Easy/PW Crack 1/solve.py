from pwn import xor

password='1e1a'
with open('level1.flag.txt.enc','r') as f:
    encrypted=f.read()
    flag=xor(encrypted,password)
    print(flag.decode('utf-8'))
