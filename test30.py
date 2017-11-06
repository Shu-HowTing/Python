# -*- coding: utf-8 -*-
# Author: 小狼狗
def get_content():
    print('hello world')
def foo(bar):
    print(bar())
    return bar
func = foo(get_content)



#构造函数对象,有__call__方法的即为函数对象，当函数被被调用的时候会执行
class Foo():
    def __init__(self,name):
        self.name = name
        print('hello')
    def __call__(self, n, **kwargs):
        print('Hi',self.name)
        print(n)
f = Foo('python')
f(1)

#用函数对象构造装饰器
class Make_bold():
    def __init__(self,func):
        print('Initialize')
        self.func = func
    def __call__(self):
         print("Call")
         return '<b>{}<b>'.format(self.func())
@Make_bold
def a():
    return ("hello world")
print(a())
