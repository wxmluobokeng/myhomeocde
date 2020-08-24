# -*- coding: utf-8 -*-
# @time :2020/7/24 12:43
# @Author:老萝卜
# @file:递归练习-times_3
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

# 练习 定义一个函数 用来检查一个任意字符串是否是回文字符串。如果是就返回True 不是就返回False

# 什么是回文字符串？ 字符串从后往前念和从前往后念是一样的 例如 aba abcba b

# abcdefgfedcba
# 先检查第一个字符和最后一个字符是否一致，如果不一致一定不是回文
# 如果第一个字符和最后一个字符一致。看其余的部分是不是回文字符串
# 检查 bcdefgfedcb 是不是回文字符串
# 检查 cdefgfedc 是不是回文字符串
# 检查 defgfed 是不是回文字符串
# ...
#  检查 fgf 是不是回文字符串
# 检查 g 是不是回文字符串


def fn2(s):
    # 参数 s 要检查的字符串
    # 基线条件
    # if len(s) < 2:
    #
    #     # 字符串的长度小于2 则字符串一定是回文字符串
    #     return True
    #
    # elif s[0] != s[-1]:
    #     # 第一个字符和最后一个字符不相等 不是回文字符串
    #     return False
    #
    # # 递归条件
    # return fn2(s[1:-1])
    if len(s) < 2:
        return True
    return s[0] == s[-1] and fn2(s[1:-1])

print(fn2('g'))
print(fn2('abcdgcba'))
print(fn2('abcggcba'))
print(fn2('abcggcba?'))
print('abcggcba?'[1:-1])

# s = 'abcgcba'
# # bcgcb
# s = 'bcgcb'
# # cgc
# print(s[1:-1])



