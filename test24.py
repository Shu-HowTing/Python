# -*- coding: utf-8 -*-
#Author: 小狼狗

'''
yield
生成器的优势:
    节省存储空间
    更快的响应速度
    使用更加灵活
'''

#yield写法
# def gen(n):
#     for i in range(n):
#         yield i**2
#
# for i in gen(5):
#     print(i, ' ', end='') #0  1  4  9  16
#
# print('')
# #对比
# #普通写法
# def gen(n):
#     lst = [i**2 for i in range(n)]
#     return lst
#
# for i in gen(5):
#     print(i, ' ', end='') #0  1  4  9  16
#
# print('')
#
# # def foo():
# #     yield 1
# #     print("hello world")
# #     yield 2
# #
# # p = foo()            # p是一个生成器对象
# # print(p)             #<generator object foo at 0x000002634BC92468>
# # print(p.__next__())  #运行第一个yield返回的值，之后函数执行暂停
# # print(p.__next__())  #运行第二个yield返回值，中间有一句打印语句print("hello world")，先执行，然后打印返回的值2
# #
#
# def foo():
#     number = 0
#     while True:
#         val = yield number
#         print("hello world")
#         if val:
#             number = val
#         else:
#             number += 1
#
# p = foo()
# print(p.__next__())
# print(p.send(2))
# #print(p.__next__())

#斐波那契数列
# index = int(raw_input())
# def fib(n):
#     a, b = 1, 1
#     for i in range(n):
#         yield a
#         a, b = b, a + b
#
#
# a = []
# #print(type(p))
# for p in fib(index + 1):
#     a.append(p)
# print a[index]

# def fib():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b
#
# p = fib()
# print([p.__next__() for i in range(10)])

# def fib_re(n):
#
#     if (n < 1):
#         print("Wrong input! ")
#         return -1
#     else:
#         if (n == 1 or n == 2):
#             return 1
#         else:
#             return fib_re(n - 1) + fib_re(n - 2)
#
# n = int(raw_input())
# result = fib_re(n+1)
# if result != -1:
#     print result
# import math
# x = math.sqrt(5.0)
# a = (1 + x)/2.0
# b = (1 - x)/2.0
# def f(n):
#     return int(1.0/x * ((a**n) - (b**n)))
# n = int(raw_input())
# print(f(n+1))

import numpy as np
x = [1,2,3,4,5]
np.random.shuffle(x)
print(x)