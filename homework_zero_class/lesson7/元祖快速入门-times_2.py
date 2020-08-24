#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/18 19:25
# @Author : 老萝卜
# @File : 元祖快速入门-times_1.py
# @Software: PyCharm Community Edition


tup= ()
print(tup,type(tup))
my_tuple = (1,2,3,4,5)
print(my_tuple,type(my_tuple))
# my_tuple[3] = 8 # TypeError: 'tuple' object does not support item assignment

print(my_tuple[3])   # 4

tup = (10 )
print(tup,type(tup))
tup = (10,)
print(tup,type(tup))
# 如果元祖不是空元祖，它里面至少得有一个 ,
my_tuple = 10,20,30,40

print(my_tuple, type(my_tuple))


a,b,c,d = my_tuple
print('a =',a)
print('b =',b)
print('c =',c)
print('d =',d)
# a,b = my_tuple # ValueError: too many values to unpack (expected 2)

a,b,*c = my_tuple
print('a =',a)
print('b =',b)
print('c =',c)

# a = 10
# b = 20
# c = [30, 40]


a,*b,c = my_tuple
print('a =',a)
print('b =',b)
print('c =',c)

# a = 10
# b = [20, 30]
# c = 40

# *a,*b,c = my_tuple                # SyntaxError: two starred expressions in assignment

*a,b,c = my_tuple
print('a =',a)
print('b =',b)
print('c =',c)

# a = [10, 20]
# b = 30
# c = 40

a,b,*c = 'hello python'

print('a =',a)
print('b =',b)
print('c =',c)

# a = h
# b = e
# c = ['l', 'l', 'o', ' ', 'p', 'y', 't', 'h', 'o', 'n']


