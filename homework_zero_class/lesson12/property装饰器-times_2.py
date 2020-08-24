#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/30 23:32
# @Author : 老萝卜
# @File : property装饰器-times_2.py
# @Software: PyCharm Community Edition

import requests

class Person:
    def __init__(self,name):
        self._name = name
    def name(self):
        print("get方法执行了")
        return self._name
p=Person("葫芦娃")
print(p.name())
# get方法执行了
# 葫芦娃

# @property 将方法转换为相同名称的只读属性

class Person:
    def __init__(self,name):
        self._name = name
    @property
    def name(self):
        print("get方法执行了")
        return self._name
p=Person("葫芦娃")
# print(p.name()) # TypeError: 'str' object is not callable
print(p.name)
# get方法执行了
# 葫芦娃


r= requests.get("http://www.baidu.com")
# print(r.text)       # r.text是个方法,Response.text()


# @property 将方法转换为相同名称的只读属性
# 也可以紧跟着写set方法，中间不能插入其它代码

class Person:
    def __init__(self,name):
        self._name = name

    @property
    def name(self):
        return self._name
    def name(self,name):
        self._name=name
print("-"*8)
p=Person("葫芦娃")
print(p.name)
p.name="超人"
print(p.name)
# <bound method Person.name of <__main__.Person object at 0x0000000001DD9278>>
# 超人

p.name="老萝卜"
print(p.name)
# 老萝卜


# 这个是setter方法 setter方法的装饰器 @属性名.setter
class Person:
    def __init__(self,name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        self._name=name
print("-"*8)
p=Person("葫芦娃")
print(p.name)
p.name="超人"
print(p.name)
# 葫芦娃
# 超人



