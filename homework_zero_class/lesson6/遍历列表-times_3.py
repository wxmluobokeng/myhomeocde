#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/14 22:34
# @Author : 老萝卜
# @File : 遍历列表-times_3.py
# @Software: PyCharm Community Edition


# 遍历列表：指将列表中的元素取出来

hero = ['a','b','c','d']

print(hero[0])
print(hero[1])
print(hero[2])
print(hero[3])

# while循环取出
print("while循环取出:")
i = 0
while i < len(hero):
    print(hero[i])
    i += 1

# for循环来遍历列表
# for循环的代码块会执行多次，序列中有几个元素就会执行几次
# 每执行一次，就会将序列中的元素赋值给变量
# 语法
# for 变量 in 遍历的内容:
#      代码块


print("\n\nfor循环取出:")
for i in hero:
    print(i)
