# Mod 26

![image.png](images/image.png)

If we read the values.txt, we will see a flag-like string, but not exactly the flag

```bash
└─$ cat values.txt
cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_45559noq}
```

The description hints that it uses ROT-13, which rotates each character by 13 positions. For example, a will become their difference is 13.

Take `c` as an example, we can place the letters a-z into an array in alphabetic order, where `c` is the third (3 assuming 1-origin indexing) character, so we can add 13 to it, resulting in 16, which maps to `p`.  There are some cases that might exceed 26 (No. of character), so that we can use the remainder of 26, in the case of `v`, it is (22+13)%26=9, which is `i`

We can convert it back by using `tr`. and for every uppercase and lowercase letter (a-zA-Z), transform it accordingly 

```bash
└─$ cat values.txt| tr a-zA-Z n-za-mN-ZA-M
picoCTF{next_time_I'll_try_2_rounds_of_rot13_45559abd}
```

Flag: `picoCTF{next_time_I'll_try_2_rounds_of_rot13_45559abd}`
