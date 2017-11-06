#字典
#键——值
"""
my_dic = {"Tom":123456, "John":345672, "Jack":9837468}
print(my_dic["Tom"])
print(my_dic.items())
print(my_dic.keys())
print(my_dic.values())
#增加键——值
my_dic["Peter"] = 17638
print(my_dic.items())

#统计一个字符串中每个字母出现的次数
s = "assdskxndyhemxxl"
d = {}
for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(d)

#统计一篇文章中最常见的10个单词
f = open ("emma.txt","r")
word_seq = {}
for line in f:
    words = line.strip().split()
    for word in words:
        if word in word_seq:
            word_seq[word] += 1
        else:
            word_seq[word] =1

seq_word = []
for (word,seq) in word_seq.items():
    seq_word.append([seq, word])
seq_word.sort(reverse = True)

for (seq, word) in seq_word [ : 10]:
    print(seq,word)
f.close()
"""

#交换字典的键--值
#字典中，键不可以重复，但值可以
# d1 = {'Zhang': 123,'Li':456,'Wang':123, 'Zhao':456}
# d2 = {}
# for name,room in d1.items():
#     if room in d2:
#         d2.append(name)
#     else:
#         d2[room] = name
# print(d2)
#

#集合，无序不重复键集
#集合和字典相似，但无“值”
#可以执行 -（求差集）/&（求并集）/in / for ...   in ...
# -*- coding: utf-8 -*-
def load_dic(filename):
    word_dic = set()
    max_len = 1
    f = open(filename)
    for line in f:
        word = unicode(line.strip(),'utf-8')
        word_dic.add(word)
        if len(word) > max_len:
            max_len = len(word)
    return max_len,word_dic

def fmm_word_seg(sent, max_len,word_dic):
    begin = 0
    words = []
    sent = unicode(sent,'utf-8')
    while begin < len(sent):
        for end in range(begin + max_len, begin, -1):
            if set[begin:end] in word_dic:
                words.append(sent[begin:end])
                break
        begin = end
    return words
max_len, word_dic = load_dic("lexicon.dic")
sent = input("input a word:")
fmm_word_seg(sent, max_len, word_dic )
for word in words:
    print(word)
