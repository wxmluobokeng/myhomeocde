# -*- coding: utf-8 -*-
# @time :2020/7/24 11:14
# @Author:老萝卜
# @file:命名空间-times_2
# @Software:%{PRODUICT_NAME}


# 命名空间实际上就是一个字典。是一个专门用来存储变量的字典

# locals()用来获取当前作用域的命名空间
# 返回的是一个字典
a = 80
b = 30

scope = locals() # 获取当前的命名空间
print(scope)
print("a=",a)
print('scope["a"]=',scope["a"])
#{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000000000260A208>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'E:/DevProjects/python-course/homework_zero_class/lesson9/命名空间-times_1.py', '__cached__': None, 'a': 80, 'b': 30, 'scope': {...}}
# a= 80
# scope["a"]= 80


# # 向scope中添加一个key-value (就相当于在全局中创建了一个变量)
# print(c)  # NameError: name 'c' is not defined
scope['c'] = 123
print(c)
# 123


def fn4():
    scope = locals() # 要获取函数内部的命名空间
    print(scope)
fn4()
# {}

def fn4():
    scope = locals() # 要获取函数内部的命名空间
    print(scope)
fn4()
# {'a': 20}

def fn4():
    a=20
    scope = locals() # 要获取函数内部的命名空间
    scope['d'] = 200
    # print(d)      #  NameError: name 'd' is not defined
    print(scope)
    # print("d=",d)  #  NameError: name 'd' is not defined
fn4()
# {'a': 20, 'd': 200}

def fn4():
    a=20
    # globals() # 这个函数可以在任意位置获取全局的命名空间
    global_scope = globals()
    print(global_scope)
fn4()
# {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0000000001DBA208>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'E:/DevProjects/python-course/homework_zero_class/lesson9/命名空间-times_3.py', '__cached__': None, 'a': 80, 'b': 30, 'scope': {...}, 'c': 123, 'fn4': <function fn4 at 0x000000000287F840>}

