# -*- coding: utf-8 -*-
# Author: 小狼狗

'''
类的基本使用方法
'''
class Person:
    def __init__(self, na, gen, age, fig):
        self.name = na
        self.gender = gen
        self.age = age
        self.fight = fig

    def grassland(self):
        """注释：草丛战斗，消耗200战斗力"""

        self.fight = self.fight - 200

    def practice(self):
        """注释：自我修炼，增长100战斗力"""

        self.fight = self.fight + 200

    def incest(self):
        """注释：多人游戏，消耗500战斗力"""

        self.fight = self.fight - 500

    def detail(self):
        """注释：当前对象的详细情况"""

        temp = "姓名:%s ; 性别:%s ; 年龄:%s ; 战斗力:%s" % (self.name, self.gender, self.age, self.fight)
        print(temp)


# #####################  开始游戏  #####################

cang = Person('苍井井', '女', 18, 1000)  # 创建苍井井角色
dong = Person('东尼木木', '男', 20, 1800)  # 创建东尼木木角色
bo = Person('波多多', '女', 19, 2500)  # 创建波多多角色

cang.incest()  # 苍井空参加一次多人游戏
dong.practice()  # 东尼木木自我修炼了一次
bo.grassland()  # 波多多参加一次草丛战斗

# 输出当前所有人的详细情况
cang.detail()
dong.detail()
bo.detail()

cang.incest()  # 苍井空又参加一次多人游戏
dong.incest()  # 东尼木木也参加了一个多人游戏
bo.practice()  # 波多多自我修炼了一次

# 输出当前所有人的详细情况
cang.detail()
dong.detail()
bo.detail()


# -*- coding:utf-8 -*-
#继承
class D:
    def bar1(self):
        print('D.bar')


class C(D):
    def bar2(self):
        print('C.bar')


class B(D):
    def bar3(self):
        print('B.bar')


class A(B, C):
    def bar4(self):
        print('A.bar')

a = A()
a.bar2()
a.bar1()


# Python “鸭子类型”
class F1:
    pass


class S1(F1):
    def show(self):
        print('S1.show')


class S2(F1):
    def show(self):
        print('S2.show')


def Func(obj):
    obj.show()


s1_obj = S1()
Func(s1_obj)

s2_obj = S2()
Func(s2_obj)


class Province:
    # 静态字段
    country = '中国'

    def __init__(self, name):
        # 普通字段
        self.name = name


# 直接访问普通字段
obj = Province('河北省')
print(obj.name)

# 直接访问静态字段
print(Province.country)
print(obj.country)


class Foo:
    def func(self):
        pass

    # 定义属性
    @property
    def prop(self):
        pass


# ############### 调用 ###############
foo_obj = Foo()

foo_obj.func()
foo_obj.prop # 调用属性

