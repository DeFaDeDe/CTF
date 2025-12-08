# PerfectUser

![image.png](images/image.png)

Using Ghidra, you can see there are two conditions

![image.png](images/image%201.png)

The first condition is the input `1337`  in decimal as the second answer

The second condition will check the environment variable to see if `p3rf3ctr00t` is set to TRUE

```bash
└─$ export p3rf3ctr00t=TRUE                                                                                                                                                                                                                

└─$ ./perfetcuser                                                                                                                                                                                                                
What is your name? 
Hello, !
What is 13 + 37? 1337
Correct, see this: r00t{1234_welc0me_t0_th3_CTF!!}
```

Flag: `r00t{1234_welc0me_t0_th3_CTF!!}`
