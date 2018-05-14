# -*- coding: utf-8 -*-
# Author: 小狼狗
'''
错误处理
'''
# def maxpathnumber(node,row,col,mat):
#     count = 0
#     c = [x[1] for x in mat]
#     start = sum(range(node)) - sum(set(c))
#     for x in mat:
#         if x[0] == start:
#             count += 1
#             l.append(x[0])
#
#
#
# if __name__ == '__main__':
#     node = int(input())
#     row,col = [int(x) for x in input().split()]
#     M = []
#     for i in range(row):
#         M.append([int(x) for x in input().split()])
#     maxpathnumber(node, row, col, M)

# def foo(s):
#     n = int(s)
#     assert n != 0, 'n is zero!'
#     return 10 / n
#
# def main():
#     foo('0')
#
# main()

# class FooError(ValueError):
#     pass
#
# def foo(s):
#     n = int(s)
#     if n==0:
#         raise FooError('invalid value: %s' % s)
#     return 10 / n
# foo('0')

# import logging
# logging.basicConfig(level=logging.WARNING)

# s = '0'
# n = int(s)
# #logging.warn('n = %d' % n)
# print(10 / n)

