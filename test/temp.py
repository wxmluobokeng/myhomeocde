#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/7/9 21:52
# @Author : Jerry
# @File : temp.py
# @Software: PyCharm Community Edition
# 第一种：字符串拼接，如拼接url  url= "http://" + "www.baidu.com"
s = "hello"
print(s)
print("s = " + s)

# 第二种：参数传递
print("abc", 123)
print("s = ", s)

# 第三种：占位符
# %s 字符串占位      # %f 浮点数占位      # %d 整数占位
print("s = %s" % "hello")
print("s = %s" % s)
print("s = %s,s2 = %s" % (s, "world"))
print("Pi = %f" % 3.1415926)
print("R = %d" % 2)
print("%s S=Pi * R^2=%f * %d^2= %f" % ("圆的面积", 3.14, 2, 3.14 * 2 * 2))

# 第四种：格式化字符串  f+str({变量1},{变量2}......) 与 r+string 差不多
s1 = "光头强"
s2 = "熊大"
s3 = f"hello {s1},{s2}"
print("s3 = ", s3)

s4 = "hello {},{}".format(s1, s2)
s5 = "hello {1},{0}"
s6 = s4.format(s1,s2)
print("s4 = ", s4,"s6 = ",s6)
