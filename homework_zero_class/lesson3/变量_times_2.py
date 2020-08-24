# -*- coding: utf-8 -*-
# @time :2020/7/10 15:18
# @Author:老萝卜
# @file:变量_times_2
# @Software:%{PRODUICT_NAME}

import copy

dict1 = {"python","java"}
dict2 = copy.deepcopy(dict1)

print("dict1 = ",dict1)
print("dict2 = ",dict2)

print("判断dict1是否等于dict2 : ",dict1==dict2)
print("判断dict1是否是dict2 : ",id(dict1)==id(dict2))
print("dict1的id = ",id(dict1))
print("dict2的id = ",id(dict2))
