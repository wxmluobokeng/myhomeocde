#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/8/8 10:45
# @Author : 老萝卜
# @File : 文件的其他写入方式-times_1.py
# @Software: PyCharm Community Edition

filename="demo5.txt"
with open(filename,"x") as file:
    file.write("nba\n")
# Traceback (most recent call last):
#   File "E:/python-course/homework_zero_class/lesson16/文件的其他写入方式-times_2.py", line 9, in <module>
#     with open(filename,"x") as file:
# FileExistsError: [Errno 17] File exists: 'demo5.txt'


filename="demo6.txt"
with open(filename,"x", encoding='utf-8') as file:
    file.write("nba\n")
# 创建filename,并写入内容
