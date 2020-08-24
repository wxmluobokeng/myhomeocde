#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/12 16:38
# @Author : 老萝卜
# @File : 循环嵌套-times_2.py
# @Software: PyCharm Community Edition

# *****
# *****
# *****
# *****
# *****
i=0
while i<5:
    j=0
    while j<5:
        print("*",end="")
        j+=1
    print()
    i+=1

# *
# **
# ***
# ****
# *****
i=0
while i <5:
    i+=1
    j=0
    while j<i:
        print("*",end="")
        j+=1
    print()

# *****
# ****
# ***
# **
# *
i =0
while i<5:
    j=0
    while j<5-i:
        print("*",end="")
        j+=1
    print()
    i+=1