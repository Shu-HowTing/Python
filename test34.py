# -*- coding: utf-8 -*-
# Author: 小狼狗

'''
=============================================
        论numpy中matrix 和 array的区别
=============================================
'''

import numpy as np
#Numpy matrices必须是2维的,但是 numpy arrays (ndarrays) 可以是多维的（1D，2D，3D····ND）.
#Matrix是Array的一个小的分支，包含于Array。所以matrix 拥有array的所有特性
A = np.mat('1,2; 2,3')
B = np.mat('2,3; 5,6')
print(A)
# [[1 2]
#  [2 3]]
print(B)
#[[2 3]
# [5 6]]
print(A.shape)          #(2,2)
print(A.reshape(1,4))   #[[1 2 2 3]]

#矩阵相乘
C = A*B
print(C)
# [[12 15]
#  [19 24]]

#相反的是在numpy里面arrays遵从逐个元素的运算，所以array：c 和d的c*d运算相当于matlab里面的c.*d运算
a = np.array([[4, 3], [2, 1]])
b = np.array([[1, 2], [3, 4]])
c = a * b
print(c)
# [[4 6]
#  [6 4]]

#而矩阵相乘，则需要numpy里面的dot命令:
c = np.dot(a, b)
print(c)
# [[13 20]
#  [ 5  8]]

# ** 运算符的作用也不一样 :
print(a**2)     #对应元素平方
print(A**2)     #矩阵求幂

#matrix 和 array 都可以通过objects后面加.T 得到其转置。
# 但是 matrix objects 还可以在后面加 .H f得到共轭矩阵, 加 .I 得到逆矩阵。
print(A.I) #求逆矩阵
# [[-3.  2.]
#  [ 2. -1.]]

'''
问题就出来了，如果一个程序里面既有matrix 又有array，会让人脑袋大。但是如果只用array，你不仅可以实现matrix所有的功能，还减少了编程和阅读的麻烦。

当然你可以通过下面的两条命令轻松的实现两者之间的转换：np.asmatrix和np.asarray
'''
a = np.asarray(A)
print(type(a))
#<class 'numpy.ndarray'>
b = np.asmatrix(b)
print(type(b))
#<class 'numpy.matrixlib.defmatrix.matrix'>

'''
numpy 中的array与numpy中的matrix，matlab中的matrix的最大的不同是:
    在做归约运算时，array的维数会发生变化，但matrix总是保持为2维。
'''
m = np.mat([[1,2],[2,3]])
mm = m.mean(axis=1)
print(mm)  #2*1
# [[ 1.5]
#  [ 2.5]]
print(m - mm)
#[[-0.5  0.5]
# [-0.5  0.5]]

a = np.array([[1,2],[2,3]])
am = a.mean(axis=1)
print(am)
#[ 1.5  2.5]
print(a - am)   #np的广播机制，得到不一样的结果
#array([[-0.5, -0.5],
#       [ 0.5,  0.5]])

















