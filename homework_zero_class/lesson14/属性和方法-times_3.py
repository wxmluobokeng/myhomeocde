# -*- coding: utf-8 -*-
# @time :2020/8/4 13:52
# @Author:老萝卜
# @file:属性和方法-times_3
# @Software:%{PRODUICT_NAME}

class A(object):
    # 类属性 直接在类中定义的属性
    # 类属性可以通过类和该类的实力来访问
    # 类中的属性只能通过类对象来修改，无法通过实例对象来修改
    count = 0       # 类属性


a = A()
print(a.count)  # 0
print(A.count)  # 0
a.count = 10
print(a.count)  # 10
print(A.count)  # 0
A.count = 20
print(a.count)  # 10
print(A.count)  # 20


# 实例属性： 通过实例对象添加的属性属于实例属性
class A(object):
    count = 0       # 类属性
    def __init__(self):
        # 实例属性只能通过实例对象来访问，类对象无法访问和修改
        self.name = '葫芦娃'           # 实例属性

a = A()
a.age = 4           # 实例属性
print(a.name)
# 葫芦娃
# print(A.name)  # AttributeError: type object 'A' has no attribute 'name'
a.name="钢铁侠"
a.age=5
print(a.name,a.age)
# 钢铁侠 5


class A(object):
    count = 0       # 类属性
    def __init__(self):
        # 实例属性只能通过实例对象来访问，类对象无法访问和修改
        self.name = '葫芦娃'    # 实例属性

    # 实例方法
    # 在类中定义 以self为第一个参数的方法都是实例方法
    # 当通过实例对象调用时，会自动传递当前对象作为self传入
    # 当通过类去调用时，不会自动传递self
    def text(self):
        print('这是test方法',self)

a=A()
a.text()
# 这是test方法 <__main__.A object at 0x000000000271D400>
# A.text()    # TypeError: text() missing 1 required positional argument: 'self'
A.text(a)
# 这是test方法 <__main__.A object at 0x000000000271D400>


# a.text() 等价于 A.text(a)

class A(object):
    count = 0       # 类属性
    def __init__(self):             # 实例方法
        # 实例属性只能通过实例对象来访问，类对象无法访问和修改
        self.name = '葫芦娃'           # 实例属性

    # 实例方法
    # 在类中定义 以self为第一个参数的方法都是实例方法
    # 当通过实例对象调用时，会自动传递当前对象作为self传入
    # 当通过类去调用时，不会自动传递self
    def text(self):                 # 实例方法
        print('这是test方法',self)

    # 类方法
    # 在类的内部使用 @classmethod 来修饰的方法属于类方法
    # 类方法的第一个参数我们习惯写成cls 也会自动传递 cls就相当于当前的类对象
    @classmethod
    def text2(cls):             # 类方法
        print('这个是test2方法',cls)
        print(cls.count)

A.text2()       # 0
a= A()
a.text2()      # 0




class A(object):
    count = 0       # 类属性
    def __init__(self):
        # 实例属性只能通过实例对象来访问，类对象无法访问和修改
        self.name = '葫芦娃'       # 实例属性

    # 实例方法
    # 在类中定义 以self为第一个参数的方法都是实例方法
    # 当通过实例对象调用时，会自动传递当前对象作为self传入
    # 当通过类去调用时，不会自动传递self
    def text(self):     # 实例方法
        print('这是test方法',self)

    # 类方法
    # 在类的内部使用 @classmethod 来修饰的方法属于类方法
    # 类方法的第一个参数我们习惯写成cls 也会自动传递 cls就相当于当前的类对象
    @classmethod
    def text2(cls):         # 类方法
        print('这个是test2方法',cls)
        print(cls.count)

    # 静态方法
    # 在类中用  @staticmethod来修饰的方法我们称之为静态方法
    # 不需要制定任何的默认参数 静态方法可以被类对象和实例对象调用
    # 静态方法跟类本身无关，就是一个功能函数
    @staticmethod
    def text3():            # 静态方法
        print('这个是test3方法')

A.text3()
a=A()
a.text3()
# 这个是test3方法
# 这个是test3方法