# -*- coding: utf-8 -*-
# @time :2020/7/10 16:50
# @Author:老萝卜
# @file:homework_lesson3
# @Software:%{PRODUICT_NAME}

'''
   lesson 3 课后作业：第二题 ：a,b = 6, 8 我想让a=8 b=6我该怎么办？⽤2种⽅式实现
'''
# 方法一： 通过中间变量将数值互换
a, b = 6, 8
print("原始数值：a,b=%d,%d" % (a, b))

c = a
a = b
b = c

print("转换后数值：a,b=%d,%d" % (a, b))

print("-" * 40, "分割线", "-" * 40)
# 方法二： 直接将输出位置换一下,可以有3种不同的显示方式
a, b = 6, 8
print("原始数值显示：a,b=%d,%d" % (a, b))
print("转换显示1：a,b=%d,%d" % (b, a))
print("转换显示2：a,b={},{}".format(b, a))
print("转换显示3：a,b={1},{0}".format(a, b))


# 方法三
a,b= b,a
print(a,b)