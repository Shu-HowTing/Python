# -*- coding: utf-8 -*-
# Author: 小狼狗
'''
python的编码问题:

    encoding is the name of the encoding used to decode or encode the
    file. This should only be used in text mode. The default encoding is
    platform dependent, but any encoding supported by Python can be
    passed.  See the codecs module for the list of supported encodings.
'''
import chardet
# with open("f.txt",w,encoding='utf-8') as f:
#     f.write("hello world！")
f = open("./test1.py",'rb')
data = f.read()
print(chardet.detect(data))
#{'language': '', 'confidence': 0.99, 'encoding': 'utf-8'}

'''py2
# s = "中国"
# print type(s)   # str
# print s
# s1 = s.decode(encoding='utf-8') #decode to unicode from parameter
#
# s2 = s1.encode(encoding='utf-8') #encode to parameter from unicode
#
# print s1,s2   # 中国 中国
# print type(s1) #<type 'unicode'>
# print type(s2) #<type 'str'>

'''


s = "中国"
print(bytes(s,encoding='gbk'))
s1 = s.encode(encoding='gbk')  #相当于unicode(s).encode('gbk')
print(chardet.detect(s1))
print(s1)
print(s1.decode("gbk"))






