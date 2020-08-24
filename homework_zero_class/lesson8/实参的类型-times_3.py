# -*- coding: utf-8 -*-
# @time :2020/7/22 13:16
# @Author:老萝卜
# @file:实参的类型-times_3
# @Software:%{PRODUICT_NAME}


def fn2(a):
    print('fn2函数输出结果：a =', a, "type(a)=", type(a))


# 实参可以传递任意类型的对象
# 函数在调用的时候解析器是不会检查函数的类型的
b = 123
fn2(b)

b = [1, 2, 3]
fn2(b)

b = True
fn2(b)

b = 'python'
fn2(b)


def fn(a):
    print('fn函数输出结果：a =', a)


fn2(fn)
fn2(fn(1))


def fn3(a, b):
    print("a + b = ",a + b)


fn3(1, 2)


# fn3(1,'2') # TypeError: unsupported operand type(s) for +: 'int' and 'str'

def fn4(a, b, c):
    # 在函数中对形参重新赋值，不会影响其他的变量
    a = 20
    # a是一个列表 修改列表里面的元素 如果形参时一个可变对象，当我们修改对象(改对象的值)
    # 会影响到所指向该对象的变量
    b[0] = 10
    c = b
    print('函数内：a =', a, "id(a)=", id(a))
    print('函数内：b =', b, "id(a)=", id(b))
    print('函数内：c =', c, "id(a)=", id(c))


a = 10
b = [1, 2, 3]
c = [1, 2, 3]

print('调用前：a =', a, "id(a)=", id(a))
print('调用前：b =', b, "id(a)=", id(b))
print('调用前：c =', c, "id(a)=", id(c))

fn4(a, b, c)

print('调用后：a =', a, "id(a)=", id(a))
print('调用后：b =', b, "id(a)=", id(b))
print('调用后：c =', c, "id(a)=", id(c))



# fn2函数输出结果：a = 123 type(a)= <class 'int'>
# fn2函数输出结果：a = [1, 2, 3] type(a)= <class 'list'>
# fn2函数输出结果：a = True type(a)= <class 'bool'>
# fn2函数输出结果：a = python type(a)= <class 'str'>
# fn2函数输出结果：a = <function fn at 0x000000000235E840> type(a)= <class 'function'>
# fn函数输出结果：a = 1
# fn2函数输出结果：a = None type(a)= <class 'NoneType'>
# a + b =  3
# 调用前：a = 10 id(a)= 495808256
# 调用前：b = [1, 2, 3] id(a)= 42575368
# 调用前：c = [1, 2, 3] id(a)= 42574920
# 函数内：a = 20 id(a)= 495808576
# 函数内：b = [10, 2, 3] id(a)= 42575368
# 函数内：c = [10, 2, 3] id(a)= 42575368
# 调用后：a = 10 id(a)= 495808256
# 调用后：b = [10, 2, 3] id(a)= 42575368
# 调用后：c = [1, 2, 3] id(a)= 42574920
