#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/8/12 21:26
# @Author : 老萝卜
# @File : 1.py
# @Software: PyCharm Community Edition

# import random
# for i in range(10):
#     print(random.randint(1,2))


a=[lambda x:x+i for i in range(10)]
print(a[0](10))
for i  in range(10):

    print(a[i](10))


# class A:
#     x=1
# class B(A):
#     pass
# class C(A):
#     pass
#
# b=B()
# c=C()
# b.x=2
# A.x=3
# print(A.x,b.x,c.x)
#
#
# list1=[i**2 for i in range(10)]
# print(list1)
#
#
