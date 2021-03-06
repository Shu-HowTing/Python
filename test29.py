# -*- coding: utf-8 -*-
# Author: 小狼狗

# class T():
#     '''hello'''
#     a = 10
#     def __init__(self,n):
#         self.b = n
#         self.c = self.a
#     def asd(self):
#         self.d = self.b
#         #print(d)
# A = T(6)
# print(A.c)
# A.asd()
# print(A.d)

''' 问题：如何分割一个序列中的连续整数'''
import numpy as np

def group_consecutive(a):
    return np.split(a, np.where(np.diff(a) != 1)[0] + 1)

a = [1, 2, 3, 7, 8, 9, 10, 100, 101,102 ]
l = group_consecutive(a)
print(l)

'''
    np.split(ary,indices_or_sections,axis=0)
        ary:拆分对象
        indices：索引，当为整数n的时候，会把数组拆分为n个部分，不能整除会报错；
                 当为数组的时候，指定的就是拆分的点；

        axis： 按照指定的坐标轴拆分
'''
l = np.split(a, [3,5])
print(l)    #[array([1, 2, 3]), array([7, 8]), array([ 9,  10, 100, 101, 102])]


'''
    np.where(condition, x=None, y=None)

        格式
            numpy.where(condition[, x, y])
        参数
            condition : array_like, bool
            if conditon == True:
            取当前位置的x的值
            else：
            取当前位置的y的值
        返回值
            返回一个数组，或者由数组组成的元组
            根据定义条件返回元素，这些元素或者从x中获得，或者从y中获得。
            如果只给出条件，没有给出[,x, y]，返回条件中非零（True）元素的坐标。

    '''
a = np.array([1, 2, 0, 4, 0, 5])
l = np.where(a>2)
print(l)  #(array([3, 5], dtype=int64),)
print(a[l])
x = np.arange(9.).reshape(3, 3)
np.where(x < 5, x, -1)               # 值替换
# array([[ 0.,  1.,  2.],
#        [ 3.,  4., -1.],
#        [-1., -1., -1.]])

'''
    np.diff(a, n=1, axis=-1)
        对a序列做差分
        a: 输入的序列
        n: n阶差分，即：做几次差分

'''
l = np.diff([1, 2, 0, 4, 0, 5])
print(l)    #[ 1 -2  4 -4  5]

l = np.diff([1, 2, 0, 4, 0, 5], 2)
print(l)    #[-3  6 -8  9]















