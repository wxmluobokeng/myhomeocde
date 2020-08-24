#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/8/1 20:52
# @Author : 老萝卜
# @File : 继承的使用-times_1.py
# @Software: PyCharm Community Edition

class Animal:
    def run(self):
        print('动物会跑.......')
    def sleep(self):
        print('动物睡觉......')

a= Animal()
a.run()
# 动物会跑.......

class Dog:
    def run(self):
        print('狗会跑.......')
    def sleep(self):
        print('狗睡觉......')
    def speak(self):
        print("汪汪汪......")


class NewDog(Animal):
    def run(self):
        print('狗会跑.......')
    def sleep(self):
        print('狗睡觉......')
    def speak(self):
        print("汪汪汪......")


d=Dog()
print(d)
# <__main__.Dog object at 0x00000000025CB400>
d.run()
d.sleep()
d.speak()
# 狗会跑.......
# 狗睡觉......
# 汪汪汪......

r=isinstance(d,Dog)
print(r)    # True
r=isinstance(d,animal)
print(r)    # True



class Person():
    pass

# issubclass()  检测一个类是否是另一个类的子类

print(issubclass(Dog,Animal)) # True
print(issubclass(Dog,object)) # True
print(issubclass(Animal,object)) # True
print(issubclass(Person,object)) # True
print(issubclass(int,object)) # True