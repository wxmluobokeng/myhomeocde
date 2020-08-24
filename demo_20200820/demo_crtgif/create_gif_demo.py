#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/8/22 22:38
# @Author : 老萝卜
# @File : create_gif_demo.py
# @Software: PyCharm Community Edition

import imageio

list_img = ["1.jpg", "2.jpg", "3.jpg"]

img_list = []
for i in list_img:
    # 根据文件路径读取图片信息
    im = imageio.imread(i)
    # print("type(im)=",type(im))
    img_list.append(im)
# print(img_list)

# 合成并保存为 ： 文件名，图片内容列表，图片类型，时间间隔（秒）
imageio.mimsave("girl.gif", img_list, "gif", duration=1)
