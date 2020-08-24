#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/11 20:38
# @Author : 老萝卜
# @File : 99乘法口决表-times_2.py.py
# @Software: PyCharm Community Edition

i = 0
while i < 9:
    i += 1
    # print(i)
    j = 0
    while j < i:
        j += 1
        print(f'{j} * {i} = {j*i}   ', end='')  # 1*1=1
    print()


