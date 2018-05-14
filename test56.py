# -*- coding: utf-8 -*-
# Author: 小狼狗

# 堆排
import random

def MAX_Heapify(L, size, root):
    left = 2 * root + 1     #父节点的左节点
    right = left + 1        #父节点的右节点
    larger = root
    #将父节点与子及诶单进行比较,将最大的元素放到父节点上，并对得到的新的子树继续调整
    #迭代停止条件1.到达叶节点 or 2.父节点是最大元素
    if left < size and L[left] > L[larger]:
        larger = left
    if right < size and L[right] > L[larger]:
        larger = right
    if root != larger:
        L[root], L[larger] = L[larger], L[root]
        MAX_Heapify(L, size, larger)


def Build_Max_Heap(L):
    size = len(L)
    for i in range(size//2 - 1, -1, -1):    #第一个内部节点的rank = size//2 - 1
        MAX_Heapify(L, size, i)

def Heap_sort(L):
    Build_Max_Heap(L)                   #构造最大堆
    for i in range(len(L) - 1, -1, -1): #从后往前，与首元素交换位置，并且将首元素下滤，保证堆序性
        L[0], L[i] = L[i], L[0]
        MAX_Heapify(L, i, 0)


if __name__ == '__main__':
    L = [random.randint(1,100) for i in range(10)]  #随机产生10个0~100的数
    Build_Max_Heap(L)    #构造最大堆
    print(L)
    Heap_sort(L)         #进行堆排
    print(L)

