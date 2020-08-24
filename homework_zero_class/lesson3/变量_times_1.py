# -*- coding: utf-8 -*-
# @time :2020/7/10 15:16
# @Author:老萝卜
# @file:变量_times1
# @Software:%{PRODUICT_NAME}

d1 = {'Python':'Java'}

import copy

d2 = copy.deepcopy(d1)

print(d1)
print(d2)

print(d1 == d2) # True 值是相当的

print(id(d1),id(d2)) # 不一样
