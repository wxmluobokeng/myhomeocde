#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/8/22 23:04
# @Author : 老萝卜
# @File : data_gif.py
# @Software: PyCharm Community Edition

'''
    将数据走势转换成 gif 动图，类似
    实现方式：
    1、没有爬取数据，直接随机生成正态分布的数据
    2、数据处理规则： 当前数据前n项数据的和,S(n)=S(n-1)+a(n)
    3、每次根据当前数据和历史数据生成一张图片，并读取来，保存到数据列表中，最后合成一个gif
    4、生成图片的方法：
       a. 定义一个画布，
       b.设置一个网格大小和图象编号
       c.生成图象
       d.保存图象到文件中（生成后就读取出来保存到列表中，所以文件名相同，直接覆盖）
'''


import imageio
import matplotlib.pyplot as plt  # 数据分析
import numpy  as np  # 利用正态分布生成演示数据

# 准备数据
data = np.random.normal(size=40)  # 生成40条数据 （正态分布的数据）
print("data=",data)

sum=0 # 初始数据
index=[]
img_list=[]
for i in data:
    # 设置画布大小,元祖类型（长，高），实际象素大小是数值*100
    fig = plt.figure(figsize=(16, 9))
    #选图：111  1*1 的网格， 1 第一子图，如果多图，按实际数值
    ax=fig.add_subplot(111)

    # 数据处理
    sum+=i      # 后一个数=前面数之和 + 当前值
    # 数据可视化
    index.append(sum)
    ss=len(index)
    ax.plot(range(ss),index)
    #保存为图片
    plt.savefig("t.png")
    plt.close()
    #读取图片信息
    im= imageio.imread("t.png")
    img_list.append(im)

# 合成并保存为 ： 文件名，图片内容列表，图片类型，时间间隔（秒）
imageio.mimsave("123.gif", img_list, "gif", duration=1)





