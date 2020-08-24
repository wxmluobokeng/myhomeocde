# -*- coding: utf-8 -*-
# @time :2020/7/22 13:38
# @Author:老萝卜
# @file:不定长参数-times_1
# @Software:%{PRODUICT_NAME}

# 定义函数时，可以在形参前面加一个*,这样这个形参可以获取到所有的实参，它会将所有的实参保存到一个元组中
# 可以求任意数的和

def s(a,b):
    print(a + b)

def s2(a,b,c):
    print(a + b + c)

# s(1,2,3)   # TypeError: s() takes 2 positional arguments but 3 were given
s2(1,2,3)
# s2(1,2)   # TypeError: s() missing 1 required positional argument: 'c'

def fn(*b):
    print('b =',b,type(b))

# *b 会接受所有的位置实参，并且会将这些实参统一保存到一个元组当中
fn(1,2,3,4,5,6,7,8)

def s(*b):
    # 定义一个变量 保存结果
    r = 0
    # 遍历元组，并将元组中的数进行累加
    for i in b:
        r += i
    print(r)

s(1,2,300)


# def  fn2(a,*b,*c):
#     pass
# SyntaxError: invalid syntax
# 带*只能有一个
# 不定长参数不是必须写在最后，但是注意 带*的参数后面的所有的形参，必须以关键字的形式来传递
def fn2(a,b,*c):

    print('a =',a)
    print('b =',b)
    print('c =',c)
a = 1
b = 2
c = (3, 4, 5)

def fn2(a,*b,c):

    print('a =',a)
    print('b =',b)
    print('c =',c)

# fn2(1,2,3,4,5)  # TypeError: fn2() missing 1 required keyword-only argument: 'c'
fn2(1,2,3,4,c=5)
# a = 1
# b = (2, 3, 4)
# c = 5

def fn2(*a,b,c):
    print('a =',a)
    print('b =',b)
    print('c =',c)

# fn2(1,2,3,4,c=5)    # TypeError: fn2() missing 1 required keyword-only argument: 'b'
# fn2(1,2,3,b=4,5)  # SyntaxError: positional argument follows keyword argument
fn2(1,2,3,b=4,c=5)
# a = (1, 2, 3)
# b = 4
# c = 5

# *形参只能接受位置参数，不能接受关键字参数
def fn3(*b):
    print('b =', b)
# fn3(b=1,d=2,c=3)    # TypeError: fn3() got an unexpected keyword argument 'b'



def fn3(**b):
    print('b =',b)

fn3(b=1,d=2,c=3)

def fn3(b,c,**a):
    print('a =',a)
    print('b =',b)
    print('c =',c)

fn3(b=1,d=2,c=3,e=50,f=80)

# *b 处理的是位置参数 **a处理的是关键字参数  *args,**kwargs
