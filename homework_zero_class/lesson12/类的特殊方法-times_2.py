# -*- coding: utf-8 -*-
# @time :2020/7/30 15:10
# @Author:老萝卜
# @file:类的特殊方法-times_2
# @Software:%{PRODUICT_NAME}


class Person:
    name = '葫芦娃'

    def speak(self):
        print('大家好，我是%s' % self.name)


p1 = Person()
p2 = Person()
p1.speak()
p2.speak()


# 大家好，我是葫芦娃
# 大家好，我是葫芦娃

class Person:
    def speak(self):
        print('大家好，我是%s' % self.name)


p1 = Person()
# p1.speak()          # AttributeError: 'Person' object has no attribute 'name'
p1.name = "葫芦娃"
p1.speak()  # 现在调用成功了
p2 = Person()
# p2.speak()  # P2调用失败，没有定义name
# 大家好，我是葫芦娃

class Person:
    # name = '葫芦娃'
    def __init__(self, name):
        print('init方法执行了')
        self.name = name


    def speak(self):
        print('大家好，我是%s' % self.name)


p1 = Person('abc')
# p1.__init__()               # TypeError: __init__() missing 1 required positional argument: 'name'
p1.speak()
# init方法执行了
# 大家好，我是abc

class Person:
    print('Person代码中的代码')
    def __init__(self, name):
        print('init方法执行了')
        self.name = name
        print(self)

    def speak(self):
        print('大家好，我是%s' % self.name)


p1 = Person('葫芦娃')
p2 = Person('钢铁侠')
p3 = Person('超人')
# Person代码中的代码
# init方法执行了
# <__main__.Person object at 0x000000000228C940>
# init方法执行了
# <__main__.Person object at 0x000000000228C908>
# init方法执行了
# <__main__.Person object at 0x0000000002287CF8>

