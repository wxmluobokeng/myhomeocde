# -*- coding: utf-8 -*-
# @time :2020/7/10 17:28
# @Author:老萝卜
# @file:homework_lesson3_2
# @Software:%{PRODUICT_NAME}

'''
   lesson 3 课后作业：第三题 ：print()语句练习，⽤两种⽅式打印 hello,python
'''

str0="python"
str1="java"

# 方法一： 直接输出
print("python , java")
print(str0+" , "+str1)

# 方法二： 函数输出
print(str0,",",str1)

# 方法三 ： 用替换符
print("%s , %s"%(str0,str1))

#方法四： 用format
print("{} , {}".format(str0,str1))
print("{1} , {0}".format(str1,str0))

# 方法五： f+str
print(f"{str0} , {str1}")

#方法六: join
str_list= ["python "," java"]
print(",".join(str_list))

