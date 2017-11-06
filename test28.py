# -*- coding: utf-8 -*-
# Author: 小狼狗
'''
==========================================================
                    itertools
==========================================================
'''
import random
import itertools
import sys
# # 从a~d中取出不重复的三个字母
# print(random.sample(['a', 'b', 'c', 'd'], 3))
# # ['d', 'b', 'c']
#
# a = [5, 3, 1, 3, 4, 7, 11]
# d = []
# for b in itertools.combinations(a[2:], a[1]):  #从m个元素中选取n个（不放回）
#     c = []
#     b = list(b)
#     b.sort()
#     for i in range(len(b)-1):
#         c.append(b[i+1] - b[i])
#     x = min(c)
#     d.append(x)
# M = max(d)
# print(M)


import itertools
l = [1,2,3,4]
#有序
a = itertools.permutations(l,3)
for i in a:
    print(i)
print('  ')
#无序
a = itertools.combinations(l,3)
for i in a:
    print(i)
