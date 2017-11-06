import copy
l1 = [1, 2, 4]
l2 = l1
l1[2] = 5
print(l1, l2)
l3 = copy.deepcopy(l1)
l1[2] = 10
print(l2, l3)
#字符串、 列表、 元组 都是序列，字符串和元组的元素不可更改，列表可以
#所有的序列都支持以下操作
'''
    s[i]    索引
    s[i:j]  切片
    max(s)  最大值
    len(s)  长度
    for i in s  in
'''

s = 'qqwerz'
print(len(s))
for i in s:
    print(i)
print(s[2])
print(max(s)) #z
print(len(s))
# s[2] = 'a'  会报错
print(s[0:2]) #qq

a = 123
a<<2
print(a)
L = [2, 4, 5]
I = L.__iter__()
print(type(I))
print(I.__next__())
'''
优点：迭代器的功能可以使用列表代替，但如果有很多值，列表就会占用太多的内存，
     而如果有可以一个接一个地计算值的函数，那么就可以在使用时采用计算一个值时获取一个值，占用更少内存

1: 可以直接作用于for循环的对象统称为可迭代对象(Iterable)
2: 可以调用next()函数并不断返回下一个值的对象称为迭代器(Iterator)
3: 所有的Iterable均可以通过内置函数iter()来转变为Iterator

过程：for循环开始时，会通过迭代协议差传递给iter()内置函数，（即调用对象的__iter__()方法），
     从而从可迭代对象获得一个迭代器，返回的对象含有需要的next方法
'''

class Fibs:
    def __init__(self):  # 初始化
        self.a = 0
        self.b = 1

    def __next__(self):  # 获取下一个条目
        self.a, self.b = self.b, self.a + self.b
        return self.a

    def __iter__(self):  # 返回迭代器
        return self

fibs = Fibs()    #产生一个对象
for f in fibs:    #迭代
    #print(type(f))
    if f > 100:
        break
    print(f)

#比较
#print(sum([x for x in range(100000000)]))
#print(sum(x for x in range(100000000)))
#列表解析
#根据已有列表，快速生成新的列表
l = [1,2,4,5]
a = [i**2 for i in l]
print(a)
c = [i**2 for i in l if i > 3]

#print(sum([x for x in range(100000000)]))


def index_word(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text, 1):
        if letter == ' ':
            result.append(index)
    return result

s = index_word("I love china")
print(s)











