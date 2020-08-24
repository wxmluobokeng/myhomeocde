# -*- coding: utf-8 -*-
# @time :2020/7/23 16:20
# @Author:老萝卜
# @file:checkdir
# @Software:%{PRODUICT_NAME}


import os

# 在存的盘符上检查目录是否存，如果不存在就创建
def checkmkdir(path):
    # print(os.getcwd())    #当前工作目当
    print("path=",path)
    if not os.path.exists(path):
        if path[-1]=="\\":
            len0=path[:-1].rfind("\\")
        else:
            len0 = path.rfind("\\")
        checkmkdir(path[:len0])
        os.mkdir(path)



if __name__=="__main__":
    # checkmkdir("e:\\temp")
    path="e:\\temp\\pythontest\\汉服\\【仙气汉服】天淡天青，宿雨沾襟。\\"
    checkmkdir(path)
    # print(path[:-1])
    # path="E:"
    # # if path[-1]=="\\":
    # #     path1=
    # len0=path.rfind("\\")
    # print(path[:len0],len0)

    # if path.find(":") > 0 and os.path.exists(path[0] + ":"):
    #
    # checkmkdir()
