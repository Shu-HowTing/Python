# -*- coding: utf-8 -*-
# Author: 小狼狗

class Node(object):
    def __init__(self,val):    #定位的点的值和一个指向
        self.val = val         #指向元素的值,原队列第二元素
        self.next = None       #指向的指针
class stack(object):
    def __init__(self):
        self.top = None          #初始化最开始的位置
    def peek(self):              #获取栈顶的元素
        if self.top != None:     #如果栈顶不为空
            return self.top.val  #返回栈顶元素的值
        else:
            return None
    def push(self,val):             #添加到栈中
        n = Node(val)               #实例化节点
        n.next = self.top           #顶端元素传值给一个指针
        self.top = n
        #return n.val
    def pop(self):  #出栈
        if self.top == None:
            return None
        else:
            tmp=self.top.val
            self.top=self.top.next  #下移一位，进行
            return tmp

if __name__=="__main__":
    s=stack()
    s.push(1)
    s.push(2)
    s.push(3)

    print(s.pop())
    print(s.peek())
    print(s.pop())
    print(s.pop())