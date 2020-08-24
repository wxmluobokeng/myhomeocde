#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/8/8 11:45
# @Author : 老萝卜
# @File : 迭代器-times_2.py
# @Software: PyCharm Community Edition


from collections import Iterable

lst = [1, 2, 3, 4]
r = isinstance(lst, Iterable)
print(r)                            # True
r = isinstance('abc', Iterable)
print(r)                            # True
r = isinstance(132, Iterable)
print(r)                            # False
s = (x + 1 for x in range(5))       # 由列表推导式生成的生成器
r = isinstance(s, Iterable)         # True


# print(next(lst))          # 列表是可迭代的，但不是迭代器
# # Traceback (most recent call last):
# #   File "E:/python-course/homework_zero_class/lesson16/迭代器-times_1.py", line 35, in <module>
# #     print(next(lst))
# # TypeError: 'list' object is not an iterator


# iter(lst)
# 通过iter()函数可以将可迭代的变成一个迭代器

lst1=iter(lst)
print(next(lst1))
print(next(lst1))
print(next(lst1))
# 1
# 2
# 3

# 生成器和迭代器
# 生成器的出现是为了优化程序节省内存
# 迭代器是一个大的范围而生成器只是迭代器的一种