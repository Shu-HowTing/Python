# ## Numpy
# import numpy as np
# print(np.__version__) #打印版本号
# vector = np.array([1,2,7,10])
# c = np.array([[1,2,3],
#               [2,3,8],
#               [4,5,6]])
# print(vector)
# print(vector + 1) # 每个元素加1
# print(c)
# print(c.shape)
# print(c[:,1:3]) #打印C的1,2列
# print(list == 2)
# print(vector == 2)
# index = (vector % 5 == 0) | (vector % 2 == 0)  #返回序列中既是5的倍数又是2的倍数的元素的下标（返回值是一个列表）
# print(vector[index])
# print(c.max(axis=0)) #求每列的最大值
#
# print(c.transpose())
# print(c.sum()) #求所有元素的和
#
# Z = np.zeros((2,3))
# print(Z)
# Z[1][2] = 1
# print(Z)
# z = np.arange(1,10) # 生成一个1-9的向量
# print(z)
# z = z.reshape(3,3) #将向量变为矩阵
# print(z)
# s = np.nonzero(z)
# print(s)
# z = np.eye(3)
# print(z)
# z = np.diag([1,2,3,4],k=0)  #k=0,表示以[1,2,3,4]为对角线
# print(z)                    #k=1,表示在对角线的上一行
# z = np.random.random((3,3))
# print(z)
#
# z = np.zeros((8,8))
# z[1::2,::2] = 1 #1、3、5、7行&&0、2、4、6列的元素置为1
# z[::2,1::2] = 1
# print(z)
# z = np.tile([1,0],[4,4])
# print(z)
# a = np.array([1,2,3])
# b = np.array([2,3,4])
# z = np.dot(a,b) #向量的内积，是一个数 z=20
# z = np.dot(np.ones((3,1)),np.ones((1,2))) #矩阵的乘积
# print(z)
# z = np.linspace(0,10,11) #（0-10）等差生成11个数
# print(z)
# print(np.sort(z))
# print(np.sort(c,axis=0)) #对列进行排序
# print(np.mean(c,axis=0))
