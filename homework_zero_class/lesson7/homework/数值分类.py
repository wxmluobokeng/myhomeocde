#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/18 18:41
# @Author : 老萝卜
# @File : 数值分类.py
# @Software: PyCharm Community Edition

'''
    有如下值集合[11,22,33,44,55,66,77,88,99,90], 将所有⼤于66的值保存 ⾄字典的第⼀个key中，将⼩于66值保存⾄第⼆个key的值中
    解题思路一:
    1、定义一个空字典
    2、遍历列表
    3、  判断当前值是否>66
    4、  如果>66,获取key>66的value (是个列表) :  采用字典.get(key[,default]) 第一次，没有key,将列表置空，第二次就有值了，取列表
    5、      将当前值追加到列表中
    6、      修改字典key的值（如果没有Key,会自动添加key-value）
    7、  如果<66,进行相同操作
    8、  如果=66，进行相同操作
    9、打印结果

    解题思路二:
    1、定义一个字典
    2、定义3个列表
    3、遍历列表，将所有数据分别保存到相应列表中
    4、将列表保存到字典中
'''

list_source = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]


# 方法一
dict1 = {}
for item in list_source:
    if item > 66:
        list1 = dict1.get("key>66", [])
        list1.append(item)
        dict1["key>66"] = list1
    elif item < 66:
        list2 = dict1.get("key<66", [])
        list2.append(item)
        dict1["key<66"] = list2
    else:
        list3 = dict1.get("key=66", [])
        list3.append(item)
        dict1["key=66"] = list3

print(dict1)

# 方法二
dict2={}
list1=[]
list2=[]
list3=[]
for i in list_source:
    if i>66:
        list1.append(i)
    elif i==66:
        list2.append(i)
    else:
        list3.append(i)
dict2["key>66"] = list1
dict2["key=66"] = list2
dict2["key<66"] = list3
print(dict2)


