# -*- coding: utf-8 -*-
# @time :2020/7/30 17:11
# @Author:老萝卜
# @file:封装的引入-times_2
# @Software:%{PRODUICT_NAME}

# 尝试定义一个车类
# 属性 name color
# 方法 run() loudspeaker()
class Car():
    # name = 'xxx'
    # color = 'xxx'
    def __init__(self,name,color):
        self.name = name
        self.color = color
    def run(self):
        print('汽车开始跑了.....')
    def loudspeaker(self):
        print('%s 滴滴滴滴........'%self.name)


c = Car('大奔','白色')
print(c,c.name,c.color)
c.run()
c.loudspeaker()
# <__main__.Car object at 0x0000000002887CC0> 大奔 白色
# 汽车开始跑了.....
# 大奔 滴滴滴滴........


c.name="法拉利"
c.color="黑白溜秋"

c.loudspeaker()
print(c.color)
# 法拉利 滴滴滴滴........
# 黑白溜秋

