#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/12 15:08
# @Author : 老萝卜
# @File : if语句练习一-times_2.py.py
# @Software: PyCharm Community Edition

month_str=input("请输入月份")
month= int(month_str)

if month == 3 or month == 4 or month == 5:
    print(month,'春季')
elif month == 6 or month == 7 or month == 8:
    print(month,'夏季')
elif month == 9 or month == 10 or month == 11:
    print(month,'秋季')
elif month == 12 or month == 1 or month == 2:
    print(month,'冬季')
else:
    print(month,'月份不存在')

# 先把不正确的排除
if month > 12 or month < 1:
    print(month,'月份不存在')
elif 3 <= month <= 5:
    print(month,'春季')
elif 6 <= month <= 8:
    print(month,'夏季')
elif 9 <= month <= 11:
    print(month, '秋季')
else:
    print(month, '冬季')

