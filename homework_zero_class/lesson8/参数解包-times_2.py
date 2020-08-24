# -*- coding: utf-8 -*-
# @time :2020/7/22 15:26
# @Author:老萝卜
# @file:参数解包-times_2
# @Software:%{PRODUICT_NAME}

def fn3(a,b,c):
    print('a =',a)
    print('b =',b)
    print('c =',c)


t = (1,2,3)
fn3(t[0],t[1],t[2])
fn3(*t)

d = {'a':1,'b':2,'c':3}
fn3(**d)


