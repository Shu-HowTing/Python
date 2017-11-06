# -*- coding: utf-8 -*-
# Author: 小狼狗

'''os模块'''
import os

print(os.getcwd())
# os.makedirs('./hello')      #创建目录
os.rmdir('./hello')           #删除目录
#os.remove('./11.txt')        #删除文件
#os.rename('./1.txt', '11.txt')   #文件或目录重命名
os.chdir('./prank')           #改变当前的目录
#print(os.listdir())          #获取当前目录下的的文件名，返回一个列表
print(os.getcwd())
os.chdir('../')               #返回到上一层目录
print(os.getcwd())


