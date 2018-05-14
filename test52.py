# -*- coding: utf-8 -*-
# Author: 小狼狗

'''
   quicksort: 找到轴点，递归排序    L    U    G
             Rank mi = partition(lo, hi-1)
             quicksort(lo, mi)
             quicksort(mi+1, hi)
  轴点 (pivot):左/右侧的元素，均不比它大/小
'''

#L = [6, 3, 8, 2, 5, 9, 4, 5, 1, 7]
#L = [3,6,1,2,5,7,0,4,19,45,32,98,15]

def partition(L, lo, hi):
    #lo = 0
    #hi = len(L)-1
    pivot = L[lo]
    while lo < hi:
        while lo < hi and L[hi] >= pivot:
            hi-=1
        L[lo] = L[hi]
        while lo < hi and L[lo] < pivot:
            lo+=1
        L[hi] = L[lo]
    else:
        L[lo] = pivot
        mi = lo

    return mi

def quicksort(L, lo, hi):
    if hi > lo:
        mi = partition(L, lo, hi)
        quicksort(L, lo, mi-1)
        quicksort(L, mi+1, hi)
    else:
        return

if __name__=='__main__':
    L = [6, 3, 8, 2, 5, 9, 4, 5, 1]
    lo = 0
    hi = len(L)-1
    quicksort(L, lo, hi)
    print(L)


#============================================================
'''
   partiton的变种算法 O(n)
   L  G  U
'''
#============================================================
def quick_sort(array, l, r):
    if l < r:
        q = partition(array, l, r)
        quick_sort(array, l, q - 1)
        quick_sort(array, q + 1, r)

def partition(array, l, r):
    pivot = array[l]
    mi = l
    for j in range(l+1, r):
        if array[j] <= pivot:
            mi += 1
            array[mi], array[j] = array[j], array[mi]
    array[mi], array[l] = array[l], array[mi]
    return mi

if __name__=='__main__':
    L = [6, 3, 8, 2, 5, 9, 4, 5, 1, 7, 10,25,23,13,104,28,]
    lo = 0
    hi = len(L)
    quicksort(L, lo, hi)
    print(L)