#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/25 16:29
# @Author : 老萝卜
# @File : 闭包-times_1.py
# @Software: PyCharm Community Edition

# 高阶函数的特点
# 特点二 将函数作为返回值也是高阶函数
# 通过闭包可以创建一些只有当前函数能够访问的变量，将一些私有数据藏到闭包中

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


# 形成闭包的条件
# 1.函数嵌套
# 2.将内部函数作为返回值返回
# 3.内部函数必须使用到外部函数的变量
