# -*- coding: utf-8 -*-
# Author: 小狼狗

from functools import reduce
from functools import wraps
'''匿名函数:lambda, '''
'''
lambda 函数
    lambda args: expression
    :args 以逗号分隔的参数列表
    :expression 表达式
    lambda语句定义的代码必须是表达式，而不能是多条件语句，比如for和while语句
'''
f = lambda x,y: x+y
print(f(3,4))
f1 = lambda x,y,z=10: x+y+z
print(f1(3,4))

'''
函数式编程：
    filter(func, seq)：调用一个布尔函数来迭代遍历seq中的元素，返回一个使func返回值是True的元素的列表
    map(func, seq1, seq2...): 将函数func映射于给定的序列的每一个元素，并用一个列表来提供返回值
    reduce(func， seq, init):将一个二元函数作用于序列的元素，每次携带一对（先前的结果和下一个元素）带入函数，最后将序列减少为一个返回值
'''

def fun1(x):
    if x>10:
        return True
    else:
        return False
l = [1, 3, 20, 4, 14, 25]
s = list(filter(fun1, l))     # filter返回的结果是一个迭代器，如果要显示可以用for语句，也可以转成list
print(s) #[20, 14, 25]
# s = list(s)
# print(s)

def f2(x):
    return x*2
l1 = [1, 3, 4, 6, 3]
l2 = list(map(f2, l1))   # map返回的也是一个迭代器对象
print(l2)

def f2(x, y):
    return x*2, y*2
l3 = ['s', 'd', 'q', 'a', 'f']
l2 = list(map(f2, l1, l3))
print(l2)   #[(2, 'ss'), (6, 'dd'), (8, 'qq'), (12, 'aa'), (6, 'ff')]

def f3(x, y):
    return x + y

l3 = reduce(f3, l1)  #l3是一个值
print(l3)

l4 = reduce(f3, l1, 2)
print(l3)


#函数闭包
def f1(x):
    def f2(y):
        return  x**y
    return f2
f3 = f1(2) # f3 = 2**y
print(f3(4))

def start_pos(x, y):
    def new_pos(m, n):
        print("The new position is ({}, {})".format(x+m, y+n))
    return new_pos
action = start_pos(10, 10)
action(2, 3)
action(3, 4)


#函数装饰器
'''
    装饰器本质上是一个Python函数，它可以让其他函数在不需要做任何代码变动的前提下增加额外功能，装饰器的返回值也是一个函数对象。
    它经常用于有切面需求的场景，比如：插入日志、性能测试、事务处理、缓存、权限校验等场景。
    装饰器是解决这类问题的绝佳设计，有了装饰器，我们就可以抽离出大量与函数功能本身无关的雷同代码并继续重用。
    概括的讲，装饰器的作用就是为已经存在的对象添加额外的功能。
装饰器：
    1.本身是一个函数，用于装饰其他函数
    2.功能：增强被装饰函数的功能
    3.装饰器一般接收一个函数作为参数，对其进行功能增强
缺点：
    原函数的元信息不见了，比如函数的docstring、__name__、参数列表，
    解决方法：functools.wraps，wraps本身也是一个装饰器，它能把原函数的元信息拷贝到装饰器函数中，这使得装饰器函数也有和原函数一样的元信息了
'''
def deco(func):
    def wrapper():
        print("please say something:")
        func()
        print("no zuo no die")
    return wrapper
@deco    # @符号是装饰器的语法糖，在定义函数的时候使用，避免再一次赋值操作
def show():
    '''show  something'''
    print("hello")
def say():
    print('hahahhahahaha')
show()

say() #hahahhahahaha 仅对紧跟着的函数作用
print(show.__name__)   #输出为wrapper，而不是show
print(show.__doc__)    #输出None，而不是show  something



def deco(func):
    @wraps(func)
    def wrapper():
        print("please say something:")
        func()
        print("no zuo no die")
    return wrapper
@deco    # @符号是装饰器的语法糖，在定义函数的时候使用，避免再一次赋值操作
def show():
    '''show  something'''
    print("hello")
show()
print(show.__name__)   #输出为show
print(show.__doc__)    #输出为show  something



