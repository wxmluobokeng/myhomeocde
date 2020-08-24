#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/11 20:45
# @Author : 老萝卜
# @File : 99乘法口决表-times_3.py.py
# @Software: PyCharm Community Edition

'''
    为了美观，每个式都占有的列数应该相同，但积为个位数或十位数，所以，积为个位数多加一个空格
    每个式子占 14 位， "1 * 1 = " 这占了8位，
    方法一：积再占一到两位，还需要补充五个或4个空格
    方法二：用占位符(%nd)固定下来位置
'''

# 方法一：
i = 0
while i < 9:
    i += 1
    # print(i)
    j = 0
    while j < i:
        j += 1
        print(f'{j} * {i} = {j*i}{" "*5 if j*i <10 else " "*4 }', end='')
    print()

print()

# 方法二
i = 0
while i < 9:
    i += 1
    # print(i)
    j = 0
    while j < i:
        j += 1
        print('%1d * %1d = %2d    '%(j,i,j*i), end='')
    print()


def fun1(* arg):
    return sum(arg),len(arg)

def fun2(tup):
    sum1,len1=tup
    return sum1/len1

print(fun2(fun1(1,2,3)))
