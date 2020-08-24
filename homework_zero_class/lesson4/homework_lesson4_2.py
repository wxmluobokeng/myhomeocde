# -*- coding: utf-8 -*-
# @time :2020/7/10 17:54
# @Author:老萝卜
# @file:homework_lesson4_2
# @Software:%{PRODUICT_NAME}

'''
   lesson 4 课后作业：第三题 ：现在有a b c三个变量，三个变量中分别保存有三个数值，请通过条件运算符获取三个值中的最大值
'''
print("请输入3个整数值比较大小")
a= int(input("请输入第一个比较大小整数值： "))
b = int(input("请输入第二个比较大小整数值： "))
c = int(input("请输入第三个比较大小整数值： "))

# 方法一：
d = a if a>b else b
max1 = d if d>c else c
d = a if a<b else b
min1 = d if d<c else c
print("{},{},{}中，最大数是：{}，最小数是：{}".format(a,b,c,max1,min1))

# 方法二
d = max(a,b)
max2= max(d,c)
d= min(a,b)
min2=min(d,c)
print("{},{},{}中，最大数是：{}，最小数是：{}".format(a,b,c,max2,min2))