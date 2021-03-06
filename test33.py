# -*- coding: utf-8 -*-
# Author: 小狼狗
'''python中的位操作'''

#计算机中的数字都是用二进制形式表示的，在python里面，给数字加上前缀 '0b' 表示是二进制数字
#类似的，python当中的十六进制和八进制数字的前缀分别为 '0x' 和 '0'
x = 0b111
print(x)    #7
# 十六进制
#   0x10 => 16
#   0xff => 255
# 八进制
#   010 => 8
#   017 => 15



# 十进制转二进制
x = 7
a = bin(x)  #0b111
print(a)
print(type(a))  #<class 'str'>

#将输入的二进制转成十进制
x = '1101'
print(int(x,2))

'''
二进制数字有自己的特殊运算，是对每一位数字分别进行的操作，所以叫做位操作.
Python共有以下几种位操作符：
    x >> y # 返回 x 向右移 y 位得到的结果
    x << y # 返回 x 向左移 y 位得到的结果
    x & y # 且操作，返回结果的每一位是 x 和 y 中对应位做 and 运算的结果，只有 1 and 1 = 1，其他情况位0
    x | y # 或操作，返回结果的每一位是 x 和 y 中对应位做 or 运算的结果，只有 0 or 0 = 0，其他情况位1
    ~x # 反转操作，对 x 求的每一位求补，只需记住结果是 -x - 1
    x ^ y # 或非运算，如果 y 对应位是0，那么结果位取 x 的对应位，如果 y 对应位是1，取 x 对应位的补
'''
#左移、右移 >>\ <<
x = 0b1111 >> 1  #0b111 = 7
print(x)
x = 0b1010 << 2  #0b101000 = 40
print(x)

#向右移1位可以看成除以2，向左移一位可以看成乘以2。移动n位可以看成乘以或者除以2的n次方。
print(8 >> 1)      #8//2
print(15 >> 1)     #15//2
print(8 << 2)      #8 * 2**2

#且操作 &
x = 0b1111 & 0b1010     #0b1010 = 10
print(x)
#或操作  |
x = 0b1000 | 0b0111     #0b1111 = 15
print(x)
#反转操作 ~
#python的反转操作只接受一个参数n，n必须是整数，效果是对n的内部表示的每一位求补，运算结果位 -n-1
print(~4)
print(~0)
print(~True)
#或非（同或）操作 ^
x = 0b1111 ^ 0b0101     #0b1010
print(x)

















