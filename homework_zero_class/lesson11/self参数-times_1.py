#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/28 22:18
# @Author : 老萝卜
# @File : self参数-times_1.py
# @Software: PyCharm Community Edition

# 定义一个人类
class Person:
    name = '葫芦娃'
    def speak(a):
        print("同学们好！")

p1=Person()
p2=Person()

print(p1.name)          # 葫芦娃
print(p1.name)          # 葫芦娃

p1.name="钢铁侠"
p2.name="绿巨人"

print(p1.name)          # "钢铁侠"
print(p2.name)          # "绿巨人

p1.speak()
p2.speak()
# 同学们好！
# 同学们好！

class Person:
    name = '葫芦娃'

    # 方法每次被调用的时候，解析器会自动传递一个实参
    # 如果是p1调用，则第一个参数(a) 就是p1对象
    # 如果是p2调用，则第一个参数(a) 就是p2对象
    # 一般我们都会命名这个参数为self
    def speak(a):
        # print("你好,我是绿巨人")
        # print("你好,我是绿巨人%s"%name)        # NameError: name 'name' is not defined
        print("你好,我是%s"%p1.name)
        print("你好,我是%s"%p2.name)
        print("a=",a,id(a))
        print("你好,我是%s" % a.name)

p1=Person()
p2=Person()

p1.name="钢铁侠"
p2.name="绿巨人"

p1.speak()
print("p1=",p1,"id(p1))=",id(p1))
p2.speak()
print("p2=",p2,"id(p1))=",id(p2))