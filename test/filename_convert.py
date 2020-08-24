#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/12 23:19
# @Author : 老萝卜
# @File : filename_convert.py
# @Software: PyCharm Community Edition
'''
    文件名中不能包含   < > / \ | : " * ?  这几个字符，将其转换成汉字符号
'''

def filename_convert(filename_old):
    filename_new =filename_old.replace("<","˂")
    filename_new =filename_new.replace(">", "˃")
    filename_new =filename_new.replace("/", "／")
    filename_new =filename_new.replace("\\", "∖")
    filename_new =filename_new.replace("|", "│")
    filename_new =filename_new.replace(":", "：")
    filename_new =filename_new.replace("\"", "“")
    filename_new =filename_new.replace("*","×")
    filename_new=filename_new.replace("?", "？")
    return filename_new

if __name__ == "__main__":
    filename_old ="< > / \\ | : \" * ? "
    # filename_old ="123?456"
    filename_new=filename_convert(filename_old)
    print(filename_old)
    print(filename_new)



