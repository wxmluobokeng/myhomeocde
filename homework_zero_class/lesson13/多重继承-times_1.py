# -*- coding: utf-8 -*-
# @time :2020/8/3 14:16
# @Author:老萝卜
# @file:多重继承-times_1
# @Software:%{PRODUICT_NAME}多重继承-times_1.py

class A(object):
    def test(self):
        print("A......")

class B(object):
    def test(self):
        print("B......")

class C(B):
    pass

# __bases__ 可以获取当前类所有的父类
print(C.__bases__)
print(B.__bases__)
# (<class '__main__.B'>,)
# (<class 'object'>,)

# Python中是支持多重继承的，也就是我们可以为一个类同时指定多个父类
# 可以在类名后的()中添加多个类，实现多重继承
# 多重继承，会使子类同时拥有多个父类，并且会获取到所有父类的方法
class C(A,B):
    pass

print(C.__bases__)
# (<class '__main__.A'>, <class '__main__.B'>)


# 如果多个父类中有重名的方法，则会先去第一个父类中寻找，然后第二个，在然后第三个...

c= C()
c.test()
# A......
