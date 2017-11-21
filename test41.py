# -*- coding: utf-8 -*-
# Author: 小狼狗

'''
=========================================================
                将PWM信号还原为原始信号
=========================================================
'''
import numpy as np
import pylab as pl
PERIOD = 0.1

x = np.linspace(0, 2*np.pi, 200)
y = np.sin(x)
y1 = y
#y1 = np.cos(x)
for i in range(66):
    x0 = x[3*i]
    y0 = np.sin(x0)
    if y0>0:
    #x_p = x[:,np.ceil(10/np.pi)]
        y1[3*i: int(y0*3)+3*i] = 1
        y1[int(y0*3)+3*i: 3*(i+1)] = 0
    else:
        y1[3 * i: int(y0 * 3) + 3 * i] = -1
        y1[int(y0 * 3) + 3 * i: 3 * (i + 1)] = 0



pl.plot(x,y1)
pl.show()
#
# FILENAME = "numpy_pwm.bin"
# #【你的程序】将FILENAME的内容读入数组pwm，并计算pwm的积分pwm_int
# with open(FILENAME, 'rb') as f:
#     pwm = np.array(list(f.read()))
#
# print(pwm[pwm < 0])
# pl.figure(figsize=(8,5))
# pl.subplot(211)
# pl.plot(pwm)
# #pl.subplot(212)
# #pl.plot(pwm_int)
# pl.show()
# l = np.array([1,2,3,4,5,6,9,0])
# print(l[l>3])