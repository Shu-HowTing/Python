# -*- coding: utf-8 -*-
# Author: 小狼狗
'''
================================================================
                selectionsort  O(n^2)
1.第一轮比较选出最小值
2.第二轮选出次小值
3.···
================================================================
'''
def selectSort(s):
    for i in range(0, len(s) - 1 ):
        index = i
        for j in range(i + 1, len(s)):
            if s[index] > s[j]:
                index = j
        s[i], s[index] = s[index], s[i]
l = [1, 34, 43, 21, 56, 12, 9 ]
selectSort(l)
print(l)


'''
================================================================
                insertsort  O(n^2)
================================================================
'''
def insertsort(s):
    for i in range(1, len(s)):
        key = s[i]
        for j in range(i-1, -1, -1):
            if key < s[j]:
                s[j+1] = s[j]
                s[j] = key

l = [2,9,3,5,1,7,38,24,31,21,11]
insertsort(l)
print(l)