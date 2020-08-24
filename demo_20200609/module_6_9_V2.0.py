'''
    作者：老萝卜
    版本：2.0中
    日期：2020.6.10 夜
    功能：6月9日学习selenium爬虫
          1、爬 后花园网文-经典语录，解析（仅一页）
          2、采用pandas.dataframe 结构 保存数据
          3、数据保存到cvs文件
     局限性：
          1、如果存在数据缺项时，不进行清洗，此方法用不成，每一列个数相同才行
          2、部分数据未抓取，如时间、点击次数： <a href="/Yulu/Detail/XLJT/" class="catname">心灵鸡汤</a>　2019-07-10 15:31:00　　Click:1461<div class="bg_t1"></div>
          3、是否有更优的解析方法
          4、CSV列名能否按规定顺序保存：目前没有按赋值顺序， class_text,class_url,title_text,title_url,text
'''

from selenium import webdriver
import  pandas  as  pd
import time
driver = webdriver.Chrome()                               #chromedrive.exe保存在python目录下
url = "http://www.lovehhy.net/YuLu/Detail/"               #后花园网文-经典语录
driver.get(url)                                           #注意要加 http://


# content = {dict["name"] : dict["value"] for dict in cookies }
# print(content)


#   // 根目录   [] 谓语  / 选择元素  @ 提取元素
dom = driver.find_element_by_id("footzoon")                                 #找到主体部分
# dom_class = dom.find_elements_by_css_selector("a")                        #找到分类
dom_class = dom.find_elements_by_css_selector("a[class='catname']")         #找到分类
dom_title = dom.find_elements_by_xpath("//h3/a")                            #找到标题
dom_text = dom.find_elements_by_xpath("//div[@id='endtext']")               #找到正文

list_class_text=[]
list_class_url = []
for i,item in enumerate(dom_class):
    list_class_text.append(item.text)
    list_class_url.append(item.get_attribute("href"))
    # print(item.text,item.get_attribute("href"))

list_title_text = []
list_title_url = []
for i,item in enumerate(dom_title):
    list_title_text.append(item.text)
    list_title_url.append(item.get_attribute("href"))

list_text = []
for i,item in enumerate(dom_text):
    list_text.append(item.text)
    # print(item.text)

print(len(list_class_text))
print(len(list_class_url))
print(len(list_title_text))
print(len(list_title_url))
print(len(list_text))

dict1 = {"class_text":list_class_text,"list_class_url":list_class_url,"list_title_text":list_title_text,"list_title_url":list_title_url,"list_text":list_text}
data1 = pd.DataFrame(dict1)
# print(dict1)
# print(data1)

csv_path = "./后花园网文_经典语录.csv"
data1.to_csv(csv_path)

# time.sleep(5)                                                               #延迟5秒
driver.quit()