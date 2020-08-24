#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/12 14:53
# @Author : 老萝卜
# @File : while语句练习-times_3.py
# @Software: PyCharm Community Edition

num = 0 #定义一个变量保存结果
i = 0
while i < 100:
    i += 1
    # 判断 i是偶数
    if i % 2 == 0:
        num += i
print("方法一：1+2+......+100=%d"%num)

#　获取100以内所有的偶数
i = 0
num = 0
while i < 100:
    i += 2
    num += i
print("方法二：1+2+......+100=%d"%num)

#　获取100以内所有的偶数
i = 0
num = 0
while i < 50:
    i += 1
    num += i*2
print("方法三：1+2+......+100=%d"%num)

