#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/12 13:20
# @Author : 老萝卜
# @File : input函数-times_1.py
# @Software: PyCharm Community Edition

#会接受一个标准的输入的数据 返回的类型string类型 调用这个函数之后 程序会立即暂停，等待用户输入
input()

print(123)

# 获取用户输入的内容 ，如果是python 则验证成功
# 先获取用户输入的内容

content = input('请输入:')
# # 判断用户输入的内容是否是python

if content == 'python':
    print('验证正确！！！')



