#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/12 14:57
# @Author : 老萝卜
# @File : if语句练习一-times_1.py
# @Software: PyCharm Community Edition

# 根据指定的月份打印该月份是几月
# 3 4 5 春季 6 7 8 夏季 9 10 11 秋季 12 1 2 冬季

month = 15
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

