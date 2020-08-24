#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/8/6 22:25
# @Author : 老萝卜
# @File : 异常简介-times_1.py
# @Software: PyCharm Community Edition

# print(abc)   #NameError: name 'abc' is not defined

# 异常
# 在程序运行的过程中，不可避免的会出现一些错误。比如 使用了不存的索引，引用了没有赋值的变量..
# 这些错误我们就称之为异常
# 程序一旦出现异常，会导致程序立即终止。异常后面的代码都不会执行

# print("hello")
# print(6/0)  # ZeroDivisionError: division by zero
# print("java")
# # Traceback (most recent call last):
# #   File "E:/python-course/homework_zero_class/lesson15/异常简介-times_1.py", line 16, in <module>
# #     print(6/0)
# # ZeroDivisionError: division by zero
# # hello



# 处理异常
# 程序出现异常，目的并不是让我们的程序终止
# 而是希望我们在出现异常的时候，能够编写响应的代码来对异常进行处理
# try语句
# try:
#     代码块(可能出现错误的语句)
# except 异常类型 as 异常名:
#     代码块(出现错误以后的处理方式)
# except 异常类型 as 异常名:
#     代码块(出现错误以后的处理方式)
# except 异常类型 as 异常名:
#     代码块(出现错误以后的处理方式)
# else:
#     代码块(没有出现错误的语句)

print('hello')
try:
    print(6/0)
except:
    print('大兄弟出错了.....')
print('java')
# hello
# 大兄弟出错了.....
# java


print('hello')
try:
    print(6/2)
except:
    print('大兄弟出错了.....')
else:
    print('程序正常执行没有错误.....')
print('java')
# hello
# 3.0
# 程序正常执行没有错误.....
# java

