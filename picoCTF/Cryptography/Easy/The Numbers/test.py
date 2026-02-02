list = [16,9,3,15,3,20,6,'{',20,8,5,14,21,13,2,5,18,19,13,1,19,15,14,'}']
for element in list:
    if type(element)==int:
        print(chr(97+element-1), end='')
    else:
       print(element, end='')

