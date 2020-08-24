# -*- coding: utf-8 -*-
# @time :2020/8/3 14:48
# @Author:老萝卜
# @file:多态-times_1
# @Software:%{PRODUICT_NAME}

# 多态是面向对象三大特性之一 一个对象可以以不同的形态去呈现
# 多种形态 狗

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


# 在speak2()我们做了一个类型检查，也就是只有obj是A类型的对象，才可以使用
# 其他类型的对象，无法使用该函数，所以这个函数违反了多态
# 违反了多态的函数，只适用于一种类型的对象，无法处理其他类型的对象。这样导致这个函数的适用性很差
def speak2(obj):
    if isinstance(obj,A):
        print('你好%s'%obj.name)

speak2(a)       # 你好葫芦娃
speak2(b)       #


# len()
# 也就是对象中有个这个__len__特殊方法就可以使用len()函数来获取长度

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


'''
面向对象三大特性
封装 确保对象中的数据安全
继承 保证了对象的可拓展性
多态 保证了程序的灵活性
'''