#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/25 14:03
# @Author : 老萝卜
# @File : 高阶函数-times_2.py
# @Software: PyCharm Community Edition
lst = [1,2,3,4,5,6,7,8,9,10]



def fn(lst):
    new_lst=[]
    for b in lst:
        if b % 2==0:
            new_lst.append(b)
    return new_lst
print(fn(lst))

def fn(lst):
    new_lst=[]
    for b in lst:
        if b % 2!=0:
            new_lst.append(b)
    return new_lst
print(fn(lst))

# 定义一个函数用来检测任意数>5
def fn(lst):
    new_lst=[]
    for b in lst:
        if b>5:
            new_lst.append(b)
    return new_lst
print(fn(lst))


def fn(lst):
    def fn2(i):
        if i % 2 == 0:
            return True
        return False

    def fn3(i):
        if i>5:
            return True
        return False

    for b in lst:
        if fn3(b):
            new_lst.append(b)
    return new_lst

print(fn(lst))


def fn2(i):
    if i % 2 == 0:
        return True
    return False


def fn3(i):
    if i > 5:
        return True
    return False

def fn4(i):
    if  i%3==0:
        return True
    return False

def fn(func,lst):
    new_lst=[]
    for b in lst:
        # if fn2(b):
        # if not fn2(b):
        if func(b):
            new_lst.append(b)
    return new_lst

print(fn(fn2,lst))
print(fn(fn3,lst))
print(fn(fn4,lst))