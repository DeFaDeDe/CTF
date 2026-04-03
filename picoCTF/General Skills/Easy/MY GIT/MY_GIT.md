# MY GIT

![image.png](images/image.png)

Reading the instruction we will find that we need to commit under some restrictions found in README.md

```bash
# MyGit

### If you want the flag, make sure to push the flag!

Only flag.txt pushed by ```root:root@picoctf``` will be updated with the flag.

GOOD LUCK!

```

We can find create a flag.txt 

```bash
└─$ touch flag.txt
```

Then configure so that we will impersonate `root:root@picoctf`

```bash
└─$ git config user.name 'root'                                        
                                                                                                                                                                                                    
└─$ git config user.email 'root@picoctf'
```

Finally we commit the changes

```python
                                                                                                                                                                                                
└─$ git add .                           
                                                                                                                                                                                                    
└─$ git commit -m 'Get flag'                            
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 flag.txt
                                                                                                                                                                                                    
└─$ git push                
.
.
.
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 8 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 261 bytes | 261.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Author matched and flag.txt found in commit...
remote: Congratulations! You have successfully impersonated the root user
remote: Here's your flag: picoCTF{1mp3rs0n4t4_g17_345y_05f9a904}

```

Flag: `picoCTF{1mp3rs0n4t4_g17_345y_05f9a904}`
