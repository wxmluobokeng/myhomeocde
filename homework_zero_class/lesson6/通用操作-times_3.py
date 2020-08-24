#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/15 0:02
# @Author : 老萝卜
# @File : 通用操作-times_3.py
# @Software: PyCharm Community Edition

# + *  ,没有- 和  /
# 列表 + 列表 ： 可以将两个列表拼接成一个列表
lst = [1,2,3] + [4,5,6]
# 列表 * 整数 ： 可以将列表重复指定的次数
lst = [1,2,3] * 2           # [1,2,3,1,2,3]
print(20 * [1,2,3])         # [1,2,3,1,2,3]
# lst = [1,2,3] * [4,5,6] # TypeError: can't multiply sequence by non-int of type 'list'
# lst = [1,2,3,4] -[2,3]  # TypeError: unsupported operand type(s) for -: 'list' and 'list'


# in 和 not in
# in用来检测指定预算是否在列表中
# not in 用来检测指定元素是否不在列表中
hero = ['钢铁侠','绿巨人','蜘蛛侠','黑寡妇','蚁人','美国队长']

print('绿巨人' in hero) # True

print('蝙蝠侠' not in hero) #  True

#　min() 获取列表中的最小值 max() 列表中的最大值

lst = [1,2,3,4,5,6]

print(min(lst),max(lst))
# 注： 列表中元素类型相同，有可比性才行
# print(max(1,"str",None)) #TypeError: '>' not supported between instances of 'str' and 'int'
# print(max(1,None)) #TypeError: '>' not supported between instances of 'NoneType' and 'int'


# s.index(x[, i[, j]])，s.count(x)

# 函数和方法的区别
# xxx()     函数 fun
# yyy.xxx() 方法 (比较特殊的函数) method

# s.index(x[, i[, j]])  x：待查找的元素，i是查找的起始位置，j 是查找的结束位置，返回元素在列表中，指定区间的位置

hero = ['钢铁侠','绿巨人','蜘蛛侠','黑寡妇','蚁人','美国队长','蜘蛛侠','蜘蛛侠','蜘蛛侠']

print(hero.index('蜘蛛侠'))  # 2

print(hero.index('蜘蛛侠',3,7)) # 6


#  s.count(x) 获取指定元素在列表中出现的次数

print(hero.count('蜘蛛侠'))   # 4
print(hero.count('超人'))     # 0
# print(hero.count('蜘蛛侠',3,8))   # TypeError: count() takes exactly one argument (3 given)
print(hero[3:].count('蜘蛛侠'))  #3            # s.count()无法指定区间，只有选进行切片后，再进行统计
