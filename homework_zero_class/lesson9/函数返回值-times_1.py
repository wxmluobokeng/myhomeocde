# -*- coding: utf-8 -*-
# @time :2020/7/24 9:46
# @Author:老萝卜
# @file:函数返回值-times_1
# @Software:%{PRODUICT_NAME}

# 求任意数的和
# 返回值就是函数执行以后返回的结果
# 可以通过return来指定函数的返回值
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
    # return后面跟什么值，函数就会返回什么值
    # return后面可以跟任意的对象，甚至是一个函数
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


def fn3():
    return

r = fn3()
print(r)

def fn4():
# 在函数中return后的代码都不会执行,return一旦执行函数自动结束
    print('hahah')
    return
    print('123')

r = fn4()
print(r)


def fn5():
    print("测试break")
    for i in range(5):
        if i == 3:
            break # 立即退出当前的循环
        print(i)
    print('循环执行完毕！！！')
fn5()
# 测试break
# 0
# 1
# 2
# 循环执行完毕！！！

def fn5():
    print("测试continue")
    for i in range(5):
        if i == 3:
            continue # 用来跳过循环
        print(i)
    print('循环执行完毕！！！')
fn5()
# 测试continue
# 0
# 1
# 2
# 4
# 循环执行完毕！！！

def fn5():
    print("测试return")
    for i in range(5):
        if i == 3:
            return # 用来结束函数
        print(i)
    print('循环执行完毕！！！')
fn5()
# 测试return
# 0
# 1
# 2

def fn():
    # print('hello')
    return 123

print(fn)
fn()
print(fn())
# <function fn at 0x000000000285EA60>
# 123

# fn  是函数对象 打印fn实际上就是在打印函数对象
# fn() 是在调用函数 打印fn()实际上就是在打印fn()的返回值