#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/14 20:40
# @Author : 老萝卜
# @File : 求列表合集.py
# @Software: PyCharm Community Edition

'''
有两个列表 lst1 = [11, 22, 33] lst2 = [22, 33, 44]获取内容相同的元素
'''

lst1=[11, 22, 33]
lst2=[22, 33, 44]


result= []
# 方法一:将lst1列表的每一个元素取出，判断是否在lst2中，如果存在，就插入到结果列表中
for item in lst1:
    if item in lst2:
        result.append(item)
print(result)


# 方法二:将lst1赋值给结果列表，将lst1列表的每一个元素取出，判断是否不在lst2中，如果不在，将此元素从结果列中删除
result=lst1
for item in lst1:
    if item not in lst2:
        result.remove(item)
print(result)
