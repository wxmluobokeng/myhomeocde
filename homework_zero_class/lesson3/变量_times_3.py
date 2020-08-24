# -*- coding: utf-8 -*-
# @time :2020/7/10 15:18
# @Author:老萝卜
# @file:变量_times_2
# @Software:%{PRODUICT_NAME}
'''
    功能： 测试值相等的两个变量，是否是同一个变量
    结论:  值相同的两个变量，不一定是同一变量
           字符串、数值型变量有些特殊，.
    验证思路：
        1、分别对 字典变量、列表变量、整型变量进行测试
        2、测试方法：
            a.每个类型变量取3个，第一个直接赋值，第二个用copy 第一个，第三个用第一个赋值
            b.比较值 ，比较id
            c.对其中一个变量修改，看其他变量的值是否变更

定义变量
   dict1 = 直接按定义赋值
   dict2 = 对dict1进行复制   ---> 在内存中开辟一块区域，将dict1对象的东西拷贝一份，相当于，dict2按照dict1的房子重新建
   dict3 = 将字典dict1m赋值给dict3  --->将dict1内存区域地址直接给dict3，相当于dict1和dict3 拿到的同一套房子的钥匙
'''


import copy

num = 50

dict1 = {"python","java"}
dict2 = copy.deepcopy(dict1)
dict3 = dict1
print("dict1 = ",dict1)
print("dict2 = ",dict2)
print("dict3 = ",dict3)

print("dict1的id = ",id(dict1))
print("dict2的id = ",id(dict2))
print("dict3的id = ",id(dict3))

print("判断dict1是否等于dict2 : ",dict1==dict2)
print("判断dict1是否等于dict3 : ",dict1==dict3)
print("判断dict1是否是dict2 : ",id(dict1)==id(dict2))
print("判断dict1是否是dict3 : ",id(dict1)==id(dict3))

dict1.add("C#")
dict2.add("C++")
print("dict1 = ",dict1)
print("dict2 = ",dict2)
print("dict3 = ",dict3)

dict3.clear()
print("dict1 = ",dict1)
print("dict2 = ",dict2)
print("dict3 = ",dict3)

print("-"*num)

#  list  也是
list0 = [1,2,3]
list1= copy.deepcopy(list0)
list2 = list0
print("id(list0)=",id(list0))
print("id(list1)=",id(list1))
print("id(list2)=",id(list2))
print("id(list0)==id(list1)?",id(list0)==id(list1))
print("id(list0)==id(list2)?",id(list0)==id(list2))

list1.append("python")
print("list0=",list0)
print("list1=",list1)
print("list2=",list2)

list2.append(4)
print("list0=",list0)
print("list1=",list1)
print("list2=",list2)

print("-"*num)

str0 = "作业写不完了!"
str1= copy.deepcopy(str0)
str2= str0
print("id(str0)=",id(str0))
print("id(str1)=",id(str1))
print("id(str2)=",id(str2))
print("id(str0)==id(str1)?",id(str0)==id(str1))
print("id(str0)==id(str2)?",id(str0)==id(str2))

str2 *=2
print("str0=",str0)
print("str1=",str1)
print("str2=",str2)
print("id(str0)=",id(str0))
print("id(str1)=",id(str1))
print("id(str2)=",id(str2))
print("id(str0)==id(str1)?",id(str0)==id(str1))
print("id(str0)==id(str2)?",id(str0)==id(str2))

print("-"*num)

int0 = 1
int1 = int0
int1 = 3
print("id(int0)=",id(int0),"id(int1)=",id(int1),"id(int0)==id(int1)?",id(int0)==id(int1))
print(int0,int1)





