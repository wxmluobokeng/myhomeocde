# -*- coding: utf-8 -*-
# @time :2020/7/10 16:36
# @Author:老萝卜
# @file:布尔值_times_1
# @Software:%{PRODUICT_NAME}

print(1 + 2)

# print(1 + 'hello') # 报错： TypeError: unsupported operand type(s) for +: 'int' and 'str'

print("2 + True =",2 + True)
print("2 + False=",2 + False)
print("2 / True",2 / True)
print("2 * False",2 * False)

i = 0
while 1:
    if i>10:
        break
    i += 1
    pass
print(i)
while True:
    if i < 0:
        break
    i -= 1
    pass