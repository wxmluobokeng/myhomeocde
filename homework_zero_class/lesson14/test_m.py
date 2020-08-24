#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/8/4 22:02
# @Author : 老萝卜
# @File : test_m.py
# @Software: PyCharm Community Edition

print("这是我的第一个模块")

print("__name__ = ",__name__)

# 在模块中定义变量
a = 1
b = 2


username = 'shuai jerry'
password = '123456'


# c是私有的(不希望你去修改)
_c = 3

# 在模块中定义函数
def test1():
    print('test1')

def test2():
    print('test2')

# 在模块中定义类
class Person:
    def __init__(self):
        self.name = '葫芦娃'
    def est3(self):
        print("这是Person类的实例函数test3")


p = Person()
if __name__ == '__main__':
    # 以下是测试代码
    print(p.name)
    test1()
    test2()


# 这是我的第一个模块
# __name__ =  __main__
# 葫芦娃
# test1
# test2
