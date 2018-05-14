# -*- coding: utf-8 -*-
# Author: 小狼狗
'''
访问限制:
    如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，
    在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问

    在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，
    不是private变量，所以，不能用__name__、__score__这样的变量名。
    有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，
    但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。
'''

class Student():
    def __init__(self,name,score,age):
        self.__name = name
        self.__age = age
        self.__score = score
    def get_score(self):
        return self.__score

Lily = Student("Lily", 60, 20)
print(Lily.get_score())
print(Lily._Student__score)

#### 注意下面的错误写法
# 表面上看，外部代码“成功”地设置了__name变量，但实际上这个__name变量和class内部的__name变量不是一个变量！
# 内部的__name变量已经被Python解释器自动改成了_Student__name，而外部代码给bart新增了一个__name变量
Lily.__score = 80
print(Lily.get_score())

class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1
# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')

class Student():

    __slots__ = ('name', 'age','score','gender')  # 用tuple定义允许绑定的属性名称
    def __init__(self,name,score,age):
        self.name = name
        self.age = age
        self.score = score
    def get_score(self):
        return self.score

Lily = Student("Lily","20","80")
Lily.gender = "F"
