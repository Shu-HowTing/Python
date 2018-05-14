# -*- coding: utf-8 -*-
# Author: 小狼狗

'''
"=="和"is"的区别
    官方文档中说 is 表示的是对象标示符（object identity），而 == 表示的是相等（equality）。
    is 的作用是用来检查对象的标示符是否一致，也就是比较两个对象在内存中的地址是否一样，而 == 是用来检查两个对象是否相等。
    我们在检查 a is b 的时候，其实相当于检查 id(a) == id(b)。而检查 a == b 的时候，实际是调用了对象 a 的 __eq()__ 方法，a == b 相当于 a.__eq__(b)。
    一般情况下，如果 a is b 返回True的话，即 a 和 b 指向同一块内存地址的话，a == b 也返回True，即 a 和 b 的值也相等。

'''
a = "hello"
b = "hello"
print(a is b)  # 输出 True
print(a == b)  # 输出 True
print(id(a))
print(id(b))
c = 5
print(c is 5)

