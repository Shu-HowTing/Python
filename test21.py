
# print(a)
# def good_append(new_item, a_list=None):
#     print(id(new_item))   #145
#     print(id(a_list))
#     if a_list == None:
#         a_list = []
#         print(id(a_list))
#     a_list.append(new_item)
#     print(id(a_list))
#     return a_list
# print(good_append(1))
# print(good_append(1))
# print(id(good_append))

# count = 10
# def fun():
#     count = 5
#     print(count)
#
# fun()
# print(count)
#
# count = 10
# def fun():
#     global count
#     count = 5
#     print(count)
#
# fun()
# print(count)
#
# def fun1():
#     print("fun1正在被调用。。。")
#     def fun2():
#         print("fun2正在被调用。。。")
#     fun2()
# fun1()
#
# def fun1():
#     x = 5
#     def fun2():
#         nonlocal x
#         x += x
#         return x
#     return fun2()
# print(fun1())

#lambda函数
# f = lambda x: 2 * x + 1
# print(f(5))
# f1 = lambda x,y :x+y
# print(f1(2,4))
#
# def odd(x):
#     return x %2
# temp = range(10)
# print(list(filter(odd, temp)))
# print(list(filter(lambda x: x%2, range(10))))
#
#递归
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
# result = factorial(5)
# print(result)
# #汉诺塔
# def hanoi(n, x, y, z):
#     if n == 1:
#         print(x, "-->", z)
#     else:
#         hanoi(n-1, x, z, y)
#         print(x, "-->", z)
#         hanoi(n-1, y, x, z)
# hanoi(5,'X','Y','Z')
#
#字典的索引
# dic = dict.fromkeys(range(10),"good")
# for key in dic.keys():
#     print(key)
# for value in dic.values():
#     print(value)
# for item in dic.items():
#     print(item)
#
# a = {1:'one', 2:'two', 3:'three', 4:'four'}
# a.pop(2) #'two'
# print(a) #{1: 'one', 3: 'three', 4: 'four'}
# b = {'小白':'dog'}
# a.update(b)
# print(a)  #{1: 'one', 3: 'three', 4: 'four', '小白': 'dog'}
#集合
#集合里面的元素是唯一的
set1 = {1,2,4,5,6,7,2,4,6,0}
print(set1) #{0, 1, 2, 4, 5, 6, 7}
#实践：去除列表中的重复元素
list1 = [1,2,4,5,6,7,2,4,6,0]
list1 = list(set(list1))
print(list1)  #[0, 1, 2, 4, 5, 6, 7]
f = open("file.txt")
for line in f:
    print(line)
f.close()
#











