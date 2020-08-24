#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/28 20:51
# @Author : 老萝卜
# @File : 类的简介-times_1.py
# @Software: PyCharm Community Edition


# 类class
# 类，简单理解相当于一张图纸，在程序中我们需要根据类来创建对象
# 如果多个对象是通过一个类创建的，我们就称这些对象是一类对象
# int() float() bool() str().....
# a = int(10) 等价于   a = 10 创建了一个int类的实例

a = 10
a = int(10)

# 语法
# class 类名([父类]):
#     pass

# 定义一个类
class MyClass():
    pass

print(MyClass)      #<class '__main__.MyClass'>
# 使用 MyClass来创建一个对象
mc = MyClass()      # mc就是通过MyClass创建的对象 mc是MyClass的实例
mc2 = MyClass()
mc3 = MyClass()
mc4 = MyClass()

print("mc:", mc, type(mc))
print("mc2:", mc2, type(mc2))
print("mc3:", mc3, type(mc3))
print("mc4:", mc4, type(mc4))
# mc: <__main__.MyClass object at 0x00000000023AB320> <class '__main__.MyClass'>
# mc2: <__main__.MyClass object at 0x00000000023AB3C8> <class '__main__.MyClass'>
# mc3: <__main__.MyClass object at 0x00000000023AB400> <class '__main__.MyClass'>
# mc4: <__main__.MyClass object at 0x00000000023AB438> <class '__main__.MyClass'>

# mc mc2 mc3 mc4 都是由MyClass这个类创建的对象， 它们都是一类对象

# isinstance() 用来检测一个对象是否是一个类的实例 返回值是布尔类型
r = isinstance(mc,MyClass)      # True
print(r)
r = isinstance(mc2,MyClass)     # True
print(r)
r = isinstance(mc3,MyClass)     # True
print(r)
r = isinstance(mc4,MyClass)     # True
print(r)

r = isinstance(mc3,int)         # False
print(r)




