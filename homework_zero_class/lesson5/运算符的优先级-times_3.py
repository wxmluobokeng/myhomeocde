#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/12 17:56
# @Author : 老萝卜
# @File : 运算符的优先级-times_3.py.py
# @Software: PyCharm Community Edition

print(2 or 3 and 4)                 # 2
'''
or 优先级低于 and ,即 2 or (3 and 4 )
or 非布尔值运算规则：“如果第一个值是True，则不看第二个值，直接返回第一个值，否则返回第二个值”
2是True，直接返回2
'''

print( (2 or 3 ) and 4 )            # 4
'''
() 比 and 优先级高，(2 or 3 ) 和 4 与运算
and 运算规则是“如果第一个值是False，则不看第二个值，直接返回第一个值，否则返回第二个值”
所以还得先算（2 or 3），得到 2
根据与运算规则，（2 or 3 )=2 是True
所以 直接返回 4
'''

print(2 and 3 or 4)                 # 3
'''
or 优先级低于 and ,即 （ 2 and 3 ） or 4
or 非布尔值运算规则：*“如果第一个值是True，则不看第二个值，直接返回第一个值，否则返回第二个值”
如果(2 and 3) 是True，就返回(2 and 3）的值, 否则返回4
与运算规则是**“如果第一个值是False，则不看第二个值，直接返回第一个值，否则返回第二个值”**
2 是True，所以 （2 and 3)= 3
所以 直接返回 3
'''
