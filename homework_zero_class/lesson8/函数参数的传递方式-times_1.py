#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/22 0:11
# @Author : 老萝卜
# @File : 函数参数的传递方式-times_1.py
# @Software: PyCharm Community Edition


def fn(a = 5,b = 6,c =10):
    print('a =',a)
    print('b =',b)
    print('c =',c)

fn(1,2,3)
fn(1,2)
fn()

# 参数的传递方式

# 位置传参
# 位置参数：位置参数就是将对应位置的实参赋值给对应位置的形参
# fn(1,2,3) --> def fn(a,b,c)

def fn2(a ,b ,c ):
    print('a =',a)
    print('b =',b)
    print('c =',c)

# 关键字传参
# 关键字参数可以不按照形参定义的顺序去传递，而根据参数名进行传递
fn2(b=1,c=2,a=3)
fn(1,2,c=20) # 位置传参和关键字传参可以混合使用
# fn2(c=20,1,2) # SyntaxError: positional argument follows keyword argument

# import requests
# headers = {}
# data = {}
# url = ''
# requests.get(url,headers=headers,data=data) # 为什么
# requests.request(headers=headers,url)
'''
因为函数参数的传递方式决定的，函数参数有两种：实参和形参，定义时用形参，调用函数时用实参，实参与形参一一对应。函数参数有两种传递方式，位置传参和关键字传参，这两种方式可以混合一起使用，但是，混合使用位置参数和关键字参数的时候必须将位置参数写到关键字参数前面，url是位置传参，headers=headers 是关键字传参。
'''