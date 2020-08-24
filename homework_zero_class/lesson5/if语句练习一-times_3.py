#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/12 15:12
# @Author : 老萝卜
# @File : if语句练习一-times_3.py.py
# @Software: PyCharm Community Edition


month_str=input("请输入月份").strip()
if not month_str.isnumeric():
    print("正确的月份是1-12的数字，您的输入是 %s"%month_str)
else:
    month= int(month_str)
    if month<1:
        print("月份不能为零或负数，您的输入是 %s"%month_str)
    elif month>12:
        print("月份不能大于12，您的输入是 %s" % month_str)
    elif 3<=month<=5:
        print(f"{month} 月是春季 ")
    elif 6 <= month <= 8:
        print(f"{month} 月是夏季 ")
    elif 9<=month<=11:
        print(f"{month} 月是秋季 ")
    else:
        print(f"{month} 月是冬季 ")


