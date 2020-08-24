#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/12 14:48
# @Author : 老萝卜
# @File : while语句练习-times_1.py
# @Software: PyCharm Community Edition

# 获取100以内所有的数


r = 0 #定义一个变量保存结果
i = 0
while i < 100:
    i += 1
    # 判断 i是偶数
    if i % 2 == 0:
        r += i
print(r)

#　获取100以内所有的偶数
i = 0
r = 0
while i < 100:
    i += 2
    r += i
print(r)