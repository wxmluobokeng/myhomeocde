# -*- coding: utf-8 -*-
# @time :2020/8/6 17:36
# @Author:老萝卜
# @file:1
# @Software:%{PRODUICT_NAME}


import requests
import re

url='http://www.nipic.com/photo/jingguan/ziran/index.html'

data = requests.get(url).text

print("网站源码", data)

r'data-src="(.*?.jpg)"'

# pa = re.compile(r'data-src="(.*?.jpg)"')

ma = re.findall(r'data-src="(.*?.jpg)"', data)

print(ma)

# i=0
# for image in ma:
#     i += 1
#
#     image = requests.get(image).content
#
#     with open('imgs/' + str(i) + '.jpg', 'wb') as f:
#         f.write(image)
