#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/28 21:45
# @Author : 老萝卜
# @File : 类的说明-times_2.py
# @Software: PyCharm Community Edition

# 类也是一个对象
# 类就是一个用来创建对象的对象
# 类是type类型的对象，定义类实际上就是定义了一个type类型的对象

# 现在通过MyClass创建的对象都是一个空对象
# 可以向对象中添加变量，对象中的变量称为属性
# 语法 对象.属性名 = 属性值
# 调用方法 对象.方法名()
# 类的定义
# 对现实生活中事物的抽象
# 实际上所有的事物都是由两部分组成
# 1.数据(属性)
# 2.行为(方法)

# 类对象和实例对象都可以保存属性/方法
# 如果这个属性/方法是所有实例共享的，则应该将其保存到类对象当中
# 如果这个属性/方法是某个实例独有的，则应该保存到实例对象当中
# 一般情况下属性都保存到实例对象中
# 方法一般都保存到类对象中


class MyClass():
    pass

mc = MyClass()
mc2 = MyClass()
mc.name = '葫芦娃'

print(id(MyClass),type(MyClass))    # 38099768 <class 'type'>
print(mc.name)            # 葫芦娃
# print(mc2.name)           # AttributeError: 'MyClass' object has no attribute 'name'
mc2.name = '钢铁侠'
print(mc2.name)           # 钢铁侠

# 定义一个人类
class Person:
    name = '葫芦娃'

    def speak(a):
        print('同学们好！！！')



# 创建Person的实例
p1 = Person()
p2 = Person()

p1.name = '钢铁侠'

print(p2.name)
# p2.speak() # TypeError: speak() takes 0 positional arguments but 1 was given


