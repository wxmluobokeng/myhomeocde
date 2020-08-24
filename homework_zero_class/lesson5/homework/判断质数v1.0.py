#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/11 23:26
# @Author : 老萝卜
# @File : 判断质数v1.0.py
# @Software: PyCharm Community Edition


while True:  # 循环输入，直到不想测试时，输入
    str_num = input("请输入您想要判断的数，q表示退出)： ").strip()
    if str_num == "q" or str_num == "Q":
        break
    elif not str_num.isnumeric():  # 输入不是数字
        print("数据输入有误，请重新输入！ ")
        continue
    elif str_num == "1":
        print("1是特殊自然数，即不质数，也不是合数,请重新输入！")
        continue
    # elif str_num=="2":
    #     print("2是质数")
    #     continue
    # elif str_num=="3":
    #     print("2是质数")
    #     continue
    else:
        pass

    num = int(str_num)

    i = 2
    count = 0
    max_num = num // 2 + 1
    while i < max_num:
        if num % i == 0:
            count = 1
            break
        i += 1
    if count == 0:
        print(f" {str_num} 是质数")
    else:
        print(f" {str_num} 不是质数")
