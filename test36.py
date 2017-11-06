# -*- coding: utf-8 -*-
# Author: 小狼狗

'''
=====================================================================================
np.random.binomial(n, p, size=None)
    n：每回采样时实验的次数
    p：概率
    size：采样次数
例如：抛5次硬币，其中出现3次正面朝上的概率是多少？
     n=5, p=0.5, size=1000(自己决定)即每回抛5次硬币，一共进行1000回
     返回一个size维的列表,其中每个元素表示每回实验的结果（有多少个硬币正面朝上）
     prob = sum(np.random.binomial(5, p=0.5, size=1000) == 3)/1000
=====================================================================================
'''
import numpy as np

#dropout的实现

def dropout(x, level):
    if level < 0. or level >= 1:  # level是概率值，必须在0~1之间
        raise Exception('Dropout level must be in interval [0, 1.0]')
    retain_prob = 1. - level
    # 我们通过binomial函数，生成与x一样的维数向量。binomial函数就像抛硬币一样，我们可以把每个神经元当做抛硬币一样
    # 硬币 正面的概率为p，n表示每个神经元试验的次数
    # 因为我们每个神经元只需要抛一次就可以了所以n=1，size参数是我们有多少个硬币。
    sample = np.random.binomial(n=1, p=retain_prob, size=x.shape)  # 即将生成一个0、1分布的向量，0表示这个神经元被屏蔽，不工作了，也就是dropout了
    print(sample)
    x *= sample  # 0、1与x相乘，我们就可以屏蔽某些神经元，让它们的值变为0
    print(x)
    x /= retain_prob  #rescale

    return x

# 对dropout的测试，大家可以跑一下上面的函数，了解一个输入x向量，经过dropout的结果
x = np.asarray([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=np.float32)
y = dropout(x, 0.4)
print(y)















