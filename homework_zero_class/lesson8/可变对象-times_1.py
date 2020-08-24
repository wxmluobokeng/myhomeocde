#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/21 22:43
# @Author : 老萝卜
# @File : 可变对象-times_1.py
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
print("修改前：a=",a,type(a),id(a))
# 通过索引来修改列表
a[0] = 8
print("修改后：a=",a,type(a),id(a))
# 为变量重新赋值
a = [4,5,6]
print("修改后：a=",a,type(a),id(a))

# 修改前：a= [1, 2, 3] <class 'list'> 39673352
# 修改后：a= [8, 2, 3] <class 'list'> 39673352
# 修改后：a= [4, 5, 6] <class 'list'> 39672968


a = [1,2,3]
b= a
print("变化前：a=",a,type(a),id(a))
print("变化前：b=",b,type(b),id(b))
a[0]=8
print("修改后：a=",a,type(a),id(a))
print("修改后：b=",b,type(b),id(b))

b = [20,2,3]
print("变化后：b=",b,type(b),id(b))
print("变化后：b=",b,type(b),id(b))

# 变化前：a= [1, 2, 3] <class 'list'> 39214600
# 变化前：b= [1, 2, 3] <class 'list'> 39214600
# 修改后：a= [8, 2, 3] <class 'list'> 39214600
# 修改后：b= [8, 2, 3] <class 'list'> 39214600
# 变化后：b= [20, 2, 3] <class 'list'> 39214216
# 变化后：b= [20, 2, 3] <class 'list'> 39214216