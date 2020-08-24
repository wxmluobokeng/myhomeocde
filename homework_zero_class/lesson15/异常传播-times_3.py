#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/8/6 23:25
# @Author : 老萝卜
# @File : 异常传播-times_1.py
# @Software: PyCharm Community Edition


# print(6/0)
# def fn():
#     print('hello fn')
# # Traceback (most recent call last):
# #   File "E:/python-course/homework_zero_class/lesson15/异常传播-times_1.py", line 9, in <module>
# #     print(6/0)
# # ZeroDivisionError: division by zero

# def fn():
#     print('hello fn')
#     print(6/0)
# fn()
# # hello fn
# # Traceback (most recent call last):
# #   File "E:/python-course/homework_zero_class/lesson15/异常传播-times_1.py", line 20, in <module>
# #     fn()
# #   File "E:/python-course/homework_zero_class/lesson15/异常传播-times_1.py", line 19, in fn
# #     print(6/0)
# # ZeroDivisionError: division by zero


# 异常的传播
# 当函数中出现异常的时候，如果在函数中对异常进行了处理，则异常不会在继续传播
# 如果在函数中没有对异常进行处理，则异常会继续向函数调用处传播

# def fn():
#     print(6/0)
#     print('hello fn')
# fn()
# # Traceback (most recent call last):
# #   File "E:/python-course/homework_zero_class/lesson15/异常传播-times_1.py", line 37, in <module>
# #     fn()
# #   File "E:/python-course/homework_zero_class/lesson15/异常传播-times_1.py", line 35, in fn
# #     print(6/0)
# # ZeroDivisionError: division by zero


# def fn():
#     print('hello fn')
#     print(6 / 0)
# def fn2():
#     print('hello fn2')
#     fn()
# def fn3():
#     print('hello fn3')
#     fn2()
# fn3()
# # hello fn3
# # Traceback (most recent call last):
# # hello fn2
# # hello fn
# #   File "E:/python-course/homework_zero_class/lesson15/异常传播-times_3.py", line 55, in <module>
# #     fn3()
# #   File "E:/python-course/homework_zero_class/lesson15/异常传播-times_3.py", line 54, in fn3
# #     fn2()
# #   File "E:/python-course/homework_zero_class/lesson15/异常传播-times_3.py", line 51, in fn2
# #     fn()
# #   File "E:/python-course/homework_zero_class/lesson15/异常传播-times_3.py", line 48, in fn
# #     print(6 / 0)
# # ZeroDivisionError: division by zero
# #
# # Process finished with exit code 1

# 当程序在运行的过程当中出现异常以后，所有异常信息会被保存到一个专门的异常对象中而异常进行传播
# 时其实就是异常对象抛个了调用处

def fn():
    print('hello fn')
    print(6 / 0)
def fn2():
    print('hello fn2 调用fn前')
    fn()
    print('hello fn2 调用fn后')
def fn3():
    print('hello fn3 调用fn2前')
    try:
        fn2()
        print('hello fn3 调用fn2  try 内')
    except:
        pass
    print('hello fn3 调用fn2后')

def fn4():
    print('hello fn4 调用fn3前')
    fn3()
    print('hello fn4 调用fn3后')

fn4()
# hello fn4 调用fn3前
# hello fn3 调用fn2前
# hello fn2 调用fn前
# hello fn
# hello fn3 调用fn2后
# hello fn4 调用fn3后