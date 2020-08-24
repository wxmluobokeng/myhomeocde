#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/8/16 16:56
# @Author : 老萝卜
# @File : demo2.py
# @Software: PyCharm Community Edition

'''
    CSDN fun_always 《用PyEcharts实现数据可视化快速上手指南》
    https://blog.csdn.net/fun_always/article/details/89854150
    CSDN Lida_wu 《python实现省市热力地图》
    https://blog.csdn.net/u013004700/article/details/106766278

'''

from pyecharts.charts import Map
from pyecharts import options as opts
from pyecharts.globals import ThemeType
from pyecharts.faker import Faker

value = [115.4,121.6,122,116,123.3,110.4,118.4,116.8,114.3,
         113.2,111.8,116.8,113.4,113,121.3,118.7,119,117.6,113.8,
         115.1,114.1,115.2,112.6,114.8,120.2,118.2,119.8,114.7,115.4,
         114.6,112.7]
attr = ['甘肃','广东', '广西','贵州','海南',
        '河南','湖北', '湖南','宁夏','青海',
        '陕西','四川', '西藏','新疆','云南',
        '重庆','北京', '天津','河北','山西','内蒙古',
        '辽宁','吉林', '黑龙江','上海','江苏','浙江','安徽','福建'
        ,'江西','山东']
sequence = list(zip(attr,value))


def map_visualmap(sequence, year) -> Map:
    c = (
        Map(opts.InitOpts(width='1200px',height='600px'))               #  opts.InitOpts() 设置初始参数:
            .add(series_name=year, data_pair=sequence, maptype="china" )       # 系列名称(显示在中间的名称 )、数据 、地图类型
            .set_global_opts(
            title_opts=opts.TitleOpts(title="地图"),
            visualmap_opts=opts.VisualMapOpts(max_=130, min_=95),
        )
    )
    return c


map = map_visualmap(sequence, '1993')
map.render(path='./test.html')




# from pyecharts.charts import Map
# from pyecharts import options as opts
# from pyecharts.globals import ThemeType

value = ['78', '17', '101', '95', '36', '16', '19', '23', '35']
attr = ['福州市', '莆田市', '泉州市', '厦门市', '漳州市', '龙岩市', '三明市', '南平市', '宁德市']
sequence = list(zip(attr, value))


def map_visualmap(sequence, year) -> Map:
    c = (
        Map()
            .add(year, sequence, "福建", )
            .set_global_opts(
            title_opts=opts.TitleOpts(title="地图"),
            visualmap_opts=opts.VisualMapOpts(max_=101, min_=16),
            #             visualmap_opts=opts.VisualMapOpts(max_=101,range_color=["lightskyblue", "yellow", "orangered"]),
        )
    )
    return c


map = map_visualmap(sequence, '2020')
map.render(path='./test1.html')

# from pyecharts.charts import Map
# from pyecharts import options as opts
# from pyecharts.globals import ThemeType

value = ['78', '17', '101', '95', '36', '16', '19', '23', '35']
attr = ['福州市', '莆田市', '泉州市', '厦门市', '漳州市', '龙岩市', '三明市', '南平市', '宁德市']
sequence = list(zip(attr, value))


def map_visualmap(sequence, year) -> Map:
    c = (
        Map()
            .add(year, sequence, "福建",is_map_symbol_show=False )        # 系列名称(显示在中间的名称 )、数据 、地图类型,不显示标记点
            .set_global_opts(
            title_opts=opts.TitleOpts(title="地图"),
            #             visualmap_opts=opts.VisualMapOpts(max_=101,min_=16),
            visualmap_opts=opts.VisualMapOpts(max_=101,min_=16, range_color=["lightskyblue", "yellow", "orangered"],is_piecewise=True),  # 范围 最大值 、最小值 、组件过渡颜色 、 是否为分段型
        )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))      # 不显示系列名称
    )
    return c


map = map_visualmap(sequence, '2020')
map.render(path='./test2.html')



data_hubei=[list(z) for z in zip(Faker.guangdong_city, Faker.values())]

print(data_hubei)

c = (
    Map()
    .add("商家A", data_hubei, "广东")
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Map-广东地图"), visualmap_opts=opts.VisualMapOpts()
    )
    .render("map_guandong.html")
)
