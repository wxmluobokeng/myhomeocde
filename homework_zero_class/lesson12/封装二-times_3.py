封装二-times_2.py#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/30 21:34
# @Author : 老萝卜
# @File : 封装二-times_3.py
# @Software: PyCharm Community Edition

class Person:
    def __init__(self,name):
        self.hidden_name = name
    def get_name(self):
        return self.hidden_name
    def set_name(self,name):
        self.hidden_name = name

p = Person('葫芦娃')
p.set_name('钢铁侠')
print(p.get_name())
p.hidden_name = '超人'
print(p.get_name())
# 钢铁侠
# 超人




# 可以对对象的属性使用双下划线开头
# 双下划线的属性是对象的隐藏属性，隐藏属性只能在类的内部访问，无法通过对象访问
class Person:
    def __init__(self,name):
        self.__name = name
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name = name

p = Person('葫芦娃')
print(p.get_name())
# 葫芦娃
# print(p.__name)         #AttributeError: 'Person' object has no attribute '__name'
p.__name = '苍老师'
print(p.get_name())
# 葫芦娃



# 其实隐藏属性只不过是Python自动为属性修改了一个名字
# 实际上将改的名字改为了 _类名__属性名 例如 __name -> _Person__name

print(p._Person__name)
p._Person__name = '苍老师'                 # 仍然可以修改，用正确的属性名修改
print(p.get_name())
# 葫芦娃
# 苍老师


# 一般我们会将一些私有的属性(不希望被外部访问) 以_开头，表示属性被封装，不建议直接引用和修改
class Person:
    def __init__(self,name):
        self._name = name
    def get_name(self):
        return self._name
    def set_name(self,name):
        self._name = name

p = Person('葫芦娃')
print(p._name)
p._name="超人"
print(p.get_name())
# 葫芦娃
# 超人