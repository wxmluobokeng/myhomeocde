# -*- coding: utf-8 -*-
# @time :2020/8/3 12:45
# @Author:老萝卜
# @file:方法重写-times_2
# @Software:%{PRODUICT_NAME}

class Animal:
    def run(self):
        print('动物会跑.......')
    def sleep(self):
        print('动物睡觉......')

class Dog(Animal):
    def run(self):
        print('狗会跑.......')
    def speak(self):
        print('我会看家....')

d = Dog()
d.run()
# 狗会跑.......


class A(object):
    def test(self):
        print('A.........')

class B(A):
    pass

class C(B):
    pass

c = C()
c.test()
# A.........

class A(object):
    def test(self):
        print('A.........')

class B(A):
    def test(self):
        print('B.........')

class C(B):
    pass

c = C()
c.test()
# B.........

class A(object):
    def test(self):
        print('A.........')

class B(A):
    def test(self):
        print('B.........')

class C(B):
    def test(self):
        print('C.........')

c = C()
c.test()
# c.speak()               # AttributeError: 'C' object has no attribute 'speak'
# C.........