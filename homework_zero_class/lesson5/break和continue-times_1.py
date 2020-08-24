#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/12 9:51
# @Author : 老萝卜
# @File : break和continue-times_1.py
# @Software: PyCharm Community Edition

# continue 可以用来跳过当成循环

# break 可以用来立即退出循环语句，包括else语句


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