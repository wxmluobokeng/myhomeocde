#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/8/8 11:58
# @Author : 老萝卜
# @File : 迭代器-times_3.py
# @Software: PyCharm Community Edition

# 迭代：就是在一些元素中获取元素的过程或者是一种方式

# 可迭代: 可以在迭代中使用
# 可迭代对象 1. 生成器 2. 列表、元祖、字符串、字典...

# 生成器是可迭代的，也是迭代器
# 列表是可迭代的。但是它不是迭代器

from collections import Iterable

lst = [1, 2, 3, 4]
r = isinstance(lst, Iterable)
print(r)  # True
r = isinstance('abc', Iterable)
print(r)  # True
r = isinstance(132, Iterable)
print(r)  # False
s = (x + 1 for x in range(5))  # 由列表推导式生成的生成器
r = isinstance(s, Iterable)  # True

# 迭代器 它是一个可以记住遍历位置的对象。迭代器对象从序列中的一个元素开始访问，直到所有的元素被访问完结束，而且只能往前不能往后
# 可以被next()函数调用并不断返回下一个值的对象我们称之为迭代器 Iterator

# print(next(lst))          # 列表是可迭代的，但不是迭代器
# # Traceback (most recent call last):
# #   File "E:/python-course/homework_zero_class/lesson16/迭代器-times_1.py", line 35, in <module>
# #     print(next(lst))
# # TypeError: 'list' object is not an iterator


# iter(lst)
# 通过iter()函数可以将可迭代的变成一个迭代器

lst1 = iter(lst)
print(next(lst1))
print(next(lst1))
print(next(lst1))
# 1
# 2
# 3

# 生成器和迭代器
# 生成器的出现是为了优化程序节省内存
# 迭代器是一个大的范围而生成器只是迭代器的一种


list1 = [str(i + 1) for i in range(10)]
# print("\t","\t\t","list1=",list1)
print("i\t", "item\tlist1=", list1)
for i, item in enumerate(list1):
    if item in ("2", "3", "6"):
        list1.remove(item)
    print(i, "\t", item + "\t\tlist1=", list1)
print("遍历后:", list1)
# i	 item	list1= ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# 0 	 1		list1= ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# 1 	 2		list1= ['1', '3', '4', '5', '6', '7', '8', '9', '10']
# 2 	 4		list1= ['1', '3', '4', '5', '6', '7', '8', '9', '10']
# 3 	 5		list1= ['1', '3', '4', '5', '6', '7', '8', '9', '10']
# 4 	 6		list1= ['1', '3', '4', '5', '7', '8', '9', '10']
# 5 	 8		list1= ['1', '3', '4', '5', '7', '8', '9', '10']
# 6 	 9		list1= ['1', '3', '4', '5', '7', '8', '9', '10']
# 7 	 10		list1= ['1', '3', '4', '5', '7', '8', '9', '10']
# 遍历后: ['1', '3', '4', '5', '7', '8', '9', '10']


from collections import Iterator
r = isinstance([1, 2, 3, 4], Iterator)
print(r)                                    # False
r = isinstance((1, 2, 3, 4), Iterator)
print(r)                                    # False
r = isinstance('abc', Iterator)
print(r)                                    # False
r = isinstance({'a': 1, 'b': 2}, Iterator)
print(r)                                    # False
r = isinstance({1, 2, 3}, Iterator)
print(r)                                    # False
r = isinstance(132, Iterator)
print(r)                                    # False
s = (x + 1 for x in range(5))  # 由列表推导式生成的生成器
r = isinstance(s, Iterator)                 # True
print(r)
r = isinstance(iter([1, 2, 3, 4]), Iterator)
print(r)                                    # True
r = isinstance(iter((1, 2, 3, 4)), Iterator)
print(r)                                    # True
r = isinstance(iter('abc'), Iterator)
print(r)                                    # True
r = isinstance(iter({'a': 1, 'b': 2}), Iterator)
print(r)                                    # True
r = isinstance(iter({1, 2, 3}), Iterator)
print(r)                                    # True
# r = isinstance(iter(132), Iterator)
# # Traceback (most recent call last):
# #   File "E:/python-course/homework_zero_class/lesson16/迭代器-times_3.py", line 100, in <module>
# #     r = isinstance(iter(132), Iterator)
# # TypeError: 'int' object is not iterable


vList=[1,2,3,4]
vIter=iter(vList)  #从列表生成迭代器对象
for i in vIter:
    print('第一次：',i)   #输出迭代器中的数据1、2、3、4
for i in vIter:
    print('第二次:',i)  #再次输出没有数据，因为迭代器已经空了
# 第一次： 1
# 第一次： 2
# 第一次： 3
# 第一次： 4

vList=[1,2,3,4]
for i in vList:
    print('第一次：',i)
for i in vList:
    print('第二次:',i)
# 第一次： 1
# 第一次： 2
# 第一次： 3
# 第一次： 4
# 第二次: 1
# 第二次: 2
# 第二次: 3
# 第二次: 4


print("-"*8)
vList=[1,2,3,4]
vIter=iter(vList)
while True:
    try:
        i=next(vIter)
    except:
        break
    print('第一次：',i)
while True:
    try:
        i=next(vIter)
    except:
        break
    print('第二次：',i)
# print(next(vIter))
# # Traceback (most recent call last):
# #   File "E:/python-course/homework_zero_class/lesson16/迭代器-times_3.py", line 148, in <module>
# #     print(next(vIter))
# # StopIteration


#while循环如果执行第二次机也不会输出。


# 第一次： 1
# 第一次： 2
# 第一次： 3
# 第一次： 4