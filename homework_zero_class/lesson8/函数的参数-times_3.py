#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/22 00:01
# @Author : 老萝卜
# @File : 函数的参数-times_3.py
# @Software: PyCharm Community Edition

# 定义一个函数 可以用来求任意2个数的和
# 在定义函数的时候可以在括号后面定义和数量不等的形参 多个形参用,隔开

def s1():
    a=1
    b= 2
    print(a+b)

def s2(a,b):
    print('a =',a)
    print('b =',b)
    print(a,'+',b,'=',a+b)

s1()
# s2() # TypeError: s() missing 2 required positional arguments: 'a' and 'b'
s2(10000,6)


