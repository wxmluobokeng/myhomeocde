#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/25 18:38
# @Author : 老萝卜
# @File : 装饰器的引入-times_2.py
# @Software: PyCharm Community Edition


# 求任意两个数的和
def add(a,b):
    return a + b

def mul(a,b):
    return a * b

r=add(1,2)
print(r)



# 给函数增加两个功能
def add(a,b):
    print("函数正在计算")
    print("函数计算结束")
    return a + b


def mul(a,b):
    print("函数正在计算")
    print("函数计算结束")
    return a * b

r = add(1, 2)
print(r)


#　我们可以通过修改函数中的代码来完成这个需求，但是会产生一些问题
# 问题一 如果要修改的函数过多，修改起来比较麻烦
# 问题二 不方便后期的维护
# 问题三 违反开闭原则(ocp) 程序的设计思想 要求开发对程序的扩展，要关闭对程序的修改

# 希望在不修改原函数的前提下，来多函数扩展功能

def fn():

    print('我是fn函数')

# 创建一个新的函数来对原函数进行扩展
def fn2():

    print('函数开始执行.....')
    fn()
    print('函数执行结束.....')


fn2()
fn()


def new_add(a,b):

    print('函数开始执行.....')
    r = add(a,b)
    print('函数执行结束.....')
    return r

r = new_add(1,2)
print(r)

