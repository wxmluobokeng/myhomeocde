#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/25 15:27
# @Author : 老萝卜
# @File : 匿名函数-times_1.py
# @Software: PyCharm Community Edition

# filter()
# 参数 1 函数 2 需要过滤的序列(可迭代的) 返回值 过滤后的新的序列（可迭代的结构）

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def fn4(i):
    if i % 3 == 0:
        return True
    return False


print(list(filter(fn4, lst)))
print(list(filter(lambda x: x % 3 == 0, lst)))


# 匿名函数 lambda函数表达式
#  lambda函数表达式就是专门用来创建一些简单的函数
# 语法：lambda 参数列表 ： 返回值
def fn5(a, b):
    return a + b


print(fn5(1, 2))
print(lambda a, b: a + b)  # <function <lambda> at 0x00000000025857B8>
print((lambda a, b: a + b)(5, 6))  # 11
fn6 = lambda a, b: a + b
print(fn6(5, 6))


nums = [2, 3, 6, 12, 15, 18]

def nums_res(x):
    return x % 2 == 0 and x % 3 == 0

fn = lambda x: x % 2 == 0 and x % 3 == 0
print(list(filter(nums_res, nums)))
print(list(filter(fn, nums)))
print(list(filter(lambda x: x % 2 == 0 and x % 3 == 0, nums)))
