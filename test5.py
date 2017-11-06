#二分法求开方
#此方法存在缺陷，如果想x<1,则无法计算出正确的结果
"""
x=float(input("x = "))
low=0.0
high=x
guss=(low+high)/2
while abs(guss**2 - x)>1e-4:

    if guss ** 2 > x:
        high = guss
    else:
        low = guss
    guss = (low + high) / 2
print(guss)

import math
a=math.sqrt(x)
print(a)
"""

"""
#判断prime
x = int(input("x ="))
for i in range (2,int(x/2)): #range 的范围必须是整数
    if x%i ==0:
        print("x is not a prime")
        break
else:
    print("x is  prime")

#判断50以内的素数
import  math
for k in range(3, 50):
    for i in range(2, int(math.sqrt(k))+1):
        if k % i == 0:
            break
    else:
        print(k,"is a prime")
"""
#判断回文数
#求X的逆序数是否等于X
num = int(input ("num ="))
num_t = num
num_p = 0
while num_t != 0:
    num_p = num_t % 10 + num_p * 10
    num_t = int(num_t / 10)
if num == num_p:
    print (num,"is palindrome")
else:
    print(num ,"is not palindrome" )

