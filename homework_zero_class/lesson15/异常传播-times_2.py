#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/8/6 23:05
# @Author : 老萝卜
# @File : 异常传播-times_2.py
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


def fn():
    print('hello fn')
    print(6 / 0)

def fn2():
    print('hello fn2')
    fn()


def fn3():
    print('hello fn3')
    fn2()

# fn3()
# # hello fn3
# # Traceback (most recent call last):
# # hello fn2
# #   File "E:/python-course/homework_zero_class/lesson15/异常传播-times_1.py", line 59, in <module>
# # hello fn
# #     fn3()
# #   File "E:/python-course/homework_zero_class/lesson15/异常传播-times_1.py", line 57, in fn3
# #     fn2()
# #   File "E:/python-course/homework_zero_class/lesson15/异常传播-times_1.py", line 52, in fn2
# #     fn()
# #   File "E:/python-course/homework_zero_class/lesson15/异常传播-times_1.py", line 48, in fn
# #     print(6 / 0)
# # ZeroDivisionError: division by zero

