# Transformation

![image.png](Transformation/image.png)

We are given `enc ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])`, which is how enc(`灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸形㝦㘲捡㕽`) is formed.

We can see that in each loop, it steps 2, meaning that 2 characters are involved in each encrypted letter in enc.

As for the encryption process, the ASCII code of the first character is left shifted by 8 bits, then add the second character’s ASCII code

We can recover 2 characters at a time by first right-shifting 8 bits to obtain the first character, and then subtracting the right-shifted first character (just like during encryption) from the letter in enc. The code are the following:

```python
#''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
enc='灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸形㝦㘲捡㕽'
for i in enc:
    first_char=chr(ord(i)>>8)
    second_char=chr(ord(i)-(ord(first_char)<<8))
    print(first_char+second_char, end='')
```

Run the code to recover the flag.

Flag: `picoCTF{16_bits_inst34d_of_8_b7f62ca5}`