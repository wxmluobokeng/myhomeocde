#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/12 13:29
# @Author : 老萝卜
# @File : while语句-times_1.py
# @Software: PyCharm Community Edition

'''
执行流程
while语句执行时，先对while语句的条件表达式进行求值判断
如果结果为True,则执行循环体的代码块
循环体执行完后，继续对条件表达式进行求值判断，以此类推
直到判断结果为False .则退出循环，执行else语句中的代码块
'''


# while循环的三要素
# 初始化表达式，通过初始化表达式来初始化一个变量 例如 i = 0
# # 初始化变量是0 你小于几就执行几次
# # 条件表达式，用来设置循环的执行条件 例如 i < 20
#       更新条件表达式，修改初始化变量的值
i = 0
while i < 22:
    i += 1
    print(i)


i = 0
while i < 10:
    i += 1
    print(i,'hello')
else:
    print('执行到else语句的逻辑了')

