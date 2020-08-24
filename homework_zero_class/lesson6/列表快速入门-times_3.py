#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/14 22:51
# @Author : 老萝卜
# @File : 列表快速入门-times_3.py
# @Software: PyCharm Community Edition




# [] 创建一个空的list列表对象

list1=[]
print(list1)

list1 = [1,2,3]
print(list1)

#list(序列)   创建一个序列
list1= range(5)
# print[range(5)]   #TypeError: 'builtin_function_or_method' object is not subscriptable
print(list1,type(list1))
list1= list(range(5))
print(list1,type(list1))
list1=list("老萝卜")
print(list1,type(list1))
print(list())       #创建一个空序列



# 列表可以保存任意对象
list2 = [1 , 'a',None,True,max(4,5),print()]
print(list2,type(list2))

# 可以通过索引(index)来获取列表中元素
# 索引就是元素在列表中的位置 列表当中每一个位置都会有一个索引 索引是从0开始，列表的第一个位置就是0,第二个位置是1 以此类推,最后一个元素是len(列表)-1

list3 = [10,20,30,40,50]

print(list3[0],list3[2],list3[4],list3[1],list3[3])

# print(list3[5]) # IndexError: list index out of range   下标超出列表范围时，会报错

# len()函数可以获取列表的长度（列表元素的个数）
# 总结：获取列表的长度，可以是列表的最大索引值+1
print(len(list3))
# 索引可以是负数，如果索引为负是从后往前获取元素 -1表示最后一个 -2表示倒数第二个 以此类推,第一个元素是-len(列表)
print(list3[-2])
print(list3[-3])
print(list3[-4])

# print(list3[-8])    # IndexError: list index out of range    下标负数超出范围也会报错