# -*- coding: utf-8 -*-
# @time :2020/7/22 15:30
# @Author:老萝卜
# @file:参数解包-times_3
# @Software:%{PRODUICT_NAME}

def fn3(a,b):
    print('a =',a,'b =',b)


t = (1,2)
fn3(t[0],t[1])
fn3(*t)

s =[1,2]
fn3(*s)

# s= [1,2,3,4]
# fn3(*s)    #TypeError: fn3() takes 3 positional arguments but 4 were given


d = {'a':1,'b':2}
fn3(**d)
