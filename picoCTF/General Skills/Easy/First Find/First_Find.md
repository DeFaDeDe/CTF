# First Find

![image.png](images/image.png)

Because all we want to find is the file called `uber-secret.txt`, we can just use `find` and specify the name, and then read the content using `strings`

```bash
└─$ find . -name 'uber-secret.txt' -exec strings {} \;                                                                                                                                                                                     
picoCTF{f1nd_15_f457_ab443fd1}
```

Additionally, we can locate where is the file using `locate`

```bash
└─$ locate 'uber-secret.txt'
First find/files/adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/uber-secret.txt

```

Because the zip isn’t that big, using `tree` is also an option. But we need to include the `-a` to show hidden files

```bash
└─$ tree -a
.
├── 13771.txt.utf-8
├── 14789.txt.utf-8
├── acceptable_books
│   ├── 17879.txt.utf-8
│   ├── 17880.txt.utf-8
│   └── more_books
│       └── 40723.txt.utf-8
├── adequate_books
│   ├── 44578.txt.utf-8
│   ├── 46804-0.txt
│   └── more_books
│       ├── 1023.txt.utf-8
│       └── .secret
│           └── deeper_secrets
│               └── deepest_secrets
│                   └── uber-secret.txt
└── satisfactory_books
    ├── 16021.txt.utf-8
    ├── 23765.txt.utf-8
    └── more_books
        └── 37121.txt.utf-8

10 directories, 12 files
```

Flag: `picoCTF{f1nd_15_f457_ab443fd1}`
