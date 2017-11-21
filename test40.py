# -*- coding: utf-8 -*-
# Author: 小狼狗

'''
=========================================================
                研究list和array的内存增长模式
=========================================================
'''
import sys
import time
import numpy as np
from array import array
import pylab as pl
from scipy.optimize import curve_fit
# 计算size列表，它的每个小标都保存增长到此下标时size列表的大小
size = []
l = []
for i in range(10000):
    l.append(i)
    size.append(sys.getsizeof(l))
pl.plot(size, lw=2)
pl.show()

# 计算resize_pos，它的每个元素是size中每次分配内存的位置
pl.figure()
#resize_pos = np.array([])
dif = np.diff(size, n=1)
resize_pos = np.where(dif)[0]
#pl.plot(resize_pos, lw=2)
#pl.show()
print("list increase rate:")
tmp = resize_pos[25:].astype(np.float)
print(np.average(tmp[1:]/tmp[:-1]))

# 用指数函数对resize_pos数组进行拟合
def func(x, a, b, c, d):
    return a * 10 ** (b*x + c) + d
x = np.arange(len(resize_pos))
y = resize_pos
popt, pcov = curve_fit(func, x, y, maxfev=2000)
b = popt[1]
plot1 = pl.plot(x, resize_pos, 's',label='original values')
plot2 = pl.plot(x, func(x, *popt), 'r',label='polyfit values')
pl.show()
print("list increase rate by curve_fit:")
print(10**b)

# 计算往array中添加元素的时间times
times = []
arr = array('i')
for i in range(10000):
    t1 = time.time()
    arr.append(i)
    t2 = time.time()
    times.append(t2-t1)

pl.figure()
pl.plot(times, lw=2)
pl.show()

# 通过times计算array对象内存分配时的长度resize_pos2
dif0 = np.diff(times, n=1)
resize_pos2 = np.where(dif0)[0]
pl.figure()
pl.plot(resize_pos2, lw=2)
pl.show()