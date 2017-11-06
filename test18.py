# #python 无处不是类
# #类的核心 ：封装 / 继承 / 多态
# #self  相当于 this 指针
# class People:
#     #静态变量a , b，不可以改变
#     a = 3
#     b = 4
#     def __init__(self,):
#         pass
#     def Name(self,name):
#         self.name = name
#     def printname(self):
#         print("My name is %s " % self.name)
#
# #继承 list就是一个类
# class Mylist(list):
#     pass
# lst = list()
# # 字典也是类
# dic = dict()
# lst = Mylist()
# lst.append(1)
# dic[1] = 'I'
# dic[2] = 'Love'
# dic[3] = 'U'
#
# print(lst)
# print(dic.values())
#
# a = People()
# a.Name("X")
# b = People()
# b.Name("Y")
# c = People()
# c.Name("Z")
# #多态
# a.printname()
# b.printname()
# c.printname()
#
# class Ball:
#     def __init__(self,name):
#         self.name = name
#     def kick(self):
#         print("我是%s" % self.name)
# a = Ball("球A")
# b = Ball("球B")
# c = Ball("球C")
# #多态
# a.kick()
# b.kick()
# c.kick()
#
# class People:
#     __name="小甲鱼"  #伪私有
#
# A = People()
# #伪私有
# print(A._People__name)
#继承
# class Parent:
#     def hello(self):
#         print("hello world")
#
# class Child(Parent):
#     pass
#
#
# P = Parent()
# P.hello()
# C = Child()
# C.hello()
#
# #子类和父类中有相同的函数，子类会覆盖父类
# class Son(Parent):
#     def hello(self):
#         print("你好世界！")
# S = Son()
# S.hello()
# C.hello()
# import random
# class Fish:
#     def __init__(self):
#         self.x = random.randint(0,10)
#         self.y = random.randint(0,10)
#     def move(self):
#         self.x -= 1
#         print("我的位置是：",self.x,self.y)
# class Glodfish(Fish):
#     pass
# class Salmon(Fish):
#     pass
# class Shark(Fish):
#     def __init__(self):
#         #Fish.__init__(self)
#         super().__init__()
#         self.z = 5
#         self.hungry = True
#     def eat(self):
#         if self.hungry:
#             print("我要吃饭！")
#             self.hungry = False
#         else:
#             print("吃饱了")
#
# fish = Fish()
# print(fish.x)
# fish.move()
# fish.move()
# goldfish = Glodfish()
# goldfish.move()
# shark = Shark()
# shark.eat()
# shark.move()
# print(shark.x)
# print(shark.z)
#
# #多重继承
# class Base1:
#     def f1(self):
#         print("我为Base1代言。。。")
# class Base2:
#     def f2(self):
#         print("我为Base2代言。。。")
# class C(Base1,Base2):
#     pass
#
# c =C()
# c.f1()
# c.f2()
#组合

# class Fish:
#
#     def __init__(self,x):
#         self.num = x
#
# class Turtle:
#     def __init__(self,y):
#         self.num = y
# class pool:
#     def __init__(self,x,y):
#         self.fish = Fish(x)
#         self.turtle = Turtle(y)
#     def print_num(self):
#         print("水池里有%d条鱼，%d只乌龟" % (self.fish.num, self.turtle.num))
#
# P = pool(2,5)
# P.print_num()
# fish = Fish(9)


# class C:
#     count = 2
#
# a = C()
# b = C()
# c = C()
# c.count += 5
# print(a.count)
# print(b.count)
# print(c.count)
#
# C.count += 10  #类本身也是对象
# print(a.count) #12
# print(c.count) #7
# c.x = 1
# print(c.x)
#
# class BB:
#     def printBB(self):
#         print("No zuo no die")
#
#
# class C:
#     def __init__(self,x=1,y=4):
#         self.x = x
#         self.y = y
#
# c = C()
# b = BB()
# print(b.__dict__)
# print(c.__dict__)

#__init__不能有返回值，默认返回None
# class A:
#     def __init__(self):
#         return "a"
# a = A()
#报错
# a = "abc"
# a = a.upper() //转成大写
# print(a)
#
# class C:
#      def __init__(self,x=1,y=4):
#          self.x = x
#          self.y = y
# print(C.__dict__)



# class A:
#     def __init__(self,x):
#         print("我是__init__，我被调用了")
#         self.x = x
#     def __del__(self):
#         print("我是__del__，我被调用了")

# a = int(123) #对象的实例化
# class New_int(int): #继承了int的方法
#     def __add__(self, other):
#         return int.__sub__(self, other)
#     def __sub__(self, other):
#         return int.__add__(self, other)
# a = New_int(2)
# b = New_int(4)
#
# print(a - b)
# print(a + b)
# print(pow(a,b))
# c = divmod(6,4)[1] #divmod: 返回商和余数
# print(c)
#
#
# class Int(int):
#     pass
# a = Int(2)
# b = Int(5)
# print(a - b) #调用__sub__函数
# print(1 - b) #调用的是__rsub__(other, self)
#
# import urllib.request
# response = urllib.request.urlopen("http://www.fishc.com")
# http = response.read().decode()
# print(http)

# class C:
#     def __init__(self,size):
#         self.size = size
#     def getsize(self):
#         return self.size
#     def setsize(self,value):
#         self.size = value
#     def delsize(self):
#         del self.size
#
#     x = property(getsize,setsize,delsize)
# c = C(2)
# c.x = 3

class C:
     def __init__(self,x):
         self.x = x
     def __getattribute__(self, item):
         print("AA")
         return super().__getattribute__(item)
     def __getattr__(self, item):
         print("class C has no attribute %s"% item)

    #注意，如果在__setattr__ 函数里存在对象属性赋值操作会陷入死循环
     def __setattr__(self, name, value):
         print("setattr")
         super().__setattr__(name,value)



c = C(2)
print(c.x)
c.y = 4



































