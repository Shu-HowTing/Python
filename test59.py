# -*- coding: utf-8 -*-
# Author: 小狼狗

# import sys
# def test():
#     args = sys.argv
#     if len(args) == 1:
#         print("hello,world!")
#     elif len(args) == 2:
#         print("hello"+' '+args[1])
#     else:
#         print("Too many arguments!")
# if __name__ == '__main__':
#     test()

class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.age = 8
