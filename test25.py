# -*- coding: utf-8 -*-
# Author: 小狼狗

'''file 操作'''

'''
    当以'r'模式打开文件时，文件必须存在
    而以'w'模式打开时，文件如果不存在，则会被创建
'''
import os
# with open('11.txt','w') as f:
#     f.write("I love china!\n")
# with open('11.txt', 'a') as f:
#     f.write("hahahahhah")

with open('11.txt', 'r') as f:
    #text = f.read()           #返回文件中的所有的内容，格式是字符串
    text = f.readline()        #返回文件的一行内容，格式是字符串
    text1 = f.readline()
    text2 = f.readlines()      #返回所有的行，但保存在列表中,即返回一个列表
    f.seek(0)                  #将光标返回到文件头
    text3 = f.read(10)         #可以指定读取的字节数,缺省时读取所有的内容

print(text3)

'''
注意：
    文件是以指针决定位置的，每次执行readline()后指向下一行；
    而对于readlines()，执行之后，直接指向文件内容的末尾
    继续读取的话，则为空
'''
x = ['wo', 'ni', 'hao']
with open('11.txt', 'a') as f:
    f.writelines(x)    #writelines() 写入字符串序列



