with open('not_fl4g.txt', 'r') as file:
    content = file.read()
    print(' '.join(str(ord(x)) for x in content))

