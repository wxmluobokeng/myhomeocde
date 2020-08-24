#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/21 21:41
# @Author : 老萝卜
# @File : 集合的运算-times_3.py
# @Software: PyCharm Community Edition

# & 交集运算
a = {1, 2, 3, 4}
b = {2, 3, 4, 5}
c = {7, 8, 9}
d = a & b  # {2, 3, 4}
e = a & c  # set()


# | 并集运算
a = {1, 2, 3, 4}
b = {2, 3, 4, 5}
c = {7, 8, 9}
d = a | b  # {1, 2, 3, 4, 5}
e = a | c  # {1, 2, 3, 4, 7, 8, 9}

print(d)
print(e)

# - 差集运算
a = {1, 2, 3, 4}
b = {2, 3, 4, 5}
c = {7, 8, 9}
d = a - b       # {1}
e = a - c       # {1, 2, 3, 4}

print(d)
print(e)

# ^  异或运算
a = {1, 2, 3, 4}
b = {2, 3, 4, 5}
c = {7, 8, 9}
d = a ^ b       # {1, 5}
e = a ^ c       # {1, 2, 3, 4, 7, 8, 9}


# <= 检查一个集合是否是另一个集合的子集
# < 检查一个集合是否是另一个集合的真子集
a = {1, 2, 3, 4}
b = {1, 2, 3, 4}
c = {1, 2, 3}
d = {4, 5, 6, 7}
e = {6, 7, 8}
g = a <= b          #  True
h = c <= a          #  True
i = e <= a          #  False

j = a < b          #  False
k = c < a          #  True
l = e < a          #  False


# >=检查一个集合是否是另一个集合的超集
# >检查一个集合是否是另一个集合的真超集
a = {1, 2, 3, 4}
b = {1, 2, 3, 4}
c = {1, 2, 3}
d = {4, 5, 6, 7}
e = {6, 7, 8}
g = a >= b          #  True
h = a >= c          #  True
i = e <= a          #  False

j = a < b          #  False
k = c < a          #  True
l = e < a          #  False

