#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/8/15 17:12
# @Author : 老萝卜
# @File : demo1.py
# @Software: PyCharm Community Edition

'''
    CSDN zerow__ 《python 利用echarts画地图(热力图)(世界地图，省市地图，区县地图)》
    https://blog.csdn.net/zerow__/article/details/88785759?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param

'''

from pyecharts.charts import Map
from pyecharts import options as opts       # 初始化配置
# value = [95.1, 23.2, 43.3, 66.4, 88.5]
# attr = ["China", "Canada", "Brazil", "Russia", "United States"]
# map0 = Map("世界地图示例", width=1200, height=600)
# map0.add("世界地图", attr, value, maptype="world", is_visualmap=True, visual_text_color='#000')
# map0.render(path="世界地图.html")


value = [95.1, 23.2, 43.3, 66.4, 88.5]
attr = ["China", "Canada", "Brazil", "Russia", "United States"]
a = list(zip(attr,value))
map0=Map(opts.InitOpts(width='1200px',height='600px')).add(series_name="世界地图",data_pair=a,maptype="world",is_map_symbol_show=False )

map0.set_series_opts()
# map_.set_global_opts(title_opts=opts.TitleOpts(title="国外疫情的情况"),
#                      visualmap_opts=opts.VisualMapOpts(max_=6000000,is_piecewise=True))
map0.render("测试1.html")



districts=['白云区', '从化区', '番禺区', '海珠区', '花都区', '黄埔区', '荔湾区', '南沙区', '天河区', '越秀区', '增城区']
value = [ 1, 2, 3,4, 5,6,7,8,9,10, 11]
a= list(zip(districts,value))
map1 = Map(opts.InitOpts(width='1200px',height='600px'))
map1.add(maptype='广州',
        data_pair=a,
        series_name="Map地图示例",is_map_symbol_show=False
       ).set_global_opts(title_opts=opts.TitleOpts(title="广州地图"),visualmap_opts=opts.VisualMapOpts(max_=11,min_=1, range_color=["lightskyblue", "yellow", "orangered"],is_piecewise=True))
map1.set_series_opts(label_opts=opts.LabelOpts(is_show=False))      # 不显示系列名称
map1.render("测试2.html")
