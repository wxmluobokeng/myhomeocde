#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/14 22:04
# @Author : 老萝卜
# @File : range()函数-times_1.py
# @Software: PyCharm Community Edition

# 函数 range(开始，结束，步长)
# 开始:默认是从0开始,0可以省略,例如 range(5) 等价于 range(0, 5)
# 结束:不包括结束,例如 range(0,5)   [0, 1, 2, 3, 4]
# 步长 默认为1 可以省略 例如 range(5) 等价于range(0, 5) 等价于 range(0, 5,1)

for i in range(5):
    print(i)

# 获取奇数
lst = [1,2,3,4,5,6,7,8,9]

print(list(range(0,9,2)))        # [0, 2, 4, 6, 8]

for i in range(0,9,2):

    print(lst[i])
