'''
    功能:下载QQ表情包
'''

import requests
import re

url= "https://qq.yh31.com/zjbq/2920180.html"

html=requests.get(url)
print(html.text)

# str1="123123<img src='/image/ontop3.gif' alt='123'>\n123123<img src='/image/ontop4.gif' alt='1253'>"
# str_regular= re.compile(r"<img src='(.*?)' alt=.*? >")
str_regular= re.compile(r'<img border="0" .* src="(.*)">')


# img_list = re.findall(str_regular,html.text)
img_list = str_regular.findall(html.text)
# img_list = str_regular.findall(str1)
print(img_list)