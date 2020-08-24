# -*- coding: utf-8 -*-
# @time :2020/7/24 10:41
# @Author:老萝卜
# @file:文档字符串-times_3
# @Software:%{PRODUICT_NAME}


'''
help() 可以查询Python中函数的用法
语法 help(函数对象)
'''
# help(print)

def fn(a:int,b:str,c:bool) -> int:
    '''
    这是一个文档字符串的案例

    参数的作用
    :param a: 作用.... 类型... 默认值...
    :param b: 作用.... 类型... 默认值...
    :param c: 作用.... 类型... 默认值...
    :return:
    '''
    return 123

help(fn)
fn(1,'abc',True)
fn(1,('abc'),True)