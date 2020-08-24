#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/18 21:59
# @Author : 老萝卜
# @File : 遍历字典-times_1.py
# @Software: PyCharm Community Edition

# d.keys() 该方法返回的是一个序列，保存的是字典中所有的键
# d.values() 该方法返回的是一个序列，保存的是字典中的值
# d.items() 该方法会返回字典中所有的项 。它返回的也是一个序列
#           这个序列当中包含有双值子序列 双值就是字典中的key-value

d = {'name':'钢铁侠','age':38,'sex':'男'}
print(d,type(d))
# {'name': '钢铁侠', 'age': 38, 'sex': '男'} <class 'dict'>

print(d.keys())
# dict_keys(['name', 'age', 'sex'])

for k in d.keys():
    print(d[k])
# 钢铁侠
# 38
# 男


for v in d.values():
    print(v)
# 钢铁侠
# 38
# 男

print(d.items())
# dict_items([('name', '钢铁侠'), ('age', 38), ('sex', '男')])

for k,v in d.items():
    print(k,'=',v)

# name = 钢铁侠
# age = 38
# sex = 男