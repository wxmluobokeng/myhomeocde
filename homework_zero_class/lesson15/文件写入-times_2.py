#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/8/7 0:52
# @Author : 老萝卜
# @File : 文件写入-times_1.py
# @Software: PyCharm Community Edition

# file_name = 'demo.txt'
# with open(file_name, encoding='utf-8') as file_obj:
#     # write()来向文件中写内容
#     file_obj.write('Ke hou hao hao fu xi!')
# # Traceback (most recent call last):
# #   File "E:/python-course/homework_zero_class/lesson15/文件写入-times_1.py", line 8, in <module>
# #     with open(file_name, encoding='utf-8') as file_obj:
# # NameError: name 'file_name' is not defined


file_name = 'demo.txt'
with open(file_name,'w',encoding='utf-8') as file_obj:
    # write()来向文件中写内容
    file_obj.write('Ke hou hao hao fu xi!')


# a表示追加内容

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
