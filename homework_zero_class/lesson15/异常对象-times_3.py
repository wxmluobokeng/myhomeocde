#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/8/6 23:47
# @Author : 老萝卜
# @File : 异常对象-times_3.py
# @Software: PyCharm Community Edition

print('异常出现前')
try:
    print(6/0)
except:
    print("处理异常逻辑......")
print('异常出现后')
# 异常出现前
# 处理异常逻辑......
# 异常出现后


print('异常出现前')
try:
    print(abc)
    print(6/0)
except:
    print("处理异常逻辑......")
print('异常出现后')
# 异常出现前
# 处理异常逻辑......
# 异常出现后


print('异常出现前')
try:
    print(abc)
    print(6/0)
except NameError:
    # 如果except后面不跟任何的内容，则此时它会捕获所有的内容
    # 如果except后面跟着一个异常类型，它只会捕获 该类型的异常
    print("出现 NameError ......")
except ZeroDivisionError:
    print("出现 ZeroDivisionError ......")
print('异常出现后')
# 异常出现前
# 出现 NameError ......
# 异常出现后

print('异常出现前')
try:
    # print(abc)
    print(6/0)
except Exception as e:
    print("出现异常了.",e)
print('异常出现后')
# 异常出现前
# 出现异常了. division by zero
# 异常出现后

print('异常出现前')
try:
    print(abc)
    print(6/0)
except Exception as e:
    print("出现异常了.",e,type(e))
print('异常出现后')
# 异常出现前
# 出现异常了. name 'abc' is not defined <class 'NameError'>
# 异常出现后


print('异常出现前')
try:
    print(6/2)
except Exception as e:
    print("出现异常了.",e,type(e))
finally:
    print("无论是否出现异常，哥们都执行")
print('异常出现后')
# 异常出现前
# 3.0
# 无论是否出现异常，哥们都执行
# 异常出现后


print('异常出现前')
try:
    print(6/0)
except Exception as e:
    print("出现异常了.",e,type(e))
finally:
    print("无论是否出现异常，哥们都执行")
print('异常出现后')
# 异常出现前
# 出现异常了. division by zero <class 'ZeroDivisionError'>
# 无论是否出现异常，哥们都执行
# 异常出现后



# try:
#  	代码块(可能出现错误的语句)
# except 异常类型 as 异常名
# 	代码块(出现错误以后的处理方式)
# except 异常类型 as 异常名:
#     代码块(出现错误以后的处理方式)
# except 异常类型 as 异常名:
#     代码块(出现错误以后的处理方式)
# ......
# else:
#     代码块(没出错时要执行的语句)
# finally:
#     代码块(是否出错该代码块都会执行)
