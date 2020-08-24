#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/18 19:35
# @Author : 老萝卜
# @File : 集合-times_2.py
# @Software: PyCharm Community Edition


s = {20,10,1,2,3,4,100,1,2,3,4,1,1,1}
print(s,type(s))
# {1, 2, 3, 4, 100, 10, 20} <class 'set'>

# s = {[1,2,3],[4,5,6]}  # TypeError: unhashable type: 'list'

s = {}
print(s,type(s))
#{} <class 'dict'>

s = {1,2,3}
print(s, type(s))
#　{1, 2, 3} <class 'set'>


# set() 可以将序列和字典转换为集合
s = set()
# set()

s = set([1,2,3,4,5,1,2,3,5,5])
# {1, 2, 3, 4, 5}

s = set('hello')
# {'e', 'h', 'l', 'o'}

s = set({'a':1,'b':2,'c':3}) # 使用set()函数将字典转换为集合的时候，只会包含字典中的键
# {'a', 'b', 'c'}

s = {'a','b',1,2,3}
print(s, type(s))
# {1, 2, 3, 'b', 'a'} <class 'set'>

# print(s[1])         # TypeError: 'set' object does not support indexing

print(list(s)[0])
# 1

