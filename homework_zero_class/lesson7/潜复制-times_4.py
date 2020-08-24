#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/21 1:14
# @Author : 老萝卜
# @File : 潜复制-times_4.py
# @Software: PyCharm Community Edition


'''
测试思路：
定义变量a 为 列表, a[0] = 字典，a[1] = 列表  a[2]= 字符串 ，a[3]= int  ,a[4] = 元组
将变量a 潜复制给变量  b 、  c
分别打印 变量 a 、 b  、 c   的值
分别打印 变量 a 、 b  、 c   的 id 值
分别打印 变量 a 、 b  、 c   序号0 -4 的 id 值

改变  序号0 的值 ：给字典增加一个key-value
改变  变量c[1] 列表  为 元组
将 a[1] 赋值 给  b[1]           #  值和id 均未改变
将 a[1] * 2 赋值 给  a[1]       #  id 未改变，所有相同id 值都相同
但将  a[1] * 2 赋值 给  a[1]    #  仅 b[1]  id  改变,  a[1]  id 不变 , 值也不同
将 b[2] 改变 ,仅 b[2] id 和 值 发生改变           # 正常 ，不可变对象赋 值 会改变id


'''


a =[ {"key1":[1,2,3,4]},[100,200],"python",20,(4,5,6)]
b = a.copy()
c= b.copy()
print("-----------------变化前-----------------")
print("a=",a)
print("b=",b)
print("c=",c)

print("id(a)=",id(a))
print("id(b)=",id(b))
print("id(c)=",id(c))

print("id(a[0])=",id(a[0]),"id(a[1])=",id(a[1]),"id(a[2])=",id(a[2]),"id(a[3])=",id(a[3]))
print("id(b[0])=",id(b[0]),"id(b[1])=",id(b[1]),"id(b[2])=",id(b[2]),"id(b[3])=",id(b[3]))
print("id(c[0])=",id(c[0]),"id(c[1])=",id(c[1]),"id(c[2])=",id(c[2]),"id(c[3])=",id(c[3]))

b[0]["key2"]="新增的key_value"    # 对变量b[0] 增加一个key_value
c[1]=(500,800)                    # 将变量c[1]换成一个元组
a[1]*=2                           # 将变量a[1]自身复制一次,id 和值都不变
b[1]= a[1]                        # 将变量[1]赋值给 b[1] ,id 和值都不变
b[1]= a[1]*2                      # 将变量[1]赋值给 b[1] ,变量b[1]的id 和值都变了
b[2]="java"                       # id 和值都变了

print("-----------------变化后-----------------")
print("a=",a)
print("b=",b)
print("c=",c)

print("id(a)=",id(a))
print("id(b)=",id(b))
print("id(c)=",id(c))

print("id(a[0])=",id(a[0]),"id(a[1])=",id(a[1]),"id(a[2])=",id(a[2]),"id(a[3])=",id(a[3]))
print("id(b[0])=",id(b[0]),"id(b[1])=",id(b[1]),"id(b[2])=",id(b[2]),"id(b[3])=",id(b[3]))
print("id(c[0])=",id(c[0]),"id(c[1])=",id(c[1]),"id(c[2])=",id(c[2]),"id(c[3])=",id(c[3]))




#  测试  a*2=a  和  b =a*2  的区别，不清楚为什么
a =[1,2,3]
b =a
c =b
c=2*b

print(a,b,c)


a = [1,2,3]
b= a
c=b
d=c
a*=2
b=a*2

print(a)
print(b)
print(c)
print(d)
