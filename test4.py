"""
x=1
while x < 10:
    print(x)
    x += 1

#对0-10求和
sum=0
x=1
while (x <= 10):
    sum += x
    x += 1
print(sum)

#打印0-10之间的偶数，注意count+=1语句的位置
count=0
while count <= 10:
    if count%2 == 0:
       print(count)
    count+=1

count = 0
while count < 5:
    if count > 2:
        break
    print("hello world!")
    count+=1
print("===========")
count = 0
while count < 5:
    count += 1
    if count > 2:
        continue
    print("hello world!")
"""
#for 循环
"""
sum = 0
for i in range (11):
    sum += i
print ("sum=",sum)

import math
e = 1.0
t=1
for i in range(1,100):
    t *= i
    e=e + 1.0/t
print(e)

count=0
for i in range(100,1000):
    if i % 17 ==0:
        print(i)
        count+=1
print(count)

pi = 0
i = 1
k = 1.
for x in range(1,1000):
    pi+=4*i/k
    i=-i
    k+=2
print("pi = ",pi)

#卡拉兹猜想
for n in range(1,100):
    while n!=1:
        if n%2==0:
            n/=2
        else:
            n=3*n+1
    print(n)
    """
#九九乘法表

for i in range(1,10):
    for j in range (1,10):
        print("%d*%d=%2d" % (i, j, i * j), end=" ")
    print()









