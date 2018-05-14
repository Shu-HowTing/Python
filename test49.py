# -*- coding: utf-8 -*-
# Author: 小狼狗

'''
    关于python一些知识点的理解
'''

#查看python的一些关键字
import keyword
print(keyword.kwlist)

#运算优先级
print(3*1**3)  #3

# is 比较的是对象的内存，区别 '=='
a = 300
b = 300
print(a is b)

#操作符重载的概念
def func(a):
    a = a + '2'
    a = a*2
    return a
print(func('hello'))

#在Python中，表达式 0.1 + 0.2 == 0.3 的返回是？
print(0.1 + 0.2 == 0.3)  #False
'''
在Python中，数值对象都是用二进制来表示的，浮点数也不例外，但不是所有的浮点数都能用二进制精确表示的。
一个浮点数转化为二进制就是是不断的乘2，取其中的整数部分，例如：
    (1) 0.1*2 = 0.2,  整数部分为0，小数部分为0.2
    (2) 0.2*2 = 0.4 , 整数部分为0，小数部分为0.4
    (3) 0.4*2 = 0.8 , 整数部分为0，小数部分为0.8
    (4) 0.8*2 = 1.6,  整数部分为1，小数部分为0.6
    (5) 0.6*2 = 1.2,  整数部分为1，小数部分为0.2
   重复第2步
所以0.1的二进制表示就是0.0 0011 0011 0011 ···，计算机没法精确表示这个浮点数，所有就造成了误差。
'''

#表达式 ~~~5 的值是多少？
print(~~~5)
####“~x”的结果为“ -（x+1）”  ~~~5 = ~5, 所以结果为-6

#表达式 bool(‘False’) 的返回值是：
print(bool('False'))    #True
#'False'是一个字符串，当bool运算接受一个非空的字符串时，返回True

#表达式 True==False==False 的返回值是：
print(True==False==False)   #True
#链式比较中，True==False==False 等价于 (True==False) and (False==False)
print(1<2<4)  # True
#相当于 (1<2) and (2<4)

#下面这段程序的指向结果为：#0 1 2
i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
else:
    print(0)
#while和else是一个层级的循环，当i>=5时，会执行else;
#但是由于提前执行了break，跳出了循环，所以不执行else

#下面表达式输出结果为：
x = 12
def f1():
    x = 3
    print(x)
def f2():
    x += 1
    print(a)
def f3():
    a = x + 1
    print(a)
f1()   # 3
f2()  # 报错
f3()   # 13











