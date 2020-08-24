#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/24 0:57
# @Author : 老萝卜
# @File : 函数的作用域-times_4.py
# @Software: PyCharm Community Edition

b = 20
def fn1():
    def fn2():
        a = 30
        # a定义在了函数fn3内部，所有它的作用域就是函数内部，函数外部访问不到
        print("fn2中：a =",a)
        print("fn2中：b =",b)
    fn2()
    # print("fn1中：a =", a)
    print("fn1中：b =", b)


fn1()
print('函数外部:', 'b =', b)
# print('函数外部:', 'a =', a)        # NameError: name 'a' is not defined
# 函数内部: a = 10
# 函数内部: b = 20
# 函数外部: b = 20
