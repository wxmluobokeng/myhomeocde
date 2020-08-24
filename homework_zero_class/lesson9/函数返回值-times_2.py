# -*- coding: utf-8 -*-
# @time :2020/7/24 10:00
# @Author:老萝卜
# @file:函数返回值-times_2
# @Software:%{PRODUICT_NAME}


def s(*b):
    # 定义一个变量 保存结果
    r = 0
    # 遍历元组，并将元组中的数进行累加
    for i in b:
        r += i
    # print(r)
    return r
r = s(1,2)
print(r - 6)

def fn():
    # return 123
    # return 'python'
    # return [1,2,3]
    # return '123'
    def fn2():
        print('hahaha')

    return fn2

print(fn())
r = fn()
print(r)
r()


def fn2():
    # return
    a = 123
    print('hahah')
r = fn2()

print(r)

def fn3():
    print('hahah')
    return
    print('123')

r = fn3()
print(r)


def fn4():
    for i in range(5):
        if i == 3:
            return # 用来结束函数
        print(i)
    print('循环执行完毕！！！')
fn4()


def fn():
    return 123
    # print('hello')
print(fn)
# fn()
print(fn())
