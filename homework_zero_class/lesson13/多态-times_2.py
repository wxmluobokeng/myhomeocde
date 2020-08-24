# -*- coding: utf-8 -*-
# @time :2020/8/3 15:28
# @Author:老萝卜
# @file:多态-times_2
# @Software:%{PRODUICT_NAME}

class A:
    def __init__(self,name):
        self._name = name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name

class B:
    def __init__(self, name):
        self._name = name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name

a = A('葫芦娃')
b = B('黑猫警长')

def speak(obj):
    print('你好%s'%obj.name)

speak(a)
speak(b)
# 你好葫芦娃
# 你好黑猫警长

class C:
    pass
c=C()
# speak(c)        # AttributeError: 'C' object has no attribute 'name'


def speak2(obj):
    if isinstance(obj,A):
        print('你好%s'%obj.name)

speak2(a)       # 你好葫芦娃
speak2(b)       #


lst=[1,2,3,4]
str="python"

print(len(lst))     # 4
print(len(str))     # 6
# print(len(a)) # TypeError: object of type 'A' has no len()

class A:
    def __init__(self,name):
        self._name = name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name
    def __len__(self):
        return 100

a=A("葫芦娃")
print(len(a))       # 100


