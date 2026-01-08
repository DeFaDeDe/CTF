# fixme2.py

![image.png](images/image.png)

If we run the code, we will see that it should be `==`(comparison operator) instead of `=`(assignment operator), which is very common in if-conditions

```bash
└─$ python fixme2.py 
.
.
.
    if flag = "":
       ^^^^^^^^^
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
```

Adding a `=` so that it becomes `if flag == "":`, and we are done

```bash
└─$ python fixme2.py 
That is correct! Here's your flag: picoCTF{3qu4l1ty_n0t_4551gnm3nt_e8814d03}
```

Flag: `picoCTF{3qu4l1ty_n0t_4551gnm3nt_e8814d03}`
