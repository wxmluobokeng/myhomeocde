#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/7/11 18:24
# @Author : Jerry
# @File : 2.py
# @Software: PyCharm Comnity Edition

print("请输入待比较大小的三个整数")
a = int(input("请输入第一个整数： "))
b = int(input("请输入第二个整数： "))
c = int(input("请输入第三个整数： "))

# 方法一：表件表达式（1）
m1 = a if a > b  else b
max1 = m if m1 > c else c
m2 = a if a < b else b
min1 = m if m2 < c else c
print(f"方法一：{a}、{b}、{c}中，最大的是{max1},最小的是{min1}")

# 方法二：表件表达式（2）
max2 = a if a > b and a > c else b if b > c else c
min2 = a if a < b and a < c else b if b < c else c
print(f"方法二：{a}、{b}、{c}中，最大的是{max2},最小的是{min2}")

# 方法三：if语句
if a > b:
    m1 = a
    m2 = b
else:
    m1 = b
    m2 = a
if m1 > c:
    max3 = m1
else:
    max3 = c
if m2 < c:
    min3 = m2
else:
    min3 = c
print(f"方法三：{a}、{b}、{c}中，最大的是{max3},最小的是{min3}")

# 方法四：系统函数max() 、 min()
max4 = max(max(a, b), c)
min4 = min(min(a, b), c)
print(f"方法三：{a}、{b}、{c}中，最大的是{max3},最小的是{min3}")