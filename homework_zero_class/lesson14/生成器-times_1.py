# -*- coding: utf-8 -*-
# @time :2020/8/5 12:52
# @Author:老萝卜
# @file:生成器-times_1
# @Software:%{PRODUICT_NAME}

# 在Python中有一边循环一边计算的机制，称之为生成器 generator

# 如何创建生成器

# 1.通过列表推导式

# 需求:得到一个0-10之内 分别和3想乘的列表

new_lst = [x * 3 for x in range(10)]
print(type(new_lst),new_lst)
# <class 'list'>    [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]

g = (x * 3 for x in range(10))
print(type(g),g)
# <class 'generator'>    <generator object <genexpr> at 0x0000000002699E60>

# 方式一__next__() 获得元素
print(g.__next__())         # 0
print(g.__next__())         # 3
print(g.__next__())         # 6
print(g.__next__())         # 9


# # 方式二 next()

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
# print(next(g)) #　StopIteration　
# 当取值超出生成器范围时，会报错


# 定义生成器方式二 通过函数来完成
# 只要在函数中添加了yield关键字，就变成了一个生成器函数
# 1 .定义一个函数，函数中使用yield关键字
# 2 .调用函数，接收调用结果
# 3 .得到的结果就是个生成器
# 4 .通过next()函数 __next__()
def fn():
    n = 0
    while True:
        n += 1
        # print(n)
        yield n  #  return n + 暂停
        # return n
n = fn()
print(n)
print(next(n))
print(next(n))



