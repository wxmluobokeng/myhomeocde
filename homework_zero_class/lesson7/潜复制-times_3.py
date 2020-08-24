#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/18 21:50
# @Author : 老萝卜
# @File : 潜复制-times_1.py
# @Software: PyCharm Community Edition


# copy()
# 浅复制只会复制字典的本身，如果字典中还有个字典是不会被复制的
# 用于对字典进行一个浅复制
# 复制以后的对象，和原对象是独立的。修改一个不会影响另一个
d = {'a':{'name':'黑猫警长','age':18},'b':2,'c':3}
d2 = d
d['b'] = 20

print(d,id(d))
print(d2,id(d2))
# {'a': {'name': '黑猫警长', 'age': 18}, 'b': 20, 'c': 3} 34631184
# {'a': {'name': '黑猫警长', 'age': 18}, 'b': 20, 'c': 3} 34631184

d = {'a':{'name':'黑猫警长','age':18},'b':2,'c':3}
d2 = d.copy()
d['a'] = 60
print('d = ',d,id(d))
print('d2 =',d2,id(d2))
# d =  {'a': 60, 'b': 2, 'c': 3} 39261384
# d2 = {'a': {'name': '黑猫警长', 'age': 18}, 'b': 2, 'c': 3} 4681520

d = {'a':{'name':'黑猫警长','age':18},'b':2,'c':3}
d2 = d.copy()
d2['a']['name'] = '皮卡丘'
print('d = ',d,id(d))
print('d2 =',d2,id(d2))

# d =  {'a': {'name': '皮卡丘', 'age': 18}, 'b': 2, 'c': 3} 31092168
# d2 = {'a': {'name': '皮卡丘', 'age': 18}, 'b': 2, 'c': 3} 35984584



d={"a":[1,2,3,4],"b":2,"c":3}
d2=d.copy()
print(d)
print(d2)
print(id(d),id(d2))
# {'a': [1, 2, 3, 4], 'b': 2, 'c': 3}
# {'a': [1, 2, 3, 4], 'b': 2, 'c': 3}
# 34762544 34762184
d2["b"]=200
d2["a"][1]="钢铁侠"
print(d)
print(d2)
# {'a': [1, '钢铁侠', 3, 4], 'b': 2, 'c': 3}
# {'a': [1, '钢铁侠', 3, 4], 'b': 200, 'c': 3}

d={"a":(1,2,3,4),"b":2,"c":3}
d2=d.copy()
print(d)
print(d2)
print(id(d),id(d2))
# {'a': (1, 2, 3, 4), 'b': 2, 'c': 3}
# {'a': (1, 2, 3, 4), 'b': 2, 'c': 3}
# 39261384 34762544
d2["b"]=200
d2["a"]="钢铁侠",
print(d)   # {'a': (1, 2, 3, 4), 'b': 2, 'c': 3}
print(d2)  # {'a': ('钢铁侠',), 'b': 200, 'c': 3}
# {'a': (1, 2, 3, 4), 'b': 2, 'c': 3}
# {'a': ('钢铁侠',), 'b': 200, 'c': 3}


