import hashlib
num='0'
result=hashlib.md5(num.encode())
print(f'0: http://10.48.170.58/{result.hexdigest()}')
num2='14'
result2=hashlib.md5(num2.encode())
print(f'14: http://10.48.170.58/{result2.hexdigest()}')
