#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/12 16:00
# @Author : 老萝卜
# @File : if语句练习二-times_3.py
# @Software: PyCharm Community Edition


dog_age = float(input('请输入狗的年龄:'))

if dog_age<=0:
    print("您的狗还没出生呢，无法估算")
elif dog_age>18:
    print("您的狗品种太优良了，此程序无法正确估算")
elif dog_age<=2:
    print(f"您{dog_age}岁的狗相当于人类{dog_age*10.5}岁")
else:
    print(f"您{dog_age}岁的狗相当于人类{2*10.5+(dog_age-2)*4}岁")
