# -*- coding: utf-8 -*-
# @time :2020/8/17 10:24
# @Author:老萝卜
# @file:syspara
# @Software:%{PRODUICT_NAME}

import os

oprtype="url"   #  url 或 txt
oprtype="txt"
# syspath=os.getcwd()
# print(syspath)
# readpath=os.getcwd()      缺省路径：当前工作目录os
# basepath="E:\\DevProjects\\python-course\\"
# basepath="E:\\python-course\\"
# savepath=""

# E:\\DevProjects\\python-course\\test_pic\\vmgirls\\www.vmgirls.com.2020-08-17.html
savepath="E:\\DevProjects\\python-course\\test_pic\\vmgirls\\"
url=""
readpath="E:\\DevProjects\\python-course\\test_pic\\vmgirls\\www.vmgirls.com.2020-08-17.html"
savepath="E:\\DevProjects\\python-course\\test_pic\\vmgirls\\www.vmgirls.com.2020-08-17_body.html"

def checksyspara():
    result=""
    if oprtype=="url":
        if len(url)<=4:
            result="url设置有误"
    elif oprtype=="txt":
        if len(readpath)<=3 and not os.path.isfile(readpath):
            result="待重排文件不存在"
    return result


# def main():
#     ret=checksyspara()
#     if ret!="":
#         print(ret)
#         return
#
#
# if __name__=="__main__":
#     main()