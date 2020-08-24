#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/8/7 0:29
# @Author : 老萝卜
# @File : 读取大文件-times_1.py
# @Software: PyCharm Community Edition

# read()来读取内容的时候
# 它会直接将全部内容读取出来。如果要读取的内容比较大，会一次性加载到内存当中，这个时候就容易导致内存溢出

file_name = 'demo2.txt'
try:
    with open(file_name,encoding='utf-8') as file_obj:
        help(file_obj.read)
        content = file_obj.read()
        print(content)
except FileNotFoundError:
    print(f'{file_name}文件不存在')


# 可以为size指定一个值，这样我们会读取指定数量的字符
# 每一次读取的位置都是从上一次读取到的位置接着读取


file_name = 'demo2.txt'
try:
    with open(file_name,encoding='utf-8') as file_obj:
        help(file_obj.read)
        content = file_obj.read(-1)
        print(content)
except FileNotFoundError:
    print(f'{file_name}文件不存在')


file_name = 'demo2.txt'
try:
    with open(file_name,encoding='utf-8') as file_obj:
        content = file_obj.read(6)
        print(len(content),content,end="")
        content = file_obj.read(6)
        print(len(content),content,end="")
        content = file_obj.read(6)
        print(len(content),content,end="")
        content = file_obj.read(6)
        print(len(content),content,end="")
except FileNotFoundError:
    print(f'{file_name}文件不存在')
# 6 白日依山尽
# 6 黄河入海流
# 6 欲穷千里目
# 5 更上一层楼


# 如果设置的这个size大于剩余字符的数量，它会一下全部把剩余的部分读取

try:
    with open(file_name,encoding='utf-8') as file_obj:

        # 定义一个变量，指定每次读取字符的数量
        chunk = 100
        # 创建一个循环来读取文件的内容
        while True:
            content = file_obj.read(chunk)
            # 退出循环
            if not content:
                # 内容读完了 退出循环
                break
            print(content,end='')

except FileNotFoundError:
    print(f'{file_name}文件不存在')