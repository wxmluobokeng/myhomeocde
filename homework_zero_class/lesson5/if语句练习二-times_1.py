#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/12 15:42
# @Author : 老萝卜
# @File : if语句练习二-times_1.py
# @Software: PyCharm Community Edition

# 5岁的狗相当于人的多大的年龄呢？
# 狗的前两年每一年相当于人类的是10.5岁 ，然后每增加一年增加四岁
# 5岁的狗相当于人的年龄 10.5+10.5+4+4+4 = 33

# 编写一个程序，获取用户输入狗的年龄 然后通过程序显示其相当于人的年龄
# 如果用户输入的是负数，请提示输入有误

# 获取狗的年龄
dog_age = float(input('请输入狗的年龄:'))
person_age = 0
# 检查用户输入年龄的合法性
if dog_age <= 0:
    print('您输入的年龄有误！！！')
# 先计算狗的年龄在2岁以下(包含2岁)
elif dog_age <= 2:
    person_age = dog_age * 10.5
# 计算2岁以上的年龄
else:
    # 先计算前2年相当于人的年龄
    person_age = 2 * 10.5
    # 计算超过两岁的部分
    person_age += (dog_age - 2) * 4

if dog_age > 0:
    print(dog_age,'岁的狗，年纪相当于',person_age,'岁的人')



# 获取狗的年龄
dog_age = float(input('请输入狗的年龄:'))
person_age = 0
# 检查用户输入年龄的合法性
if dog_age > 0:
    if dog_age <= 2:
        person_age = dog_age * 10.5
    else:
        person_age = 2 * 10.5
        person_age += (dog_age - 2) * 4
    print(dog_age,'岁的狗，年纪相当于',person_age,'岁的人')
else:
    print('您输入的不合法')



