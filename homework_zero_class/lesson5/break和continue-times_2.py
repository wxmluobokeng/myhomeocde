#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/12 9:53
# @Author : 老萝卜
# @File : break和continue-times_1.py
# @Software: PyCharm Community Edition


i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
else:
    print('hello')



i = 0
while i < 6:
    i += 1
    if i == 3:
        break
    print(i)
else:
    print('hello')