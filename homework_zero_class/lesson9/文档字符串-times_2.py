# -*- coding: utf-8 -*-
# @time :2020/7/24 10:39
# @Author:老萝卜
# @file:文档字符串-times_2
# @Software:%{PRODUICT_NAME}

def fn(a:int,b:str,c:bool) -> int:
    '''
    这是一个文档字符串的案例

    参数的作用
    :param a: 作用.... 类型... 默认值...
    :param b: 作用.... 类型... 默认值...
    :param c: 作用.... 类型... 默认值...
    :return:
    '''

    print("a=",a,"type(a)=",type(a))
    print("b=",b,"type(b)=",type(b))
    print("c=",c,"type(c)=",type(c))
    return 123

help(fn)
fn(1,'abc',True)
fn(1,(1,'abc'),True)

# Help on function fn in module __main__:
#
# fn(a:int, b:str, c:bool) -> int
#     这是一个文档字符串的案例
#
#     参数的作用
#     :param a: 作用.... 类型... 默认值...
#     :param b: 作用.... 类型... 默认值...
#     :param c: 作用.... 类型... 默认值...
#     :return:
#
# a= 1 type(a)= <class 'int'>
# b= abc type(b)= <class 'str'>
# c= True type(c)= <class 'bool'>
# a= 1 type(a)= <class 'int'>
# b= (1, 'abc') type(b)= <class 'tuple'>
# c= True type(c)= <class 'bool'>
