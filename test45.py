# -*- coding: utf-8 -*-
# Author: 小狼狗
'''
=============================================================
                    斐波那契数列的计算
=============================================================
'''
import time
#递归方法 复杂度o(2^n)
def fib1(n):
    if n < 2:
        return n
    else:
        return fib1(n-1)+fib1(n-2)
t1 = time.time()
print(fib1(33))
t2 = time.time()
print("T1:{}".format(round(t2-t1,3)))

#动态规划 迭代方法
def fib2(n):
    g = 0
    h = 1
    for i in range(n-1):
        f = g + h
        g = h
        h = f
    return f
t1 = time.time()
print(fib2(33))
t2 = time.time()
print("T2:{}".format(round(t2-t1,3)))