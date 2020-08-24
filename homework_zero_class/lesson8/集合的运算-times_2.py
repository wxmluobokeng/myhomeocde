#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/21 21:39
# @Author : 老萝卜
# @File : 集合的运算-times_2.py
# @Software: PyCharm Community Edition

# & 交集运算
s1 = {1,2,3,4,5}
s2 = {3,4,5,6,7}

result = s1 & s2  # {3,4,5}


# | 并集运算
result = s1 | s2  # {1, 2, 3, 4, 5, 6, 7}

# - 差集运算
result = s1 - s2 # {1, 2}
result = s2 - s1 # {6, 7}


# ^  异或集
result = s1 ^ s2  # {1, 2, 6, 7}
print(s1,s2,result)

# <= 检查一个集合是否是另一个集合的子集
# < 检查一个集合是否是另一个集合的真子集
# a = {1,2,3,4,5}
a = {1,2,3}

b = {1,2,3,4,5}

result =a <= b
print(result)

result =a < b
print(result)

# >=检查一个集合是否是另一个集合的超集
# >检查一个集合是否是另一个集合的真超集

a = {1,2,3}

b = {1,2,3,4,5}
result =b >= a
print(result)

result =b > a
print(result)
