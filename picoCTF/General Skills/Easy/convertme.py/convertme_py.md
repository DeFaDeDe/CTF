# convertme.py

![image.png](images/image.png)

If we run the program, we will see that we are asked to convert the given decimal number to binary

```bash
└─$ python convertme.py 
If 26 is in decimal base, what is it in binary base?
Answer:
```

To do this, we can use the python built-in `bin()` function to convert it to binary, in this case, it is `11010`

```bash
└─$ python
>>> bin(26)
'0b11010'
```

Entering the correct binary value will gives us the flag

```bash
└─$ python convertme.py 
If 26 is in decimal base, what is it in binary base?
Answer: 11010
That is correct! Here's your flag: picoCTF{4ll_y0ur_b4535_722f6b39}
```

Flag: `picoCTF{4ll_y0ur_b4535_722f6b39}`
