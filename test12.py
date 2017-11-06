#import 模块
# import time
# print(time.localtime())
#
# import time as t
# print(t.localtime())
#
# from time import localtime
# print(localtime())
#
# from time import *  #引入模块的所有功能
# print(localtime())

#import test11
# import test9
#
# lst = test9.max_min([9, 6, 5, 4, 0, 3])
# print(lst)
#
# #TRY
# try:
#     f = open("eee.txt","r+")
# except Exception as e: #将错误存放在e中
#     print(e)
#     response = input("Do you want to creat this file(y/n):")
#     if response == 'y':
#         f = open("eee.txt","w")
#     else:
#         pass
# else:
#     f.write("hello world")
#     f.close()

#lamda  zip  map
a = [1, 2, 3]
b = [3, 4, 5]
ab = zip(a,b)
print(list(ab))

fun= lambda x,y:x+y
x=int(input('x='))    #这里要定义int整数，否则会默认为字符串
y=int(input('y='))
print(fun(x,y))



def fun(x,y):
	return (x+y)
print(map(fun,[1],[2]))


print(list(map(fun,[1,2],[3,4])))

#id取地址
a = [1,2,3]
b = a  #引用
print(id(a))

print(id(a) == id(b))
 # True



