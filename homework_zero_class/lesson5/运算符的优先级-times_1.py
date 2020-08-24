#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/12 17:52
# @Author : 老萝卜
# @File : 运算符的优先级-times_1.py
# @Software: PyCharm Community Edition

a = 2 + 3 * 4

b = 2 or 3 and 4
c = (2 or 3) and 4


# or和and 优先级一样高 从左往右运算 结果4
# or比and 优先级高 从左往右运算 结果4
# and比or 优先级高 结果是2
# 结论发下 and的优先级比 or的优先级高

print(b)
print(c)