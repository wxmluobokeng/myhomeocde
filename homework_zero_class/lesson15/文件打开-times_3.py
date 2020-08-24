#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/8/7 00:05
# @Author : 老萝卜
# @File : 文件打开-times_1.py
# @Software: PyCharm Community Edition


# 文件(File)
# 通过Python程序来对计算机中的各种文件进行增删改查的操作 I/O(Input/Output)

# 操作文件
# 1.打开文件
# 2.操作文件(读、写)，保存
# 3.关闭

# open() 返回值 返回了一个对象，这个对象就是当前打开的这个文件
# file 要打开文件的名字(路径)

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

