#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/8/7 0:47
# @Author : 老萝卜
# @File : 其他的读取方式-times_2.py
# @Software: PyCharm Community Edition


file_name = 'demo.txt'

with open(file_name,encoding='utf-8') as file_obj:
    # file_obj.readline() 该方法用来读取一行的内容
    print(file_obj.read())
    print(file_obj.readline(),end='')
    print(file_obj.readline(),end='')
    print(file_obj.readline())

with open(file_name, encoding='utf-8') as file_obj:
    # file_obj.readlines() 将读取的内容放到一个列表中返回
    r = file_obj.readlines()
    print(r)