#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/21 23:43
# @Author : 老萝卜
# @File : 函数的简介-times_3.py
# @Software: PyCharm Community Edition


# 函数中保存的代码不会立即执行，需要调用函数才会执行
def fn():
	print("hello world!")
	result="我是函数返回值"
	return result


# fn是函数对象 fn() 调用函数
# print函数对象 print() 调用函数

print(fn)
print(fn())