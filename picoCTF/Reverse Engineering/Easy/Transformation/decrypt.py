#''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
enc='灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸形㝦㘲捡㕽'
for i in enc:
    first_char=chr(ord(i)>>8)
    second_char=chr(ord(i)-(ord(first_char)<<8))
    print(first_char+second_char, end='')
