# -*- coding: utf-8 -*-
# @time :2020/7/30 16:00
# @Author:老萝卜
# @file:类的特殊方法-times_3
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


# 第一个 name是必须的 第二个 name是不同的 第三个 这种添加name的方式非常容易出现错误
# 我们希望在创建对象的时候，必须设置name属性。如果不设置对象都无法创建

class Person:
    # 在类中有一些特殊方法(魔术方法)
    # 　特殊方法都是以＿开头＿结尾的方法
    # 特殊方法不需要我们自己调用
    # 特殊方法会在特殊时候自己调用
    # name = '葫芦娃'
    def __init__(self, name):
        # print('init方法执行了')
        # 通过self向新创建的对象初始化属性
        self.name = name
        # print('Person代码中的代码')
        # print(self)

    def speak(self):
        print('大家好，我是%s' % self.name)


p1 = Person('abc')
# p1.__init__()               # TypeError: __init__() missing 1 required positional argument: 'name'
p1.speak()
# 大家好，我是abc





# 类的基本结构
# class 类名(父类):
#     公共属性
#
#     # 对象初始化的方法
#     def __init__(self, ......):
#         ....
#
#     # 其他的方法
#     def method1(self, ....)
#
#         .....
#
#     def method2(self, ....)
#
#         .....
#  类在定义时,公共属性执行一次，方法不执行，每实例化一个对象时 __init__方法执行一次，其它方法由实例调用时执行

class Person:
    print('Person代码中的代码')
    def __init__(self, name):
        print('init方法执行了')
        # 通过self向新创建的对象初始化属性
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



