# -*- coding: utf-8 -*-
# Author: 小狼狗

'''
==========================================================
                剪刀,石头,布 小游戏
==========================================================
'''
import random
guess_list = ["石头", "剪刀", "布"]
win_combination = [["布", "石头"], ["石头", "剪刀"], ["剪刀", "布"]]

while True:
    computer = random.choice(guess_list)  #choice只能抽一个，想要抽多个，用random.sample(l,k)函数
    people = input('请输入：石头,剪刀,布\n').strip() #去除字符串首尾的指定字符，默认是空格
    if people not in guess_list:
        continue
    elif computer == people:
        print("平手，再玩一次！")
    elif [computer, people] in win_combination:
        print("电脑获胜！")
        break
    else:
        print("人获胜！")
        break

