'''
     功能：爬取小说列表
     版本：2.0
     主要实现：通过selenium 访问网页

'''

# 1、导入框架
from selenium import webdriver

# 2、输入url
url = "http://kuihua2020.com/v/2/renqishunv/"
# headers ={
#     "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.13 Safari/537.36",
#     "Referer": "http://kuihua2020.com/"
# }
headers ={
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.13 Safari/537.36"
}

referer = "http://kuihua2020.com/"              #网站链接用的是相对链接，需要拼接



# 3、获取数据
driver = webdriver.Chrome()
driver.get(url)
# print(response.text)

# 4、分析数据
dom = driver.find_element_by_id("blog-post")            # 找到主体部分
dom_class = dom.find_elements_by_css_selector("a")      # 找到分类

list_text = []
list_url = []
for item in dom_class:
    list_text.append(item.text)
    list_url.append(item.get_attribute("href"))
    print(item.get_attribute("href"),item.text)
