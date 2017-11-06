#递归调用

"""
#阶乘
def fun(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fun(n-1)

n = int(input("n ="))
print("%d! = %ld" %(n, fun(n)))


#汉诺塔
count = 0
def hanoi(n, A, B, C):
    global count
    if n == 1:
        print("Move" , n, "from", A,"to", C)
        count += 1
    else:
        hanoi(n-1, A, C, B)
        print("Move", n, "from", A, "to", C)
        count += 1
        hanoi(n-1, B, A, C)
n = int(input("n = "))
print(hanoi(n, "Left","Mid","Right"))
print(count)
"""

#停车问题
import random
def parking(low, high):
    if high - low <= 1:
        return 0
    else:
        x=random.uniform(low, high - 1)
        return parking(low, x) + 1 +parking(x + 1, high)
sum = 0
for i in range (0,10000):
    sum += parking(0, 5)
print(sum /10000.0)
