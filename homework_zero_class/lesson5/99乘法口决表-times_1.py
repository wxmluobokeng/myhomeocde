#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/11 20:28
# @Author : 老萝卜
# @File : 99乘法口决表-times_1.py
# @Software: PyCharm Community Edition


# 打印出形状
i = 0
while i < 9: # 0 1 2 3 4

    j = 0
    while j < i + 1:

        print('*',end='')

        j += 1

    print()

    i += 1


# 1*1=1
# 1*2=2 2*2=4
# 1*3=3 2*3=6 3*3=9
# ....
#                          9*9=81

i = 0
while i < 9:
    i += 1
    # print(i)
    j = 0
    while j < i:
        j += 1
        print(f'{j} * {i} = {j*i}', end='')  # 1*1=1
    print()


