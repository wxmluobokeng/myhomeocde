#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/8/4 23:18
# @Author : 老萝卜
# @File : 模块-times_3.py
# @Software: PyCharm Community Edition


# 在Python中一个py文件就是一个模块
# 在一个模块中引入外部模块
# 1. import 模块名 (模块名就是Python的文件名)
# 可以引入同一个模块多次，但是模块只会执行一次

import test_m
import test_m
import test_m
import test_m
# 这是我的第一个模块
print(test_m)
# <module 'test_m' from 'E:\\python-course\\homework_zero_class\\lesson14\\test_m.py'>

# 2. import 模块名 as 模块别名
import test_m as test
print(test_m)
print(test)
# <module 'test_m' from 'E:\\python-course\\homework_zero_class\\lesson14\\test_m.py'>
# <module 'test_m' from 'E:\\python-course\\homework_zero_class\\lesson14\\test_m.py'>

# __name__ 在每一个模块内部都有__name__ 我们可以获取模块的名字

# 这是我的第一个模块
# test_m

# 模块的使用
# 访问模块中的变量 语法 模块名.变量名
print(test_m.a,test_m.b)
print(test_m.username,test_m.password)
# 1 2
# shuai jerry 123456


# 访问模块中的函数 语法 模块名.函数名
test_m.test2()
test_m.test1()
# test2
# test1

# import requests
#
# requests.get()
# requests.Session()

# 访问模块中的对象 语法 模块名.对象名

p = test_m.Person()
print(p)
print(p.name)
# <test_m.Person object at 0x00000000025B9BA8>
# 葫芦娃


# 我们也可以引入模块中的部分内容
# 语法 from 模块名 import 变量
from test_m import Person
from test_m import test1
from test_m import test2

# print(test_m) # NameError: name 'test_m' is not defined

p1 = Person()
print(p1)
test2()
# <test_m.Person object at 0x00000000025B9BA8>
# test2

# 3.语法 from 模块名 import 变量,变量,变量.....
from test_m import Person,test1,test2

test2()
# test2


def test1():
    print('我是主模块中的test1')
test1()
# 我是主模块中的test1

from test_m import Person,test1,test2
test1()
#  test1


from test_m import *
import test_m

#
# # 4.语法 from 模块名 import 变量 as 别名
from test_m import test1 as new_test1

test1()
new_test1()

import test_m

# import xxx
# import xxx as yyy
# from xxx import yyy,zzz,fff....
# from xxx import *
# from xxx import yyy as zzz

import test_m
a= test_m.Person()
a.test3()

