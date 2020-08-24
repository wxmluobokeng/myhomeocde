#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/8/7 0:23
# @Author : 老萝卜
# @File : 读取文件-times_1.py
# @Software: PyCharm Community Edition


# 调用open()来打开一个文件的时候，可以将文件分为两种类型
# 第一种 是纯文本(使用utf-8等编写的文本文件)
# 第二种 是二进制文件(音频、视频、图片...)
# open()函数它默认打开文件是以纯文本的形式

file_name = 'demo2.txt'
try:
    with open(file_name,encoding='utf-8') as file_obj:
        # print(file_obj.read())
        content = file_obj.read()
        print(content)


except FileNotFoundError:
    print(f'{file_name}文件不存在')