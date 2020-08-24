#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/12 9:56
# @Author : 老萝卜
# @File : if-elif-else语句-times_1.py
# @Software: PyCharm Community Edition

value = 15000
if value >= 30000:
    print('有钱任性')
elif value >= 20000:
    print('有钱真好')
elif value >= 10000:
    print('哥也月薪上万了')
elif value >= 5000:
    print('工资还说的过去')
elif value >= 2000:
    print('能养活自己了')
else:
    print('你该加油了')


value =2500

if value >= 2000 and value<5000:

    print('能养活自己了')

elif value >= 5000 and value < 10000:

    print('工资还说的过去')
elif value >= 10000:

    print('哥也月薪上万了')
