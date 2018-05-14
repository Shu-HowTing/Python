# -*- coding: utf-8 -*-
# Author: 小狼狗

'''
装饰器：
    装饰器本质上是一个Python函数，它可以让其他函数在不需要做任何代码变动的前提下增加额外功能，装饰器的返回值也是一个函数对象。它
    经常用于有切面需求的场景，比如：插入日志、性能测试、事务处理、缓存、权限校验等场景。装饰器是解决这类问题的绝佳设计，
    有了装饰器，我们就可以抽离出大量与函数功能本身无关的雷同代码并继续重用。概括的讲，装饰器的作用就是为已经存在的对象添加额外的功能。
'''

# 权限设置

userAge = 9
def canYou(func):
  def decorator(*args, **kwargs):
      if 1< userAge <10:
          return func(*args, **kwargs)
      print('你的年龄不符合要求，不能看')
  return decorator

@canYou
def play():
  print('开始播放动画片 《喜洋洋和灰太狼》')

play()



# 多个装饰器执行顺序
def decorator_a(func):
    print('Get in decorator_a')
    def inner_a(*args, **kwargs):
        print('Get in inner_a')
        return func(*args, **kwargs)
    return inner_a

def decorator_b(func):
    print('Get in decorator_b')
    def inner_b(*args, **kwargs):
        print('Get in inner_b')
        return func(*args, **kwargs)
    return inner_b

@decorator_b
@decorator_a
def f(x):
    print('Get in f')
    return x * 2

f(1)

# Get in decorator_a
# Get in decorator_b
# Get in inner_b
# Get in inner_a
# Get in f

