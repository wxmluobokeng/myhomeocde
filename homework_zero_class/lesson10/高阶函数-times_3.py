#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/25 14:37
# @Author : 老萝卜
# @File : 高阶函数-times_3.py
# @Software: PyCharm Community Edition


# 高阶函数
# 特点一 接收一个或多个函数作为参数
# 特点二 将函数作为返回值

# 当我们使用一个函数作为参数的时候，实际上是将指定的代码传递了目标函数

# 需求:将一个指定列表中的偶数，保存到一个新的列表中返回

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# 定义一个函数用来检测任意数的偶数
def fn(lst):
    # 参数lst 需要筛选的列表
    # 创建一个新列表，保存数据
    new_lst = []
    # 对需要筛选的列表进行遍历
    for b in lst:
        if b % 2 == 0:  # 判断 n 为偶数
            new_lst.append(b)
    return new_lst


print(fn(lst))


# 定义一个函数用来检测任意数的奇数
def fn(lst):
    # 参数lst 需要筛选的列表
    # 创建一个新列表，保存数据
    new_lst = []
    # 对需要筛选的列表进行遍历
    for b in lst:
        if b % 2 != 0:  # 判断 n 为奇数
            new_lst.append(b)
    return new_lst


print(fn(lst))


# 定义一个函数用来检测任意数>5
def fn(lst):
    # 参数lst 需要筛选的列表
    # 创建一个新列表，保存数据
    new_lst = []
    # 对需要筛选的列表进行遍历
    for b in lst:
        if b > 5:  # 判断 n >5
            new_lst.append(b)
    return new_lst


print(fn(lst))


def fn(lst):
    # 定义一个函数 用来检测任意数是否偶数
    def fn2(i):
        if i % 2 == 0:
            return True
        return False

    def fn3(i):
        if i > 5:
            return True
        return False

    # 创建一个新列表，保存数据
    new_lst = []
    # 对需要筛选的列表进行遍历
    for b in lst:
        # if fn2(b):    # 判断 n 为偶数
        # if not fn2(b):  # 判断 n 为奇数
        if fn3(b):  # 判断 n >5
            new_lst.append(b)
    return new_lst


print(fn(lst))


# 定义一个函数 用来检测任意数是否偶数
def fn2(i):
    if i % 2 == 0:
        return True
    return False


def fn3(i):
    if i > 5:
        return True
    return False


def fn4(i):
    if i % 3 == 0:
        return True
    return False


def fn(func, lst):
    # 创建一个新列表，保存数据
    new_lst = []
    # 对需要筛选的列表进行遍历
    for b in lst:
        # if fn2(b):    # 判断 n 为偶数
        # if not fn2(b):  # 判断 n 为奇数
        if func(b):  # 判断 n >5
            new_lst.append(b)
    return new_lst


print(fn(fn2, lst))
print(fn(fn3, lst))
print(fn(fn4, lst))

lst1 = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]


# 定义一个函数 用来检测任意数是否偶数
def plus_square(a, b):
    return a ** 2 + b ** 2


def subtraction_squeare(a, b):
    return a ** 2 - b ** 2


def average_squeare(a, b):
    return plus_square(a, b) / 2


def fn(func, lst):
    # 创建一个新列表，保存数据
    new_lst = []
    # 对需要筛选的列表进行遍历
    for a, b in lst:
        new_lst.append(func(a, b))
    return new_lst


print(fn(plus_square, lst1))
print(fn(subtraction_squeare, lst1))
print(fn(average_squeare, lst1))
