#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/8/15 13:41
# @Author : 老萝卜
# @File : demo_echarts_conv.py
# @Software: PyCharm Community Edition

'''
    2020-8-12录播： 逻辑教育anny老师《》
    主要功能：
    1、抓取全国情数据
    2、数据可视化地图绘制

'''

import json
import requests
import jsonpath
from pyecharts.charts import Map            # 给制地图
from pyecharts import options as opts       # 初始化配置
# from dome1 import nameMap

# 1、抓取全国情数据
url = 'https://api.inews.qq.com/newsqa/v1/automation/foreign/country/ranklist'

reqs = requests.post(url).text      # 请求方式：get   post   获取源代码， 数据在源代码中
# print(reqs)
data=json.loads(reqs)               # 字符串 ——————  字典
# print(data)
# print(data["data"])

# 提取国家名和国家病死率   $ 表示最外层的{}  .. 表示模糊匹配
name=jsonpath.jsonpath(data,"$..name")      # 所有的内容，提取内容的共同规则
confirm=jsonpath.jsonpath(data,"$..confirm")
# name1=[item["name"]  for item in data["data"] ]

a= list(zip(name,confirm))      # 生成输入数据
print(a)

# nameMap={}

# 2、数据可视化地图绘制
# 需要设置：地图大小  标题  颜色  数据
mapset=opts.InitOpts(width='1200px',height='600px')
map_ = Map(opts.InitOpts(width='1200px',height='600px')).add(series_name="世界各国的病死率",
                                                            data_pair=a,        # 输入数据
                                                            maptype="world",    # 地图类型:世界地图
                                                            # name_map=nameMap,   # 添加映射，自定义地区的名称映射
                                                            is_map_symbol_show=False    # 不显示标记点
)
# 设置系列配置项
map_.set_series_opts(label_opts=opts.LabelOpts(is_show=False))      # 不显示国家名称

map_.set_global_opts(title_opts=opts.TitleOpts(title="国外疫情的情况"),
                     visualmap_opts=opts.VisualMapOpts(max_=6000000,is_piecewise=True))

map_.render("国外疫情情况.html")
