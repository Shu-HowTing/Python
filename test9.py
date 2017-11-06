#列表
"""
#与字符串相比，列表的特点：列表的内容可以类型不同 ；列表是可变的
lst = [1, 2, 3, "hello ", 4.5  ]
print(lst[3], lst[4])
print(lst + [6, 7]) #lst本身不变
lst.append(8)  #lst改变
print(lst.append(8)) #注意区别 结果 None
print(lst)
lst.pop() #不指明删除某个元素，默认最后一个
print(lst)
lst.pop(3)
print(lst)
lst1 = [1,6,3,5,2,9]
lst1.sort()
print(lst1)
lst1.reverse()
print(lst1)
print(max(lst1))

#输入10个数，求均值
nums = []
for i in range(10):
    nums.append(float(input()))
avg = sum(nums) / len(nums)
print(avg)
"""
"""
# 注意区别一下两种情况
a = [1, 2, 3, 4]
b = a #类似于C++中的引用
b[1] = 8
print(a)
b = a[:]
b[1] = 9
print(a)

#交换两个数
def swap(lst ,a, b):
    temp = lst[a]
    lst[a] = lst[b]
    lst[b] = temp

lst = [1, 2, 3, 4]
swap(lst, 0, 1)
print(lst)


def f(lst):
    lst = [2,3,4]  #这一步相当于解引用
lst = [1, 2, 3]
f(lst)
print(lst)
"""
"""
#查找
def search(lst, x):
    for i in range(len(lst)):
        if lst[i] == x:
            return i

lst = [1, 3, 5, 6, 7 ]
i = search(lst, 6)
print(i)

#二分法查找 时间复杂度O(log2(n))
# 实行二分查找时，必须排序
def bi_searh(lst, x):
    low = 0
    high = len(lst) - 1
    while low <= high:
        i = int((low + high) / 2)
        if x == lst[i]:
            return i
        elif x < lst[i]:
            high = i
        else:
            low = i
lst = [2, 4, 5, 6, 7, 9]
print(bi_searh(lst, 7))


#排序（sort）
#选择排序法 :一
def selection_sort(lst):
    for i in range(len(lst)):
        min_index = i
        for j in range (i+1, len(lst)):
            if lst[j] <= lst[min_index]:
                min_index = j
        lst.insert(i, lst.pop(min_index))

lst = [9, 5, 7, 3, 6, 2, 8]
selection_sort(lst)
print(lst)
#选择排序法 :二
def swap(lst,i,j):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp

def selection_sort(lst):
    for i in range(len(lst)):
        min_index = i
        for j in range (i+1, len(lst)):
            if lst[j] <= lst[min_index]:
                min_index = j
        swap(lst,i,min_index)

lst = [9, 5, 7, 3, 6, 2, 8]
selection_sort(lst)
print(lst)

#冒泡排序
def bubble_sort(lst):
   for i in range(len(lst)):
        for j in range(len(lst) - 1):
            if lst[j] > lst[j + 1]:
                swap(lst, j, j + 1)
lst = [11, 5, 7, 9, 6, 2, 4]
bubble_sort(lst)
print(lst)

#自带的排序函数
lst = [11, 5, 7, 9, 6, 3, 4]
lst.sort()
print(lst)
"""
"""
#列表的嵌套/二维数组
lst = [[1, 2, 3],
       [3, 4, 5],
       [6, 7, 8]]
print(lst)
print(len(lst))
print(lst[2][1])

students = [['Zhang',84],['Wang',98],['Li',76]]
s = 0
for student in students:
    s += student[1]
print(s / len(students))

#列表解析
print(sum([x[1] for x in students]) / len(students))

lst1 = [1, 2, 3, 4]
lst2 = [x ** 2 for x in lst1]
print(lst2)

#求因数和
x = int(input("x = "))
lst = [i for i in range(1,x + 1)if x % i == 0]
print(sum(lst))
"""

students = [['Zhang',84],['Wang',98],['Li',76]]
# def f(a):
#     return a[1]
# #students.sort(key = f,reverse = False)
students.sort(key = lambda x: x[1],reverse = True)

print(students)

#元组
t = (1,2,"my",5)
print(t)
a = 1
b = 2
(a, b) = (b, a)
print(a,b)

def max_min(lst):
    min = max =lst[0]
    for i in(lst):
        if i < min:
            min = i
        if i > max:
            max = i
    return (min, max)
lst = [8, 4, 5, 6, 2, 0, 1]
print(max_min(lst))

lst = ["abc","bcfd","arfgj","weqweoqeo"]
lst.sort(key = lambda x: len(x),reverse = True)
print(lst)