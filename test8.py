"""
#字符串
#=========引号=======
print("hello world!")
print('hello world!')
#两者等价
print("hello\' world")
print('''hello
        world!''')
print("hello\
        world")
# len  /  + / *
s = "hello world"
print(len(s))
s = s + "abc"    #注意：只能跟字符，s+121，会报错
print(s)
print(3*s)
# in 判断子串
print('a' in s)
for c in (s):
    print(c)

#判断s里面有多少元音字母（不分大小写）
def vowles_count(s):
    count = 0
    for c in s:
        if c in ("aeiouAEIOU"):
            count += 1
    return count
print(vowles_count("hello world"))
"""
"""
#索引，切片操作
s = "hello world"
a = s[3: 6]
b = s[ : ]
c = s[2: ]
d = s[3: 20: 2]
print(a+"\n", b+"\n", c+"\n", d)

#字符串是不可变的
S = "hello world"
#S[1] = a
#会报错
S = S[0:1] + "a" +S[2:]
print(S)
S = S.replace("a", "e")
print(S)
S = S.replace("l", "L")
print(S)

#find / split
i = S.find("o")
print(i)
print(S.split())
"""

#读取人名列表文件name.txt，将首字母大写，其他都小写
# f = open("names.txt",'r')
# for line in f:
#     line = line.strip() #去掉每一行的换行符
#     print (line.title()) #title实现首字母大写.其他小写
# f.close()

# def is_ascending(name):
#     p = name[0]
# #  从第一个字母开始，判断后面一位字母是否大于此字母
#     for c in name:
#         if p > c:
#             return False
#         else:
#             p = c
#             return True
# f = open("names.txt",'r')
# for line in f:
#      line = line.strip() #去掉每一行的换行符
#      if is_ascending(line):
#          print(line)
# f.close()

#格式化输出字符串 format

print("Have {} good {}".format(5, 'day'))

import math
print(math.pi)
print("PI ={: .4f}".format(math.pi))
print("PI ={:< 9.4f}".format(math.pi)) # <:左对齐  9.4f:一共9位，保留四位小数
print("PI ={:e}".format(math.pi))

#正则表达式
import re
f = open("names.txt",'r')
pattern = ("C.A") # . 表示C和A之间右若干字母
for line in f:
    line = line.strip()
    if re.search(pattern, line): #对每一行寻找满足题意的字符串
        print(line)
f.close()






