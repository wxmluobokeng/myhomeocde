#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/25 19:15
# @Author : 老萝卜
# @File : 装饰器的使用-times_3.py
# @Software: PyCharm Community Edition

# 定义一个函数来对其他的函数进行扩展，是其他的函数可以在执行前打印开始执行，执行后打印执行结束

# start_end(old)这一类函数我们就称之为装饰器
# 通过装饰器，可以在不修改原来的函数的情况下来对函数进行扩展
# 在开发中，我们都是通过装饰器来扩展函数的功能


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
#结论:每次运行得到一个新函数



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
#结论：已经修改，但被写死了


def add(a,b):
    return a + b

def start_end(old):
    # 创建一个新的函数
    def new_function():
        print('函数开始执行.....')
        old(a,b)
        print('函数执行结束.....')
    # 返回函数
    return new_function

f=start_end(add)
# f()   #NameError: name 'a' is not defined
print(f)
# <function start_end.<locals>.new_function at 0x0000000002585840>
# 结论：已返回函数，但没有执行


def start_end(old):
    # 创建一个新的函数
    def new_function(a,b):
        print('函数开始执行.....')
        old(a,b)
        print('函数执行结束.....')
    # 返回函数
    return new_function
f=start_end(add)
# f()         TypeError: new_function() missing 2 required positional arguments: 'a' and 'b'
f(1,2)
# 函数开始执行.....
# 函数执行结束.....
# 结论：已返回函数，已执行，但没有显示结果


def start_end(old):
    # 创建一个新的函数
    def new_function(a,b):
        print('函数开始执行.....')
        old(a,b)
        print('函数执行结束.....')

    # 返回函数
    return new_function
f=start_end(add)
#f()   #    def new_function(a,b):
r=f(1,2)
print(r)
# 函数开始执行.....
# 函数执行结束.....
# None
# 结论：已返回函数，已执行，但有显示结果,但不是我们想要的


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
# 结论：实现了功能扩展，得到了结果

f=start_end(fn)
# f()   #TypeError: new_function() missing 2 required positional arguments: 'a' and 'b'
# 结论：换个函数就报错


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
r=f(1234,5678)
print(r)
# 函数开始执行.....
# 我是fn函数
# 函数执行结束.....
# 函数开始执行.....
# 函数执行结束.....
# 3

#得到想要的