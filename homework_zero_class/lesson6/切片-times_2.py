#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/14 23:18
# @Author : 老萝卜
# @File : 切片-times_2.py
# @Software: PyCharm Community Edition




hero = ['a','b','c','d','e','f']

# 通过切片会获取一个新的列表，不会影响原来的列表
print(hero[2:4]) # ['c', 'd']
print(hero)

#　起始位置和结束位置可以不写
# 如果省略结束位置 则从当前的位置会一直截取到最后
print(hero[1:])   # ['b', 'c', 'd', 'e', 'f']

# 如果省略开始位置 则会从第一个元素截取到结束位置，但是不包括结束位置的元素
print(hero[:3]) # ['a', 'b', 'c']

# 如果开始位置和结束位置都省略，则会从第一个位置截取到最后一个位置上面的元素 (全部)
print(hero[:]) # ['a', 'b', 'c', 'd', 'e', 'f']

# 步长表示每次获取元素的间隔，默认值为1,可以省略
# 步长可以为负数但是不能为0
print(hero[0:5:1]) # ['a', 'b', 'c', 'd', 'e']
print(hero[0:5]) # ['a', 'b', 'c', 'd', 'e']
print(hero[0:5:2]) # ['a', 'c', 'e']
print(hero[0:5:3])# [a, 'd']
print(hero[::2]) # ['a', 'c', 'e']
print(hero[::-1]) # ['f', 'e', 'd', 'c', 'b', 'a']
# print(hero[::0]) # ValueError: slice step cannot be zero
print(hero[4:1:-1]) # ['e', 'd', 'c']


