#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/18 18:32
# @Author : 老萝卜
# @File : 找链接.py
# @Software: PyCharm Community Edition

'''
 a = {"name":"123","data":{"result":[{"src":"python1"}, {"src":"python2"},{"src":"python3"}]}} 找到 python1/python2/python3
'''

# 方法一：
a = {"name":"123","data":{"result":[{"src":"python1"}, {"src":"python2"},{"src":"python3"}]}}
b= a["data"]["result"]              # 取出字典a中key="data"的值，再取其的key="result"的值
for item in b:                      # 遍历以字典为元素的列表
    print(item["src"])              # 打印字典key="src"的值


# 方法二：
print(a["data"]["result"][0]["src"])
print(a["data"]["result"][1]["src"])
print(a["data"]["result"][2]["src"])