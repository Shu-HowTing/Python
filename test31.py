# -*- coding: utf-8 -*-
# Author: 小狼狗
'''
=========================================================================
                        python对象
=========================================================================
'''

'''
    Python中所有的东西，注意，我是指所有的东西——都是对象。
    这包括整数、字符串、函数以及类。它们全部都是对象，而且它们都是从一个类创建而来.
    str是用来创建字符串对象的类;而int是用来创建整数对象的类。
    type就是创建类对象的类。你可以通过检查__class__属性来看到这一点
'''
a = 35
#print(type(a))
print(a.__class__)
#<class 'int'>
s = 'abc'
print(s.__class__)
#<class 'str'>



'''
元类就是用来创建类的“东西”。你创建类就是为了创建类的实例对象，不是吗？
但是我们已经学习到了Python中的类也是对象。好吧，元类就是用来创建这些类（对象）的，元类就是类的类，你可以这样理解 为：

MyClass = MetaClass()   #通过MetaClass创建一个类（对象）
MyObject = MyClass()    #通过MyClass创建一个对象（类的实例化）
'''
#type用来创建类

#type(类名, 父类的元组（针对继承的情况，可以为空），包含属性的字典（名称和值）)

class Foo(object):
    pass
'''
Python做了如下的操作：
    Foo中有__metaclass__这个属性吗？如果是，Python会在内存中通过__metaclass__创建一个名字为Foo的类对象（我说的是类对象，请紧跟我的思路）。
    如果Python没有找到__metaclass__，它会继续在Bar（父类）中寻找__metaclass__属性，并尝试做和前面同样的操作。
    如果Python在任何父类中都找不到__metaclass__，它就会在模块层次中去寻找__metaclass__，并尝试做同样的操作。
    如果还是找不到__metaclass__,Python就会用内置的type来创建这个类对象。
'''

'''
    元类的主要目的就是为了当创建类时能够自动地改变类。
    通常，你会为API做这样的事情，你希望可以创建符合当前上下文的类。
    假想一个很傻的例子，你决定在你的模块里所有的类的属性都应该是大写形式。
    有好几种方法可以办到，但其中一种就是通过在模块级别设定__metaclass__。
    采用这种方法，这个模块中的所有类都会通过这个元类来创建，我们只需要告诉元类把所有的属性都改成大写形式就万事大吉了。
'''
#__metaclass__实际上可以被任意调用，它并不需要是一个正式的类(下面就是一个函数的例子)
# 元类会自动将你通常传给‘type’的参数作为自己的参数传入
def upper_attr(future_class_name, future_class_parents, future_class_attr):
    '''返回一个类对象，将属性都转为大写形式'''
    #  选择所有不以'__'开头的属性
    attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))

    # 将它们转为大写形式
    uppercase_attr = dict((name.upper(), value) for name, value in attrs)

    # 通过'type'来做类对象的创建
    return type(future_class_name, future_class_parents, uppercase_attr)


#__metaclass__ = upper_attr
class Foo(object, metaclass = upper_attr):
    # __metaclass__ = upper_attr  python 2.x的写法
    # 我们也可以只在这里定义__metaclass__，这样就只会作用于这个类中
    bar = 'bip'

print(hasattr(Foo, 'bar')) #False

print(hasattr(Foo, 'BAR')) #True


#改成类的写法实现上面的功能
class UpperAttrMetaClass(type):
    # __new__ 是在__init__之前被调用的特殊方法
    # __new__是用来创建对象并返回之的方法
    # 而__init__只是用来将传入的参数初始化给对象
    # 你很少用到__new__，除非你希望能够控制对象的创建
    # 这里，创建的对象是类，我们希望能够自定义它，所以我们这里改写__new__
    # 如果你希望的话，你也可以在__init__中做些事情
    # 还有一些高级的用法会涉及到改写__call__特殊方法，但是我们这里不用
    def __new__(self, future_class_name, future_class_parents, future_class_attr):
        attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)
        return type(future_class_name, future_class_parents, uppercase_attr)

class Foo(object, metaclass = UpperAttrMetaClass):
    bar = 'bip'

print(hasattr(Foo, 'bar'))  # False

print(hasattr(Foo, 'BAR'))  # True


#但是，这种方式其实不是OOP。我们直接调用了type，而且我们没有改写父类的__new__方法。现在让我们这样去处理:

#这里的cls等价于普通类self，其实类方法的第一个参数总是表示当前的实例，不一定命名成self。可以自定义，但跟下文要一致。
class UpperAttrMetaclass(type):
    def __new__(cls, name, bases, dct):
        attrs = ((name, value) for name, value in dct.items() if not name.startswith('__'))
        uppercase_attr  = dict((name.upper(), value) for name, value in attrs)
        return type.__new__(cls, name, bases, uppercase_attr)

'''
元类的作用:
    1)拦截类的创建

    2)修改类

    3)返回修改之后的类
'''















