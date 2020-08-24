# -*- coding: utf-8 -*-
# @time :2020/8/5 12:42
# @Author:老萝卜
# @file:列表推导式-times_1
# @Software:%{PRODUICT_NAME}

# 旧的列表 --> 新的列表
# 语法 1 [表达式 for 变量 in 旧列表] 2 [表达式 for 变量 in 旧列表 if 条件]

# 找到长度大于3的人名
lst = ['jerry', 'tony', 'tom', 'mok', 'abcd']

def fn(lst):
    new_lst = []
    for name in lst:
        if len(name) > 3:
            new_lst.append(name)
    return new_lst


r = fn(lst)
print(r)
# ['jerry', 'tony', 'abcd']

r = [name for name in lst if len(name) > 3]
print(r)
# ['jerry', 'tony', 'abcd']

r = [name.capitalize() for name in lst if len(name) > 3]
print(r)
# ['Jerry', 'Tony', 'Abcd']

# 1 - 100 能被3整除 放到一个新的列表
new_lst = [i for i in range(1, 100) if i % 3 == 0]
print(new_lst)
# [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]

new_lst = [i for i in range(1, 100) if i % 3 == 0 and i % 6 != 0]
print(new_lst)
# [3, 9, 15, 21, 27, 33, 39, 45, 51, 57, 63, 69, 75, 81, 87, 93, 99]
