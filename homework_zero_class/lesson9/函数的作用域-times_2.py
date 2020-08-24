#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/23 00:12
# @Author : 老萝卜
# @File : 函数的作用域-times_1.py
# @Software: PyCharm Community Edition



# 作用域(scope)
# 作用域指的是变量生效的区域

# 在Python当中一共有两种作用域:全局作用域 和  函数作用域

def fn():
    # a定义在了函数内部，所有它的作用域就是函数内部，函数外部访问不到
    a=10
    print("函数内部a=",a)

fn()   # 函数内部a= 10
# print("函数外部a=", a)    # NameError: name 'a' is not defined




b = 20

def fn1():
    # a定义在了函数内部，所有它的作用域就是函数内部，函数外部访问不到
    a = 10
    print('函数内部:','a =',a)
    print('函数内部:','b =',b)

fn1()
print('函数外部:', 'b =', b)
# 函数内部: a = 10
# 函数内部: b = 20
# 函数外部: b = 20




def fn2():
    a = 30
    def fn3():
        a = 80
        print("fn3中：a =",a)
        print("fn3中：b =",b)
    fn3()
    print("fn2中：a =", a)

fn2()
# fn3中：a = 80
# fn3中：b = 20
# fn2中：a = 30



def fn4():
    # 如果希望在函数内部修改全局变量，则需要使用一个global关键字，来声明变量
    global a # 声明在函数内部的使用a是全局变量，此时我们修改a，就是在修改全局变量
    b = 80
    print('函数内部:', 'b =', b)

fn4()
print('函数外部:','b =',b)

# 函数内部: b = 80
# 函数外部: b = 20