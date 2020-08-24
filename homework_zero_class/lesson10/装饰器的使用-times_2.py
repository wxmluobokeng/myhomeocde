#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/25 20:10
# @Author : 老萝卜
# @File : 装饰器的使用-times_2.py
# @Software: PyCharm Community Edition



def start_end():
    # 创建一个新的函数
    def new_function(*args,**kwargs):
        pass
    # 返回函数
    return new_function

def fn():
    print('我是fn函数')

f1=start_end()
f2=start_end()
print("f1=",f1)
print("f2=",f2)
# f1= <function start_end.<locals>.new_function at 0x00000000025857B8>
# f2= <function start_end.<locals>.new_function at 0x0000000002585840>


# 对fn函数进行修改
def start_end():
    # 创建一个新的函数
    def new_function():
        print('函数开始执行.....')
        fn()
        print('函数执行结束.....')

    # 返回函数
    return new_function
f=start_end()
f()
# 函数开始执行.....
# 我是fn函数
# 函数执行结束.....



def add(a,b):
    return a + b

def start_end(old):
    # 创建一个新的函数
    def new_function(a,b):
        print('函数开始执行.....')
        r=old(a,b)
        print('函数执行结束.....')
        return r
    # 返回函数
    return new_function
f=start_end(add)
# f()   #TypeError: new_function() missing 2 required positional arguments: 'a' and 'b'
r=f(1,2)
print(r)
# 函数开始执行.....
# 函数执行结束.....
# 3

def start_end(old):
    # 创建一个新的函数
    def new_function(*args,**kwargs):
        print('函数开始执行.....')
        r = old(*args,**kwargs)
        print('函数执行结束.....')
        return r
    # 返回函数
    return new_function

f=start_end(fn)
f()
f=start_end(add)
r=f(1,2)
print(r)
# 函数开始执行.....
# 我是fn函数
# 函数执行结束.....
# 函数开始执行.....
# 函数执行结束.....
# 3

