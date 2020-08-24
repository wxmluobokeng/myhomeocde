#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/8/7 00:02
# @Author : 老萝卜
# @File : 文件打开-times_2.py
# @Software: PyCharm Community Edition


file_name = "demo.txt"
file_obj = open(file_name)
print(file_obj)
# <_io.TextIOWrapper name='demo.txt' mode='r' encoding='cp936'>


file_name = "demo1.txt"
file_obj = open(file_name)
print(file_obj)

# Traceback (most recent call last):
#   File "E:/python-course/homework_zero_class/lesson15/文件打开-times_1.py", line 27, in <module>
#     file_obj = open(file_name)
# FileNotFoundError: [Errno 2] No such file or directory: 'demo1.txt'

