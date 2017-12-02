# -*- coding: utf-8 -*-
# Author: 小狼狗
'''
=====================================================
                冒泡排序（bubblesort） O(n^2)
=====================================================
'''
#
# def bubblesort(a, n):
#     for i in range(n):
#
#         for j in range(n-1-i):
#             if a[j] > a[j+1]:
#                 a[j],a[j+1] = a[j+1],a[j]
#
#         #return a
# l = [2,6,3,9,1,7,19,12,15,11,10,9]
# bubblesort(l,len(l))
# print(l)

#-------------------改进-----------------------------
def bubblesort(a, n):
    for i in range(n):
        flag =True
        for j in range(n-1-i):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
                flag = False
        if flag == True:
            break
l = [1,2,3,7,6]
bubblesort(l,len(l))
print(l)



'''
===================================================
                    实现反转一个列表
===================================================
'''
l = [1, 3, 4, 5, 6, 7, 8]

def recursive_rev(alist):
     if len(alist) <= 1:
        return alist
     return [alist[-1]] + recursive_rev(alist[:-1])
a = recursive_rev(l)
print(a)
#最简单 pythonic
print(l[::-1])












