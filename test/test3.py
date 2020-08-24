'''
    Python中矩阵转置，求逆和一些运算
    https://blog.csdn.net/Maple_XW/article/details/106166151?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-4.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-4.nonecase
    将字符串数组转换成二维数组
    https://www.jb51.net/article/137685.htm
    numpy数组，矩阵和列表之间的相互转换
    https://blog.csdn.net/StriveHeisenberg/article/details/89812714?utm_medium=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase
'''

import numpy as np


# np.vstack()   输入数组必须保持尺寸维度一致，即shape属性一致！
# ValueError: all the input array dimensions except for the concatenation axis must match exactly
# def ret_matrix(strlist):
#     result = [[],[]]
#     np.vstack((result,strlist))
#     return result

with open(".\\web_test3.txt","r",encoding='utf8') as file:
    str1 = file.read()
strlist = str1.split("\n")

print(len(strlist),strlist)

for i in range(len(strlist)):
    strlist[i] = strlist[i].split()

print(strlist)
array_0 = np.array(strlist)
print(type(array_0))
matrix_0 = np.mat(strlist)
print(type(matrix_0))

matrix_1 = matrix_0.T     #   transpose(matrix_0)
print(matrix_1)


a = np.matrix([[1,2,3],[4,5,6][7,8]])
b = a.T
print(a)
print(b)

