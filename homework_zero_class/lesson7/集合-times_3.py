#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/18 19:45
# @Author : 老萝卜
# @File : 集合-times_3.py
# @Software: PyCharm Community Edition

# 集合 set
# 集合和列表非常相似
# 不同点
# 1 集合中只能存储不可变对象
# 2 集合中存储的对象是无序的
# 3 集合中不能出现重复的元素

s = {100,3,4,1,1,1,1,20,10}
print(s,type(s))
# {1, 3, 4, 10, 20, 100} <class 'set'>

# s = {[1,2,3],[4,5,6]}  # TypeError: unhashable type: 'list'

s = {}
print(s,type(s))
#{} <class 'dict'>

s = {1,2,3}
print(s, type(s))
#　{1, 2, 3} <class 'set'>
s = {1,2,3,}
print(s, type(s))
#　{1, 2, 3} <class 'set'>


# set() 可以将序列和字典转换为集合
s = set()
# set()

s = set([1,2,3,4,5,1,2,3,4,5])
# {1, 2, 3, 4, 5}

s = set('hello')
# {'e', 'h', 'l', 'o'}

s = set({'a':1,'b':2,'c':3,"d":4}) # 使用set()函数将字典转换为集合的时候，只会包含字典中的键
# {'a', 'b', 'c'}

s = {'a','b',1,2,3}
print(s, type(s))
# {1, 2, 3, 'b', 'a'} <class 'set'>

# print(s[1])         # TypeError: 'set' object does not support indexing

print(list(s)[0])
# 1

