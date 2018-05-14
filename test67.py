# -*- coding: utf-8 -*-
# Author: 小狼狗
'''
序列化：
    我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。
    序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
    反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。
'''
import pickle
import json

#pickle
d = {'name':'bob' , 'age':20, 'score':80}

d_s = pickle.dumps(d)
print(d_s)
print(type(d_s)) #<class 'bytes'>
print(bytes(d,encoding='utf-8'))


# with open("d.txt",'wb') as f:
#     f.write(d_s)

#等价于
# with open("d.txt",'wb') as f:
#     pickle.dump(d,f)

# unpickle
f = open("d.txt","rb")
d_r = f.read()   # <class 'bytes'>
p = pickle.loads(d_r)

# 等价于
# p = pickle.load(f)
print(p)

obj = dict(name='小明', age=20, score=80)
s = json.dumps(obj)
print(s)
print(type(s))  #<class 'str'>
print(json.loads(s))

x = "中国"
d = json.dumps(x)
print(d)   #<class str>