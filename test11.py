# A =[]
# A.append((1,2))
# print(A)
# A.append([3,4])
# print(A)
# a = 1
# b = 2
# [a,b] = [b, a]
# print(a, b)
# A：[(1,2), [3,4]]
# #A[0][1] = 5 #会报错,元组的元素不能改变;但元组和列表一样是支持下标操作的 
#
# A[1][1] = 9 #列表的元素可以改变

#class类
# class Calculator:
#     name = "good calculator"
#     price = 18
#     def add(self, x,y):
#         result = x + y
#         print(result)
#     def minus(self,x,y):
#         result = x - y
#         print(result)
#     def divide(self,x,y):
#         result = x/y
#         print(result)
#
# cal = Calculator()
# print(cal.name)
# cal.add(10, 12)
# cal.divide(3, 6)
# cal.minus(8, 5)
#
# lst = list()
# lst.append(3)
# lst.append(5)
# lst.append(1)
# lst.sort()
# print(lst)
# #类的初始化
# class Human:
#     def __init__(self, name, height, age, gender):
#         self.Name = name  #不要忘了self
#         self.H = height
#         self.A = age
#         self.G = gender
#
# X = Human("Xiao ming", 1.8, 18, 'male')
# print(X.Name)
# print(X.H)
# print(X.A)
# print(X.G)

##读写文件
# text = "This is my first file!\n"
#
# f = open ("file.txt","w")
# f.write("hello world\n")
# f.write(text)
#
# f.close() #别忘了关上

#追加内容  'a'  如果以'w'打开的话，之前的内容会被覆盖
# f = open("file.txt",'a')
# text = "I Love U"
# f.write(text)
# f.close()

#读文件
f = open("file.txt",'r')
content = f.read()
print(content)

#按行读取 readline
f.seek(0)  #将光标重新定位到文件的开头，因为上面已经读完了
first_line = f.readline()
second_line = f.readline()
print(first_line, second_line)
#f.close()

#读取所有行readlines
f.seek(0)
text = f.readlines()
for i in text:
    print(i)
f.close()