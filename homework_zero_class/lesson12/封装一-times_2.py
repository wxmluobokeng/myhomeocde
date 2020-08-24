#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/30 19:37
# @Author : 老萝卜
# @File : 封装一-times_2.py
# @Software: PyCharm Community Edition

# 封装是什么？
# 封装是面向对象三大特性之一
# 封装指的是隐藏对象中一些不希望被外部访问到的属性或方法

class Dog:
    def __init__(self, name):
        self.name = name


d = Dog("大黑背")
print(d.name)
d.name = "二哈"


# 如何隐藏属性
# 将对象的属性名，修改成一个外部不知道的名字
# 如何获取(修改)对象中的属性
# 需要我们提供一个getter和setter方法访问属性和修改属性

class Dog:
    def __init__(self, name):
        self.hidden_name = name

    def speak(self):
        print('大家好，我是%s' % self.hidden_name)

    def get_name(self):
        # get_name()来获取对象的name属性
        return self.hidden_name

    def set_name(self, name):
        self.hidden_name = name


d = Dog("大黑背")
d.name = "二哈"
d.speak()
# 大家好，我是大黑背

d.hidden_name = "边抆"        # 还是可以强制修改，因为你知道的变量名称
d.speak()
# 大家好，我是边抆

print(d.get_name())
# 边抆

d.set_name("大狼青")
d.speak()
# 大家好，我是大狼青


# 使用封装，确实增加了类定义的复杂程度，但是它也确保了数据的安全
# 1.隐藏了属性名，使调用者无法随意修改对象的属性
# 2.增加了getter和setter方法，很好的控制了属性是否是只读的
# 如果希望属性只读，则可以直接去掉setter方法
# 如果希望属性不能被外部访问，则可以直接去掉getter方法
# 3.是用setter方法设置属性，可以增加数据的验证，确保数据的的值是正确的

class Dog:
    def __init__(self, name,age):
        self.hidden_name = name
        self.hidden_age = age

    def speak(self):
        print('大家好，我是%s' % self.hidden_name)

    def get_name(self):
        # get_name()来获取对象的name属性
        return self.hidden_name

    def set_name(self, name):
        self.hidden_name = name

    def get_age(self):
        # get_name()来获取对象的name属性
        return self.hidden_age

    def set_age(self, age):
        if age>0:
            self.hidden_age = age

d=Dog("大黑背",2)
d.set_age(-6)
print(d.get_age())
# 2





# 4.使用getter方法和setter方法获取和设置属性的时候，可以在读取属性和修改属性的时候做一些其他的操作

class Dog:
    def __init__(self, name,age):
        self.hidden_name = name
        self.hidden_age = age

    def speak(self):
        print('大家好，我是%s' % self.hidden_name)

    def get_name(self):
        # get_name()来获取对象的name属性
        return self.hidden_name

    def set_name(self, name):
        self.hidden_name = name

    def get_age(self):
        # get_name()来获取对象的name属性
        print("用户读取了属性")
        return self.hidden_age

    def set_age(self, age):
        print("用户修改了属性")
        if age>0:
            self.hidden_age = age

d=Dog("大黑背",2)
d.set_age(6)
print(d.get_age())
# 用户修改了属性
# 用户读取了属性
# 6