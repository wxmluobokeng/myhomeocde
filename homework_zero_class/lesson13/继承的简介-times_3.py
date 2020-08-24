#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/8/1 22:37
# @Author : 老萝卜
# @File : 继承的简介-times_3.py
# @Software: PyCharm Community Edition

class Doctor:
    name = ''
    age = ''
    def scure(self):
        print('治病救人.....')

class Guy:
    name = ''
    age = ''

    def study(self):
        print('保卫国家.....')

# 上面两个类中，都有 name、age属性，能否把这些公共属性和方法放到一个类里，让他们发生点关系

d=Doctor()  #创建实例时，医生对象才具体化


class Person:
    name=""
    age=""

# 继承
# 1.让类与类之间产生了关系，有了这个关系看，才有了多态的特性
# 2.提高了代码的复用性
