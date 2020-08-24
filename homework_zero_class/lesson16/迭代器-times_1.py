#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/8/8 11:25
# @Author : 老萝卜
# @File : 迭代器-times_1.py
# @Software: PyCharm Community Edition

# 迭代：就是在一些元素中获取元素的过程或者是一种方式

# 可迭代: 可以在迭代中使用
# 可迭代对象 1. 生成器 2. 列表、元祖、字符串、字典...

# 生成器是可迭代的，也是迭代器
# 列表是可迭代的。但是它不是迭代器

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


# 迭代器 它是一个可以记住遍历位置的对象。迭代器对象从序列中的一个元素开始访问，直到所有的元素被访问完结束，而且只能往前不能往后
# 可以被next()函数调用并不断返回下一个值的对象我们称之为迭代器 Iterator

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