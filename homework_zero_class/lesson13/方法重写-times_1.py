# -*- coding: utf-8 -*-
# @time :2020/8/3 12:55
# @Author:老萝卜
# @file:方法重写-times_1
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

# 如果子类中有和父类重名的方法。则通过子类去调用该方法时，
# 会调用的是子类里面的方法，这个特点我们称之为方法的重写(覆盖，override)

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

# 当我们调用一个对象的方法时：
#    会优先去当前对象中寻找是否具有该方法，如果有则直接调用
#    如果没有，则去当前对象的父类中寻找，如果父类中有则直接调用父类中的方法
#    如果没有，则去父类中的父类寻找，以此类推，直到找到object，如果依 然没有找到就报错了