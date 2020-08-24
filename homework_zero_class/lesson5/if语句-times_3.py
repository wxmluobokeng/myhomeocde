#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/12 19:10
# @Author : 老萝卜
# @File : if语句-times_1.py
# @Software: PyCharm Community Edition

num = 50
if num > 20:
    print('num比20大')
print('hello')

if False:
    print('haha')
    print(1)
    print(2)
print("iif False 语句执行完了")

num = 30
if num > 20 and num < 40:
    print('num比20大,num比40小')

# 上下两句是一样的
if 20 < num < 40:
    print('num比20大,num比40小')
