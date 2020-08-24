#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/18 19:59
# @Author : 老萝卜
# @File : 字典简介-times_2.py
# @Software: PyCharm Community Edition

d = {'name':'钢铁侠','age':38,'sex':'男','name':'葫芦娃'}
print(d)

headers = {
    'user-agent': 'xxxx',
    'cookie': 'xxxxx'

}
print(headers, type(headers))

# 需要根据键来获取值
print(d['name'],d['age'],d['sex'])
n="name"
print(d[n])