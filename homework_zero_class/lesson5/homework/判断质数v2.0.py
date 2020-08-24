#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/12 0:26
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
    else:
        pass

    num = int(str_num)

    list_num= []
    i = 2
    count = 0
    max_num = int(num ** 0.5)+1
    while i < max_num:
        # i+=1
        if num % i == 0:
            if i*i==num:
                list_num.append(i)
            else:
                list_num.append(i)
                list_num.append(num // i )
        i += 1
    if len(list_num) == 0:
        print(f" {str_num} 是质数")
    else:
        # list_num += [1,num]
        list_num.sort()
        print(f" {str_num} 不是质数，除了能被1和{str_num}整除外，还能被以下数整除：{'、'.join(str(i) for i in list_num)}")
