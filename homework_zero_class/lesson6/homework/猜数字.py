#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/13 22:45
# @Author : 老萝卜
# @File : 猜数字.py
# @Software: PyCharm Community Edition

import random

'''
    给⽤户9次机会猜1 - 10 个数字随机来猜数字。如果随机的数字和⽤户输⼊的数字⼀致则表示正确，如果不⼀致则表示错误。最终结果要求⽤户怎么也猜不对
'''
list1=["1","2","3","4","5","6","7","8","9","10"]

print("从1-10中随机抽取一个数字，给你9次机会猜，如果猜中，会恭喜你，如果没猜中，可以继续猜，直到9次机会用完，会公布正确答案")
i=1
while i<10:
    num_str=input(f"请输入第{i}次猜的数字： ")
    if len(num_str)!=1 and num_str!="10":
        print("一次只能输入1-10的数字，本次请重新输入")
        continue
    elif num_str=="q" or num_str=="Q":
        break
    elif num_str==10 or num_str in "123456789":
        if num_str in list1:
            list1.remove(num_str)
        if i==9:
            print(f"你猜错了，9次机会用完了，正确答案是{list1[0]}")
        else:
            print(f"对不起，猜错了，你还有{9-i}次机会")
    else:
        print("一次只能输入1-10的数字，请勿作弊，本次重新输入")
        continue

    i+=1



# 方法二：
lst = [] # 保存用户猜过的数字
for i in range(9):
    number = int(input('请输入一个数字:'))
    lst.append(number)
    print('对不起，没有猜对！')
while True:
    number_x = random.randint(1,10)  #  random.randint(1,10) 1 <= number_x <= 10
    # 判断
    if number_x in lst:
        continue
    else:
        break
print('正确号码:',number_x)

