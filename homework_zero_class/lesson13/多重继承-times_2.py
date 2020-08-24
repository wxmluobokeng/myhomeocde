# -*- coding: utf-8 -*-
# @time :2020/8/3 14:36
# @Author:老萝卜
# @file:多重继承-times_2
# @Software:%{PRODUICT_NAME}多重继承-times_2.py

class A(object):
    def test(self):
        print("A......")

class B(object):
    def test(self):
        print("B......")

class C(B):
    pass


print(C.__bases__)
print(B.__bases__)
# (<class '__main__.B'>,)
# (<class 'object'>,)

class C(A,B):
    pass

print(C.__bases__)
# (<class '__main__.A'>, <class '__main__.B'>)


class C(B,A):
    pass

c= C()
c.test()
# B......
