#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/12 16:32
# @Author : 老萝卜
# @File : 循环嵌套-times_1.py
# @Software: PyCharm Community Edition

# 在控制台打印如下图形
# *****
# *****
# *****
# *****
# *****

i = 0
while i < 5:  # 控制高度
    # print('*****')
    j = 0
    while j < 5:  # 控制图形的宽度
        print('*', end='')
        j += 1
    print()
    i += 1

# *
# **
# ***
# ****
# *****

i = 0
while i < 5:
    j = 0
    while j < i + 1:
        print('*', end='')
        j += 1
    print()
    i += 1

# *****
# ****
# ***
# **
# *

i = 0
while i < 5:
    j = 0
    while j < 5 - i:
        print('*', end='')
        j += 1
    print()
    i += 1
