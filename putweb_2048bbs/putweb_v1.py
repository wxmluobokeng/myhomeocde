'''
     功能：爬取主页
'''

# 1、导入框架
import requests

# 2、输入url
url = "http://kuihua2020.com/"
headers ={
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.13 Safari/537.36"
}
# 3、获取数据
html = requests.get(url,headers=headers)
print(html.text)
# 4、分析数据

# 5、保存数据