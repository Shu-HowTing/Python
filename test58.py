# -*- coding: utf-8 -*-
# Author: 小狼狗

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1(),f2(),f3())

def build(x, y):
    '''
    :param x:
    :param y:
    :return: x+y
    '''
    return lambda: x * x + y * y

f = build(3,4)
print(f())
print(build.__doc__)