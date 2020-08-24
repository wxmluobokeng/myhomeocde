#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/8/7 0:58
# @Author : 老萝卜
# @File : 文件写入-times_3.py
# @Software: PyCharm Community Edition

# file_name = 'demo.txt'
# with open(file_name, encoding='utf-8') as file_obj:
#     # write()来向文件中写内容
#     file_obj.write('Ke hou hao hao fu xi!')
# # Traceback (most recent call last):
# #   File "E:/python-course/homework_zero_class/lesson15/文件写入-times_1.py", line 8, in <module>
# #     with open(file_name, encoding='utf-8') as file_obj:
# # NameError: name 'file_name' is not defined


# open()函数来进行文件的操作(读 写 追加)
# 如果不指定操作类型，则默认是读取文件
# w表示是可写的。如果文件不存在，它会帮我们来创建一个文件并写入内容。如果文件存在则会覆盖原文件的内容

file_name = 'demo.txt'
with open(file_name,'w',encoding='utf-8') as file_obj:
    # write()来向文件中写内容
    file_obj.write('Ke hou hao hao fu xi!')


# a表示追加内容

# with open(file_name, 'a', encoding='utf-8') as file_obj:
#     file_obj.write('nba\n')
#     file_obj.write('cba\n')
#     file_obj.write('kfc\n')
#     file_obj.write(123)
# # Traceback (most recent call last):
# #   File "E:/python-course/homework_zero_class/lesson15/文件写入-times_1.py", line 34, in <module>
# #     r = file_obj.write(123) # TypeError: write() argument must be str, not int
# # TypeError: write() argument must be str, not int

with open(file_name, 'w', encoding='utf-8') as file_obj:
    file_obj.write('nba\n')
    file_obj.write('cba\n')
    file_obj.write('kfc\n')
    file_obj.write(str(123))

with open(file_name, 'w', encoding='utf-8') as file_obj:
    file_obj.write('nba\n')
    file_obj.write('cba\n')
    file_obj.write('kfc\n')
    r=file_obj.write(str(123))
    print(r)                # 3
    r = file_obj.write(str(123)+"\n")
    print(r)                # 4

# write()是有返回值的，它的返回值是写入字符的个数
with open(file_name, 'a', encoding='utf-8') as file_obj:
    file_obj.write('nba\n')
    file_obj.write('cba\n')
    file_obj.write('kfc\n')
    r=file_obj.write(str(123))
    print(r)                # 3
    r = file_obj.write(str(123)+"\n")
    print(r)                # 4
