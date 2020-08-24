#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/8/7 0:07
# @Author : 老萝卜
# @File : 关闭文件-times_1.py
# @Software: PyCharm Community Edition

# 打开文件
file_name = "demo.txt"
file_obj = open(file_name)

# 读取内容
# read()方法来读取文件的内容，把读取的内容以字符串来返回

content = file_obj.read()
print(content)

# 关闭文件close()
file_obj.close()

# file_obj.read()
# # Traceback (most recent call last):
# #   File "E:/python-course/homework_zero_class/lesson15/关闭文件-times_1.py", line 21, in <module>
# #     file_obj.read()
# # ValueError: I/O operation on closed file.

# with...as语句
# 一旦with...as语句结束文件自动关闭

with open(file_name) as file_obj:
    print(file_obj.read())
# file_obj.read()
# # Traceback (most recent call last):
# #
# #   File "E:/python-course/homework_zero_class/lesson15/关闭文件-times_1.py", line 32, in <module>
# #     file_obj.read()
# # ValueError: I/O operation on closed file.


# file_name = 'abc.txt'
# with open(file_name) as file_obj:
#     print(file_obj.read())
# # Traceback (most recent call last):
# #   File "E:/python-course/homework_zero_class/lesson15/关闭文件-times_1.py", line 41, in <module>
# #     with open(file_name) as file_obj:
# # FileNotFoundError: [Errno 2] No such file or directory: 'abc.txt'

file_name = 'abc.txt'
try:
    with open(file_name) as file_obj:
        print(file_obj.read())
except FileNotFoundError:
    print(f'{file_name}文件不存在')


# 读文件标准写法
# try:
#     with open(file_name) as file_obj:
#         print(file_obj.read())
#         # 文件操作....
# except FileNotFoundError:
#     print(f'{file_name}文件不存在')