# -*- coding: utf-8 -*-
# @time :2020/7/24 12:28
# @Author:老萝卜
# @file:递归练习-times_2
# @Software:%{PRODUICT_NAME}

# 练习 定义一个函数 来为任意数字做任意幂运算
# 10 ** 5 = 10 * 10 ** 4
# 10 ** 4 = 10 * 10 ** 3
# ...
# 10 ** 1 = 10

def fn1(n,i):
    # 参数 n 做幂运算的数字 i 做幂运算的次数
    # 基线条件
    if i == 1:
        return n
    # 递归条件
    return n * fn1(n,i-1)

print(fn1(5,8))
print(5 ** 8)
# 390625
# 390625



def fn2(s):
    if len(s) < 2:
        return True
    elif s[0] != s[-1]:
        return False
    return fn2(s[1:-1])
print(fn2('g'))
print(fn2('abcdefggfedcba'))
print(fn2('abcdefghfedbca'))
# True
# True
# False

# 练习 定义一个函数 用来检查一个任意字符串是否是回文字符串。如果是就返回True 不是就返回False
def fn2(s):
    if len(s) < 2:
        return True
    return s[0] == s[-1] and fn2(s[1:-1])

print(fn2('g'))
print(fn2('abcdefggfedcba'))
print(fn2('abcdefghfedbca'))
# True
# True
# False


