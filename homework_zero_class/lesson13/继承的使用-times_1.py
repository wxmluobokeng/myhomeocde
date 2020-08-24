#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/8/1 20:52
# @Author : 老萝卜
# @File : 继承的使用-times_1.py
# @Software: PyCharm Community Edition

# 定义一个动物类(Animal) 定义两个方法 run() sleep()

class Animal:
    def run(self):
        print('动物会跑.......')
    def sleep(self):
        print('动物睡觉......')

a= Animal()
a.run()
# 动物会跑.......

# 定义一个狗类
# 思路是什么？
# 方案一 直接修改动物类，在这个类中添加我们需要的功能
# (修改起来比较麻烦，并且会违反ocp原则)
# 方案二 直接创建了一个新的类
# (创建一个新的类比较麻烦，会出现大量的重复性代码)

class Dog:
    def run(self):
        print('狗会跑.......')
    def sleep(self):
        print('狗睡觉......')
    def speak(self):
        print("汪汪汪......")

# 方案三 直接从Animal类中继承它的属性和方法

class NewDog(Animal):
    def run(self):
        print('狗会跑.......')
    def sleep(self):
        print('狗睡觉......')
    def speak(self):
        print("汪汪汪......")

# 继承是面向对象的三大特性之一
# 我们使用继承是可以获取到另一个类的属性和方法
# 在定义类的时候，我们可以在类名的括号中指定当前类的父类(超类，基类)

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


# 在创建类的时候，如果省略了父类，则默认父类是object
# object是所有类的父类，所有类都继承与object

class Person():
    pass

# issubclass()  检测一个类是否是另一个类的子类

print(issubclass(Dog,Animal)) # True
print(issubclass(Dog,object)) # True
print(issubclass(Animal,object)) # True
print(issubclass(Person,object)) # True
print(issubclass(int,object)) # True