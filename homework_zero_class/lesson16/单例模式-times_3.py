#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/8/8 14:54
# @Author : 老萝卜
# @File : 单例模式-times_2.py
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

# # 1 谁创建了对象？
class Person:
    def __init__(self):
        print('初始化方法....')  # 未执行
p1 = Person()
print("p11=",p1)
# 初始化方法....
# p11= <__main__.Person object at 0x00000000025BA320>

class Person:
    def __new__(cls, *args, **kwargs):
        print(123)
    def __init__(self):
        print('初始化方法....')              # 未执行
p1 = Person()
print("p11=",p1)
# 123
# p11= None

class Person:
    sex = "男"
    def __init__(self):
        print('初始化方法....')  # 未执行
        self._name = "葫芦娃"
    def __new__(cls, *args, **kwargs):
        print(123)
    def sleep(self):
        print("人睡觉......")

p1 = Person()
print("p11=", p1)
# 123
# p11= None

# p1.sleep()            #  调用类实例方法时报错
# # Traceback (most recent call last):
# #   File "E:/python-course/homework_zero_class/lesson16/单例模式-times_3.py", line 56, in <module>
# #     p1.sleep()            #  调用类实例方法时报错
# # AttributeError: 'NoneType' object has no attribute 'sleep'
# print(p1.sex)         # 调用属性报错
# # Traceback (most recent call last):
# #   File "E:/python-course/homework_zero_class/lesson16/单例模式-times_3.py", line 61, in <module>
# #     print(p1.sex)
# # AttributeError: 'NoneType' object has no attribute 'sex'

# Person类的父类是object 继承object
# object有一个new方法来创建对象
# 创建对象之后，才可以执行 __init__(self),进行初始化

# 2. 对象的执行顺序

class Person:
    sex = "男"
    def __new__(cls, *args, **kwargs):
        print(123)
        obj = object.__new__(cls)  # 创建了一个对象,调用object的__new__方法创新类对象
        return obj
    def __init__(self):
        print('创建完对象之后再初始化....')
        self._name = "葫芦娃"
    def get_name(self):
        return self._name
    def sleep(self):
        print("人睡觉......")
p1 = Person()
print("p11=", p1)
p1.sleep()
print(p1.get_name())
print(p1.sex)
# 123
# 创建完对象之后再初始化....
# p11= <__main__.Person object at 0x000000000226A518>
# 人睡觉......
# 葫芦娃
# 男

# 3.创建单例模式
class Person:
    # 私有变量
    _instance = None
    def __new__(cls, *args, **kwargs):
        print(123)
        if Person._instance is None:
            obj = object.__new__(cls) # 创建了一个对象
            Person._instance = obj # 将这个对象赋值给类的私有变量_instance
        return Person._instance
    def __init__(self,name):
        print('创建完对象之后再初始化....')
        self._name = name
    @property
    def name(self):
        return self._name
    def sleep(self):
        print("人睡觉......")
    def print_cls(self):
        print("print_cls() 执行:",self,id(self),Person,id(Person))

print("-"*30,"p1 = Person('葫芦娃')","-"*30)
p1 = Person("葫芦娃")
print(p1)
print(p1.name)
print(id(p1))
p1.print_cls()
print("-"*30,'p2 = Person("绿巨人")',"-"*30)
p2 = Person("绿巨人")
print(p1,p2)
print(p1.name,p2.name)
print(id(p1),id(p2))
p2.print_cls()
print("-"*30,'p3 = Person("钢铁侠")',"-"*30)
p3 = Person("钢铁侠")
print(p1,p2,p3)
print(p1.name,p2.name,p3.name)
print(id(p1),id(p2),id(p3))
p3.print_cls()
# ------------------------------ p1 = Person('葫芦娃') ------------------------------
# 123
# 创建完对象之后再初始化....
# <__main__.Person object at 0x000000000258A780>
# 葫芦娃
# 39364480
# print_cls() 执行: <__main__.Person object at 0x000000000258A780> 39364480 <class '__main__.Person'> 37970680
# ------------------------------ p2 = Person("绿巨人") ------------------------------
# 123
# 创建完对象之后再初始化....
# <__main__.Person object at 0x000000000258A780> <__main__.Person object at 0x000000000258A780>
# 绿巨人 绿巨人
# 39364480 39364480
# print_cls() 执行: <__main__.Person object at 0x000000000258A780> 39364480 <class '__main__.Person'> 37970680
# ------------------------------ p3 = Person("钢铁侠") ------------------------------
# 123
# 创建完对象之后再初始化....
# <__main__.Person object at 0x000000000258A780> <__main__.Person object at 0x000000000258A780> <__main__.Person object at 0x000000000258A780>
# 钢铁侠 钢铁侠 钢铁侠
# 39364480 39364480 39364480
# print_cls() 执行: <__main__.Person object at 0x000000000258A780> 39364480 <class '__main__.Person'> 37970680