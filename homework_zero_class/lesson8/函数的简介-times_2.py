#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/21 23:43
# @Author : 老萝卜
# @File : 函数的简介-times_2.py
# @Software: PyCharm Community Edition

print('nihao')
print('黑猫警长')
print('hahaha')

# 函数中保存的代码不会立即执行，需要调用函数才会执行
def fn():
    print('这是第一个函数')
    print('nihao')
    print('黑猫警长')
    print('hahaha')

print(fn)
fn()
fn()
fn()
fn()

# fn是函数对象 fn() 调用函数
# print函数对象 print() 调用函数