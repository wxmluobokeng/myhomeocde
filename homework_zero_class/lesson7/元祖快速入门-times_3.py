#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/18 19:40
# @Author : 老萝卜
# @File : 元祖快速入门-times_1.py
# @Software: PyCharm Community Edition

# 元祖 tuple
# 元祖是一个不可变序列
# 一般情况下我不希望这个数据改变的时候就用元祖，其余情况都用列表

# [] 列表
# () 元组

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

# 元祖的解包
# 元组解包指将元组当中的每一个元素都赋值给一个变量
a,b,c,d = my_tuple
print('a =',a)
print('b =',b)
print('c =',c)
print('d =',d)
# a,b = my_tuple # ValueError: too many values to unpack (expected 2)

# 在对一个元祖解包的时候，变量的数量要和元祖中元素的数量保持一致
# 如果变量和元素不一致，也可以在变量前面加上一个 *。这样会获取元祖中剩余的元素
# 以列表形式返回

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

