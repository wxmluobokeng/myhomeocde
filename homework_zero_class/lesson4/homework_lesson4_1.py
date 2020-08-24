# -*- coding: utf-8 -*-
# @time :2020/7/10 17:42
# @Author:老萝卜
# @file:homework_
# @Software:%{PRODUICT_NAME}

'''
   lesson 4 课后作业：第二题 ：以4种格式化字符串的⽅式来实现 521 xxx 嫁给我好吗？
'''
girl = "老婆"
print("521 "+girl+" 嫁给我好吗？")

str_list = ["521","老婆","嫁给我好吗？"]
print(" ".join(str_list))

print("521",girl,"嫁给我好吗？")

print("521 %s 嫁给我好吗？"%girl)

print("521 {} 嫁给我好吗？".format(girl))

print(f"521 {girl} 嫁给我好吗？")