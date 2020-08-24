#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/21 23:14
# @Author : 老萝卜
# @File : 可变对象-times_3.py
# @Software: PyCharm Community Edition

# 可变对象
# 每个对象当中都保存了3个数据 id(标识) type(类型) value(值)


# 列表是一个可变对象
# a = [1,2,3]
# 指向的对象
# a[0] = 10 (改对象 改对象里面的值)
# 这个操作时通过变量来修改对象里面的值
# 这个操作不会改变变量指向的对象

# a = [4,5,6] (改变量)
# 这个操作是在给变量重新赋值
# 这个操作会改变变量


a = [1,2,3]
b = a
print("修改前：a=",a,type(a),id(a))
print("修改前：b=",b,type(b),id(b))
# 通过索引来修改列表
a[0] = 8
print("修改后：a=",a,type(a),id(a))
print("修改后：b=",b,type(b),id(b))
# 为变量重新赋值
a = (4,5,6)
print("修改后：a=",a,type(a),id(a))
print("修改后：b=",b,type(b),id(b))


# 定义列表a ,将变量a 赋值给 变量b
# 修改前：a= [1, 2, 3] <class 'list'> 39476744
# 修改前：b= [1, 2, 3] <class 'list'> 39476744
# 修改变量 a[0] =8  ,变量a b id未变，仅列表[0]=8
# 修改后：a= [8, 2, 3] <class 'list'> 39476744
# 修改后：b= [8, 2, 3] <class 'list'> 39476744
# 变量a 重新被赋值 [4,5,6]，则 a id、type 和 value都发生改变，但变量b id、type 和 value 未变
# 修改后：a= (4, 5, 6) <class 'tuple'> 39171344
# 修改后：b= [8, 2, 3] <class 'list'> 39476744