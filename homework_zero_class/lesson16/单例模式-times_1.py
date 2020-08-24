#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/8/8 13:54
# @Author : 老萝卜
# @File : 单例模式-times_1.py
# @Software: PyCharm Community Edition

# 单例模式是设计模式的一种
# 单例模式 保证系统中的一个类只有一个实例,

class Person:
    pass

p1 = Person()
p2 = Person()
print(p1)
print(p2)
# <__main__.Person object at 0x00000000021E97F0>
# <__main__.Person object at 0x000000000258E0F0>

# 1 谁创建了对象？
class Person:
    def __init__(self):
        print('初始化方法....')  # 未执行
p1 = Person()
print("p11=",p1)
# 初始化方法....

class Person:
    def __new__(cls, *args, **kwargs):
        print(123)
    def __init__(self):
        print('初始化方法....')              # 未执行
p1 = Person()
# 123


class Person:
    def __init__(self):
        print('初始化方法....')              # 未执行
    def __new__(cls, *args, **kwargs):
        print(123)
p1 = Person()
# 123

# object有一个new方法来创建对象
# 创建对象之后，才可以执行 __init__(self),进行初始化


# 2. 对象的执行顺序

class Person:
    def __new__(cls, *args, **kwargs):
        print(123)
        obj = object.__new__(cls) # 创建了一个对象
        return obj
    def __init__(self):
        print('创建完对象之后再初始化....')
p1 = Person()

# 3.
class Person:
    # 私有变量
    _instance = None
    def __new__(cls, *args, **kwargs):
        print(123)
        if Person._instance is None:
            obj = object.__new__(cls) # 创建了一个对象
            Person._instance = obj # 将这个对象赋值给类的私有变量_instance
        return Person._instance
    def __init__(self):
        print('创建完对象之后再初始化....')
p1 = Person()
p2 = Person()
p3 = Person()
print(id(p1),id(p2),id(p3))
# 123
# 123
# 123
# 创建完对象之后再初始化....
# 123
# 创建完对象之后再初始化....
# 123
# 创建完对象之后再初始化....
# 123
# 创建完对象之后再初始化....
# 39626232 39626232 39626232