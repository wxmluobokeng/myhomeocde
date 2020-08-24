#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/25 16:55
# @Author : 老萝卜
# @File : 闭包-times_2.py
# @Software: PyCharm Community Edition




def fn():
    # 在函数内部定义一个函数
    def fn2():
        print('我是fn2')

    # 将内部函数fn2作为返回值返回
    return fn2

print(fn())
r = fn()
print(r())


def fn():
    a=10
    # 在函数内部定义一个函数
    def fn2():
        print('我是fn2', a)

    # 将内部函数fn2作为返回值返回
    return fn2
print(fn())
r = fn()
print(r())



# 求平均数 是指在一组数据中所有数据之和再除以这组数据的个数
nums = [1,2,3,4,5,6]        # 3.5
print(sum(nums)/len(nums))


nums2 = []
# 定义一个函数来实现求平均数
def fn1(n):
    nums2.append(n)
    return sum(nums2)/len(nums2)

print(fn1(10))
print(fn1(30))
# num2.append("python")           # NameError: name 'num2' is not defined
num2=[]
print(fn1(40))   #  可能得不到想要的值


def make_fn():
    nums2=[]
    def fn1(n):
        nums2.append(n)
        return sum(nums2) / len(nums2)
    return fn1

m=make_fn()
print("make_fn:",m(10))
print("make_fn:",m(30))
nums2.append("python")
nums2=[]
print("make_fn:",m(40))



