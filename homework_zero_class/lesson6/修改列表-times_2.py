#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/15 0:47
# @Author : 老萝卜
# @File : 修改列表-times_2.py.py
# @Software: PyCharm Community Edition

hero = ['钢铁侠','绿巨人','蜘蛛侠','黑寡妇','蚁人','美国队长']

hero[0] = '雷神'

print(hero) # ['雷神', '绿巨人', '蜘蛛侠', '黑寡妇', '蚁人', '美国队长']

hero = ['钢铁侠','绿巨人','蜘蛛侠','黑寡妇','蚁人','美国队长']
print('修改前:',hero)

# 通过 del 来删除元素 关键字
del hero[2]

print('修改后:',hero)

# 通过切片来修改
print('修改前:',hero)
hero[0:3] = 'abcd'  #['a', 'b', 'c', 'd', '蚁人', '美国队长']
print('修改后:',hero)

# hero[0:3] = 123 # TypeError: can only assign an iterable 必须传递的是一个序列

hero = ['钢铁侠','绿巨人','蜘蛛侠','黑寡妇','蚁人','美国队长']
hero[0:2] = ['黑豹','雷神','灭霸']
print('修改后:',hero)

hero = ['钢铁侠','绿巨人','蜘蛛侠','黑寡妇','蚁人','美国队长']
hero[0:0] = ['雷神'] #　向索引为０的位置插入了一个元素
print('修改后:',hero)

# 当设置了步长的时候，序列中元素的个数必须和切片中元素的个数保持一致
# hero[::2] = ['雷神'] # ValueError: attempt to assign sequence of size 1 to extended slice of size 3
hero = ['钢铁侠','绿巨人','蜘蛛侠','黑寡妇','蚁人','美国队长']
hero[::2] = ['雷神','灭霸','黑豹']
print(hero[::2])

# 可以通过切片来删除元素
hero = ['钢铁侠','绿巨人','蜘蛛侠','黑寡妇','蚁人','美国队长']
hero[1:3] = []
print('修改后:',hero)

# s = 'python'
# s[1] = 'j'
# print(s) # TypeError: 'str' object does not support item assignment

s = 'python'
s = list(s)
s[1] = 'j'
print(s)

print('修改后:',hero)
