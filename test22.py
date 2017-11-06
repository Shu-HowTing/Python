# def f(x):
#     x = 2
#     print(x)
# a = 1
# f(a)
# print(a)
# def bad_append(new_item, a_list=[]):
#     print(id(new_item))   #145
#     print(id(a_list))
#     a_list.append(new_item)
#     return a_list
# print(bad_append(1))     #1
# print(id(1))    #145
# print(bad_append(3,[4]))
#
# # print(a)
# def good_append(new_item, a_list=None):
#     print(id(new_item))   #145
#     print(id(a_list))
#     if a_list == None:
#         a_list = []
#         print(id(a_list))
#     a_list.append(new_item)
#     print(id(a_list))
#     return a_list
# print(good_append(1))
# print(good_append(1))
# print(id(good_append))

#pickle模块

#import pickle
#  写入
# lst1 = [1, 2, 3, "hello world"]
# with open("f.pickle",'wb') as f:
#     pickle.dump(lst1,f)
#     #f.close()
# #  读取
# f = open("f.pickle","rb")
# lst2 = pickle.load(f)
# f.close()
# print(lst2)
#
# #Exception(异常)
# try:
#     f = open("AAA",'r')
#     print(f.read())
#     f.close()
# except:
#     print("出错了")



#迭代器
# class Fab:
#     def __init__(self,n):
#         self.a = 0
#         self.b = 1
#         self.n = n
#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.a,self.b = self.b ,self.a + self.b
#         if self.b > self.n:
#             raise StopIteration
#         return self.b
#
# fab = Fab(100)
# for each in fab:
#     print(each)


# y = [4, 5, 6]
#
# z = [7, 8, 9]
#
# xyz = zip(x, y, z)
# for x in xyz:
#     print(x)
#
# print(list(filter(lambda x: x%2, range(10))))



#图形界面
# import easygui as g
# import sys
#
# while 1:
#     g.msgbox("嗨，欢迎进入第一个界面小游戏","Welcome")
#     msg = "请问你希望在鱼C工作室学习到什么知识呢"
#     title = "小游戏互动"
#     choices = ["谈恋爱", "编程", "OOXX", "琴棋书画"]
#     choice = g.choicebox(msg, title, choices)
#
#     # note that we convert choice to string,in case
#     # the user cancelled the choice,and we got None
#     g.msgbox("你的选择是:" + str(choice), "结果")
#     msg = "你希望重新开始小游戏吗?"
#     title = " 请选择"
#     if g.ccbox(msg, title):  # show a Contiue/Cancel dialog
#         pass  # user chose Contonue
#     else:
#         sys.exit(0)  # user chose Cancel


# 汉诺塔
def hannoi(n, x, y, z):
    if  n == 1:
        print(x,'-->',z)
    else:
        hannoi(n-1, x, z, y)
        print(x, '-->', z)
        hannoi(n-1, y, x, z)
hannoi(3, 'A', 'B', 'C')

#


A = [[1,2],[2,4],[4,5]]
for m ,n in A:
    print(m,n)

a = (3,4)
a = [list(a)]
print(a)





