# -*- coding: utf-8 -*-
# Author: 小狼狗
'''
==================================================================
                        归并排序实现(Nlog(N))
==================================================================
'''
def merge(a, b):
    c = []
    h = j = 0
    while j < len(a) and h < len(b):
        if a[j] < b[h]:
            c.append(a[j])
            j += 1
        else:
            c.append(b[h])
            h += 1
    if j == len(a):
        for i in b[h:]:
            c.append(i)
    else:
        for i in a[j:]:
            c.append(i)
    return c

def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    middle = len(lists)//2
    left = merge_sort(lists[:middle])
    right = merge_sort(lists[middle:])

    return merge(left, right)

if __name__ == '__main__':
    a = [4,7,8,3,5,9,2,6]
    print(merge_sort(a))

#-------------------------------------------------------------
# from heapq import merge
# def merge_sort(seq):
#     if len(seq) <= 1:
#         return seq
#     else:
#         middle = len(seq) // 2
#     left = merge_sort(seq[:middle])
#     right = merge_sort(seq[middle:])
#     return list(merge(left, right))  # heapq.merge()
#
#
# if __name__ == "__main__":
#     seq = [10, 5, 8, 9, 14, 4, 7, 8, 3, 5, 9, 2]
#     print(merge_sort(seq))

l = [1,2,3,4]
def f(a):
    a[2] = 0
f(l)
print(l)