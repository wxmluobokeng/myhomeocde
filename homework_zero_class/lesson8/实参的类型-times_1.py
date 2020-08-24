# -*- coding: utf-8 -*-
# @time :2020/7/22 12:53
# @Author:老萝卜
# @file:实参的类型-times_1
# @Software:%{PRODUICT_NAME}


def fn2(a):
    print('a =',a)
# 实参可以传递任意类型的对象
# 函数在调用的时候解析器是不会检查函数的类型的
b = 123
fn2(b)

b = [1,2,3]
fn2(b)

b = True
fn2(b)

b = 'python'
fn2(fn)


def fn(a):
    print(print('a =',a))

fn2(fn)
fn2(fn())


def fn3(a,b):
    print(a + b)

fn3(1,2)
# fn3(1,'2') # TypeError: unsupported operand type(s) for +: 'int' and 'str'

def fn4(a,b,c):
    # 在函数中对形参重新赋值，不会影响其他的变量
    a = 20
    # a是一个列表 修改列表里面的元素 如果形参时一个可变对象，当我们修改对象(改对象的值)
    # 会影响到所指向该对象的变量
    b[0] = 10
    c=b
    print('a =',a,id(a))
    print('b =',b,id(b))
    print('c =',c,id(c))

a = 10
b = [1,2,3]
c= (1,2,3)

fn4(a,b,c)

print("-------")
print('a =', a, id(a))
print('b =', b, id(b))
print('c =', c, id(c))