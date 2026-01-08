# fixme1.py

![image.png](images/image.png)

It is always a good idea to run the code and how it behaves (if you are sure it is not a malicious code of course)

If we try to run the code, we will see there is an indentation error

```bash
└─$ python fixme1.py
.
.
.
    print('That is correct! Here\'s your flag: ' + flag)
IndentationError: unexpected indent
```

To print the flag, remove the indentation before the `print()`, and we can get the flag

```bash
└─$ python fixme1.py 
That is correct! Here's your flag: picoCTF{1nd3nt1ty_cr1515_09ee727a}
```

Flag: `picoCTF{1nd3nt1ty_cr1515_09ee727a}`
