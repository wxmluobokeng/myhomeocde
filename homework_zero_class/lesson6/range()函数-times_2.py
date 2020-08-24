#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/14 22:19
# @Author : 老萝卜
# @File : range()函数-times_2.py
# @Software: PyCharm Community Edition

for i in range(5):
    print(i)

# 获取奇数
lst = [1,2,3,4,5,6,7,8,9]

print(list(range(0,9,2)))        # [0, 2, 4, 6, 8]

for i in range(0,9,2):
    print(lst[i])
