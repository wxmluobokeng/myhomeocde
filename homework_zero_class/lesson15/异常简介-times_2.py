#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/8/6 22:37
# @Author : 老萝卜
# @File : 异常简介-times_1.py
# @Software: PyCharm Community Edition

# print(abc)   #NameError: name 'abc' is not defined


# print("hello")
# print(6/0)
# print("java")
# # Traceback (most recent call last):
# #   File "E:/python-course/homework_zero_class/lesson15/异常简介-times_1.py", line 16, in <module>
# #     print(6/0)
# # ZeroDivisionError: division by zero
# # hello




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
    print('出错了.....')
print('java')
# hello
# 出错了.....
# java


print('hello')
try:
    print(6/2)
except:
    print('出错了.....')
else:
    print('程序正常执行没有错误.....')
print('java')
# hello
# 3.0
# 程序正常执行没有错误.....
# java

