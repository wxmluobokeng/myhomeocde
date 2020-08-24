#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/18 20:22
# @Author : 老萝卜
# @File : 字典的使用-times_2.py
# @Software: PyCharm Community Edition

d = dict(name='钢铁侠',age=35,sex='男')
print(d,type(d))

# dict()函数也可以将一个包含有双值子序列转换为字典
# 双值序列 序列中有2个值 [1,2] ('b','a') 'ab'
# 子序列 如果序列中的元素，那么我们就称这个元素为子序列 [1,2,3]（No）[(1,2),(3,4)]

d = dict([('name','钢铁侠'),('age',35)])
print(d,type(d))

#　len() 获取字典中键值对的个数

print(len(d))

# in 检查字典中是否包含指定的键 True / False
# not in 检查字典中是否不包含指定的键

print('name' not in d)
# 可以根据键来获取字典当中的值
# 语法：d[key]
d = {'name':'钢铁侠','age':38,'sex':'男'}
print(d['age'])

n = 'age'
print(d[n])
# print(d['n']) # KeyError: 'n'



# get(key,[default]) 该方法是用来根据键来获取字典当中的值
# 如果字典当中没有这个Key值，会返回一个None
# 也可以指定一个默认值。来作为第二个参数，这样获取不到Key值的时候就返回默认值
print(d.get('age'))
print(d.get('hello','这个key值不存在'))

# 修改字典
# d[key] = value

d['name'] = '葫芦娃' # 修改字典中的key-value
d['phone'] = '123456789' # 向字典中添加 key-value
print(d)

# setdefault(key,[default]) 向字典中添加 key-value
# 如果这个key已经存在于字典当中，则返回key值，不会对字典有任何的影响
# 如果Key不存在 则向字典中添加这个key 并设置value

result = d.setdefault('name','葫芦娃')
result = d.setdefault('hello','葫芦娃')
print(result)
print(d)

# update() 将其他字典当中的key-value添加到当前字典当中
d1 = {'a':1,'b':2,'c':3}
d2 = {'d':4,'e':5,'f':6}

d1.update(d2)

print(d1)

print(d2)


# 删除
# del 来删除字典中的key-value
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
del d1['a']
del d1['b']
#
print(d1)



# popitem() 随机删除一个键值对，一般都会删除最后一个
# 它会将删除之后的键值对作为返回值返回
# 返回的是一个元祖 元祖中有2个元素 第一个元素时删除的Key 第二个元素时删除的value

result = d1.popitem() # ('e', 5)
print(result)
print(d1)

# {'c': 3, 'd': 4}


# pop(key,[default]) 根据Key来删除 key-value
# {'c': 3, 'd': 4, 'e': 5}
result = d1.pop('b','这个key值不存在')
result = d1.pop('b')
print(result,d1)

# clear() 清空字典

d1.clear()

print(d1)