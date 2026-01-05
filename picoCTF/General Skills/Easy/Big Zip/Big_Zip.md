# Big Zip

![image.png](images/image.png)

Welp there are too many files

```bash
└─$ ls|wc -l
759
```

To `grep` recursively, use the `-r` flag, and we will find the flag

```bash
└─$ grep -ir 'picoCTF{' *                                                                                                                                                                                                                  
folder_pmbymkjcya/folder_cawigcwvgv/folder_ltdayfmktr/folder_fnpfclfyee/whzxrpivpqld.txt:information on the record will last a billion years. Genes and brains and books encode picoCTF{gr3p_15_m4g1c_ef8790dc}
```

Alternatively, you can use `find` and then use `strings` on all of the file, and `grep` the result, but it is way slower than `grep` in this case.

```bash
└─$ find . -type f -exec strings {} \;|grep 'picoCTF{'
information on the record will last a billion years. Genes and brains and books encode picoCTF{gr3p_15_m4g1c_ef8790dc}
```
