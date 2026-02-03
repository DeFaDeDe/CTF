# strings it

![image.png](images/image.png)

As the title suggests, we can use `strings` on the file. However, there are too many lines

```bash
└─$ strings strings|wc -l
19243
```

Use with `grep` to locate the flag

```bash
└─$ strings strings|grep pico
picoCTF{5tRIng5_1T_1067EC4c}
```

Flag: `picoCTF{5tRIng5_1T_1067EC4c}`
