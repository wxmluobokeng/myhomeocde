#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/18 20:05
# @Author : 老萝卜
# @File : 字典简介-times_1.py
# @Software: PyCharm Community Edition


# 　字典 dict
# 数据结构 映射(mapping)
# 字典的作用其实和列表类似，用来存储对象的容器
# 列表存储数据的性能非常好，但是查询数据的性能很差。字典正好相反
# 在字典当中每一个元素都有唯一的一个名字 通过这个名字可以快速查询到指定的元素
# 这个唯一的名字我们一般称之为 键(key) 通过key我们可以查询value 值
# 所以字典我们也称之为键值对(key-value)
# 每个字典当中可以有多个键值对，每一个键值对我们可以称之为一项(item)

# 语法: {key:value,key:value....}
# 字典中的键是不能重复的，如果重复后面的会替换前面的
d = {'name':'钢铁侠','age':38,'sex':'男','name':'葫芦娃'}
pirnt(d)

headers = {
    'user-agent': 'xxxx',
    'cookie': 'xxxxx'

}
print(headers, type(headers))

# 需要根据键来获取值
print(d['name'],d['age'],d['sex'])
n="name"
print(d[n])