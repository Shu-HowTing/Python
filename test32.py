# -*- coding: utf-8 -*-
# Author: 小狼狗

'''用实验估计 e 的值 (e = 2.718...)'''
import random
import numpy as np
# l = np.arange(100)
# #random.shuffle(l)
# p = q = i = 0
# while i < 10000:
#     random.shuffle(l)
#     for index, c in enumerate(l):
#         if index == c:
#             p += 1
#             break
#     else:
#         p += 1
#         q += 1
#     i += 1
# print(p/q)


l = []
for i in range(10000): # 实验次数
    n = 2
    x = random.random()  #生成一个(0-1)的随机数
    y = random.random()  #生成一个(0-1)的随机数
    while (x + y  < 1):
        n += 1
        x += y
        y = random.random()
    l.append(n)          #记录每次加到第几个数时，和大于1

print(sum(l)/10000)



