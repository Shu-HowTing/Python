# -*- coding: utf-8 -*-
# Author: 小狼狗
'''
===============================================
        numpy linalg模块
：linalg即linear algebra ,线性代数运算
===============================================
'''
import numpy as np
#inv: 求逆运算
# 注：矩阵必须是方阵且可逆，否则会抛出LinAlgError异常
A = np.mat('1 2; 4 4')
A_inv = np.linalg.inv(A)

print(A * A_inv)
# [[ 1.  0.]
#  [ 0.  1.]]

# 求解线性方程组
# numpy.linalg中的函数solve可以求解形如 Ax = b 的线性方程组，其中 A 为矩阵，b 为一维或二维的数组，x 是未知变量
A = np.mat("1 -2 1; 0 2 -8; -4 5 9")
b = np.array([0,8,-9])
x = np.linalg.solve(A, b)
print(x)    #<class 'numpy.ndarray'>
#[ 29.  16.   3.]
# 使用dot函数检查求得的解是否正确
print (np.dot(A, x))
# [[ 0. 8. -9.]]

#特征值和特征向量
'''
特征值（eigenvalue）a 即方程 Ax = ax 的根，是一个标量。其中，A 是一个二维矩阵，x 是一个一维向量。
特征向量（eigenvector） x 是关于特征值的向量
numpy.linalg模块中，eigvals函数可以计算矩阵的特征值，而eig函数可以返回一个包含特征值和对应的特征向量的元组
'''
B = np.mat("3 -2; 1 0")
e  = np.linalg.eigvals(B)
print (e)
e1, e2 = np.linalg.eig(B)
print(e1)
print(e2)

#奇异值分解svd
'''
A = U*Sigma*V
numpy.linalg模块中的svd函数可以对矩阵进行奇异值分解。
该函数返回3个矩阵——U、Sigma和V，其中U和V是正交矩阵，Sigma包含输入矩阵的奇异值。
'''
C = np.mat("4 11 14;"
           "8 7 -2")
print(C)

U,Sigma,V = np.linalg.svd(C, full_matrices=False)
print ("U:",U)
print ("Sigma:",Sigma)
#Sigma: [ 18.97366596 9.48683298]
print ("V:",V)
print (U * np.diag(Sigma) * V)
#[[  4.  11.  14.]
# [  8.   7.  -2.]]
e1, e2 = np.linalg.eig(C*C.T)
print(np.sqrt(e1))
#[ 18.97366596   9.48683298]

#广义逆矩阵
# 使用numpy.linalg模块中的pinv函数进行求解,
# 注：inv函数只接受方阵作为输入矩阵，而pinv函数则没有这个限制
D = np.mat("4 11 14; 8 7 -2")
pseudoinv = np.linalg.pinv(D)
print (pseudoinv)

#行列式
E = np.mat('4 5 6 7; 1 2 4 5; 3 4 5 6; 3 2 5 6')
print(np.linalg.det(E))   #-2.0

#norm ：范数
'''
默认	        二范数：ℓ2	    √x1**2+x2**2+…+xn**2
ord=2	    二范数：ℓ2	    同上
ord=1	    一范数：ℓ1	    |x1|+|x2|+…+|xn|
ord=np.inf	无穷范数：ℓ∞	    max(|xi|)
范数理论的一个小推论告诉我们：ℓ1≥ℓ2≥ℓ∞
'''
x = np.array([3,4])
print(np.linalg.norm(x))
#5.0
print(np.linalg.norm(x, ord=1))
#7.0
F = np.mat(' 3 4;  3 -5')
print(np.linalg.norm(F))

X = np.mat([[0, 3], [1, 2], [2, 0]])    #3个样本，每个样本2维

X_mean = np.mean(X,axis=0)
print(X_mean)
print(np.dot((X-X_mean).T, X-X_mean)/3)
#[[ 0.66666667   -1.        ]
# [-1.           1.55555556]]
#等价于
x = X.T
print(np.cov(x, bias=True))













