import base64

with open('enc_flag','r') as f:
    c=f.read()
    test1=base64.b64decode(c).decode('utf-8').strip('\n').strip('b\'').strip('\'')
    test2=base64.b64decode(test1).decode('utf-8')
    print(test2)
