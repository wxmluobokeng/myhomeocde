#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/12 16:45
# @Author : 老萝卜
# @File : 循环嵌套-times_3.py
# @Software: PyCharm Community Edition



level = 8   #输出层数
# *****
# *****
# *****
# *****
# *****
i=0
while i<level:
    j=0
    while j<5:
        print("*",end="")
        j+=1
    print()
    i+=1
else:
    print("图形打印完成\n")

# *                 第一层  1个*
# **                第二层  ２个*
# ***               第三层  ３个*
# ****              第四层  ４个*
# *****             第五层  ５个*
i=0
while i <level:
    i+=1
    j=0
    while j<i:
        print("*",end="")
        j+=1
    print()
else:
    print("图形打印完成\n")

# *****         第一层  5个*    5-0
# ****          第一层  4个*    5-1
# ***           第一层  3个*    5-2
# **            第一层  2个*    5-3
# *             第一层  1个*    5-4
i =0
while i<level:
    j=0
    while j<level-i:
        print("*",end="")
        j+=1
    print()
    i+=1
else:
    print("图形打印完成\n")
#    *          第一层 i=0   数量1 左边3个空格 + 1个* + 左边3个空格   4-1个空格  1*2-1个*
#   ***         第二层 i=1   数量3 左边2个空格 + 3个* + 左边2个空格   4-2个空格  2*2-1个*
#  *****        第三层 i=2   数量5 左边1个空格 + 5个* + 左边1个空格   4-3个空格  3*2-1个*
# *******       第四层 i=3   数量7 左边0个空格 + 6个* + 左边0个空格   4-4个空格  4*2-1个*


i=0
while i< level:
    i+=1
    j=0
    while j<level-i:
        print(" ",end="")
        j+=1
    k=0
    while k<i*2-1:
        print("*",end="")
        k+=1
    print()
else:
    print("图形打印完成\n")


i=0
while i< level:
    i+=1
    print(" "*(level-i)+"*"*(2*i-1))
else:
    print("图形打印完成\n")


#    *          第一层 i=0   数量1 左边3个空格 + 1个* + 左边3个空格                       4-1个空格  1个*夹0个空格
#   * *         第二层 i=1   数量2 左边2个空格 + 2个*（两星之间夹个空格） + 左边2个空格   4-2个空格  2个*夹1个空格
#  * * *        第三层 i=2   数量3 左边1个空格 + 3个*（两星之间夹个空格） + 左边1个空格   4-3个空格  3个*夹2个空格
# * * * *       第四层 i=3   数量4 左边0个空格 + 4个*（两星之间夹个空格） + 左边0个空格   4-4个空格  4个*夹3个空格

# 简单做法：# 把*+空格当作一个整体@,
#    @
#   @@
#  @@@
# @@@@
#注意：这样最后一行会存多输出一个空格，把最后一行保存到变量后截取后再打印即可
i= 0
while i<level:
    i+=1
    print(" " * (level - i) + "* " * i)
else:
    print("图形打印完成\n")

# 按每位输出做法
i =0
while i<level:
    i+=1
    print(" " * (level - i),end="")
    j=0
    while j < i * 2 - 1:
        if j % 2 ==0:
            print("*", end="")
        else:
            print(" ", end="")
        j+=1
    print()
else:
    print("图形打印完成\n")