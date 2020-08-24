#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/14 23:52
# @Author : 老萝卜
# @File : 通用操作-times_2.py
# @Software: PyCharm Community Edition




# 列表 + 列表 ： 可以将两个列表拼接成一个列表
lst = [1,2,3] + [4,5,6]
# 列表 * 整数 ： 可以将列表重复指定的次数
lst = [1,2,3] * 2           # [1,2,3,1,2,3]
print(3 * [1,2,3])          # [1,2,3,1,2,3,1,2,3]
# lst = [1,2,3] * [4,5,6] # TypeError: can't multiply sequence by non-int of type 'list'


# in用来检测指定预算是否在列表中
# not in 用来检测指定元素是否不在列表中
hero = ['a','b','c','d','e','f']

print('a' in hero)  # True

print('g' not in hero) #  True

#　min() 获取列表中的最小值 max() 列表中的最大值

lst = [1,2,3,4,5,6]

print(min(lst),max(lst))   # 1 6



# 函数和方法的区别
# xxx()     函数 fun
# yyy.xxx() 方法 (比较特殊的函数) method

# s.index(x[, i[, j]])  x：待查找的元素，i是查找的起始位置，j 是查找的结束位置，返回元素在列表中，指定区间的位置


hero = ['a','b','c','e','e','f','c','c','c']
# s.index(x[, i[, j]])  x：待查找的元素，i是查找的起始位置，j 是查找的结束位置，返回元素在列表中，指定区间的位置

print(hero.index('c'))  # 2

print(hero.index('c',3,7)) # 6


#  s.count(x) 获取指定元素在列表中出现的次数

print(hero.count('c'))   # 4
print(hero.count('超人'))     # 0




