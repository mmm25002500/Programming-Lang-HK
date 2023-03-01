import struct

# 1-a
factor = []

for i in range(1, 100):
    if 100 % i == 0:
        factor.append(i)

with open('factors.txt', 'w') as f:
    for i in factor:
        f.write(str(i) + ', ')

# 1-b
factor = []
with open('factors.txt', 'r') as f:
    factor = f.read().split(', ')

Sum = 0
for i in factor[:-1]:
    Sum += int(i)
print('其總和為:', Sum)

# 1-c
with open('factors.bin', 'wb') as f:
    for ft in factor[:-1]:
        f.write(struct.pack('i', int(ft)))

# 1-d
with open('factors.bin', 'r') as f:
    factor = f.read().split(', ')
    Sum = 0
    for i in factor[:-1]:
        Sum += int(i)
    print('其總和為:', Sum)

# 2
s = '去年今日此門中，人面桃花相映紅'
encoded = s.encode('utf-8')
decoded = encoded.decode('utf-8')

print("原來：", s)
print("編碼：", encoded)
print("解碼：", decoded)

# 3
# barr = b'\x0c&@\xfc'
# decoded = barr.decode('ascii')
# print("Decoded string:", decoded)
# num_list = list(barr)
# print("List of numbers:", num_list)
# An Error Occur

# 4
try:
    b'\x04\xeb\x12'.decode('utf-8')
except UnicodeDecodeError:
    print('utf-8解碼錯誤')

# 5
import math
try:
    x = float(input('請輸入一個正數：'))
    if x < 0:
        raise ValueError('不能輸入負數')
    print('開根號結果為：', math.sqrt(x))
except ValueError as e:
    print(e)
except:
    print('必須輸入數字')
    
# 6-a
import math_module1

factors_50 = math_module1.factors(50)
primes_100 = math_module1.primes(100)

print(factors_50)
print(primes_100)

# 6-b
# 跟 6-1 一樣