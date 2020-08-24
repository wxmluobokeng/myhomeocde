# -*- coding: utf-8 -*-
# @time :2020/8/3 13:17
# @Author:老萝卜
# @file:super()-times_1
# @Software:%{PRODUICT_NAME}

class Animal:
    def __init__(self,name):
        self._name=name
    def run(self):
        print('动物会跑.......')
    def sleep(self):
        print('动物睡觉......')
    @property
    def name(self):
        return  self._name

    @name.setter
    def name(self,name):
        self._name=name

class Dog(Animal):
    def run(self):
        print('狗会跑.......')
    def sleep(self):
        print('我会看家......')

# d=Dog()         # TypeError: __init__() missing 1 required positional argument: 'name'
d=Dog("藏獒")
d.name="大狼狗"
print(d.name)


class Animal:
    def __init__(self,name):
        self._name=name
    def run(self):
        print('动物会跑.......')
    def sleep(self):
        print('动物睡觉......')
    @property
    def name(self):
        return  self._name
    @name.setter
    def name(self,name):
        self._name=name

class Dog(Animal):
    def __init__(self,name,age):
        self._name=name
        self._age=age
    def run(self):
        print('狗会跑.......')
    def sleep(self):
        print('我会看家......')
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, age):
        self._age = age


# d=Dog()         # TypeError: __init__() missing 1 required positional argument: 'name'
d=Dog("藏獒",5)
d.name="大狼狗"
print(d.name,d.age)
# 大狼狗 5

class Dog(Animal):
    # 希望可以直接调用父类的__init__方法来初始化父类中定义的属性
    def __init__(self,name,age):
        # self._name = name
        Animal.__init__(self,name)
        self._age=age

    def run(self):
        print('狗会跑.......')
    def sleep(self):
        print('我会看家......')
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, age):
        self._age = age
d=Dog("藏獒",5)
d.name="大狼狗"
print(d.name,d.age)
# 大狼狗 5

class Dog(Animal):
    # 希望可以直接调用父类的__init__方法来初始化父类中定义的属性
    # super() 可以用来获取当前类的父类 通过super()调用父类方法时，不需要传递self
    def __init__(self,name,age):
        # self._name = name
        # Animal.__init__(self,name)
        super().__init__(name)
        self._age=age
    def run(self):
        print('狗会跑.......')
    def sleep(self):
        print('我会看家......')
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, age):
        self._age = age

d=Dog("藏獒",5)
d.name="大狼狗"
print(d.name,d.age)
# 大狼狗 5