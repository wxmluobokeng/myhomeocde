#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/8/7 0:27
# @Author : 老萝卜
# @File : 读取文件-times_2.py
# @Software: PyCharm Community Edition

file_name = 'demo2.txt'
try:
    with open(file_name,encoding='utf-8') as file_obj:
        # print(file_obj.read())
        content = file_obj.read()
        print(content)


except FileNotFoundError:
    print(f'{file_name}文件不存在')