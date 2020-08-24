'''
    作者：老萝卜
    版本：1.0中
    功能：6月9日学习selenium爬虫
          1、sleenium框架、谷歌调用
          2、访问百度
          3、登录人人网，并查看cookies
          4、爬 后花园网文-经典语录
'''

from selenium import webdriver
from pandas import Series,DataFrame
import time
# webdrive_path = "D:\Program Files\Anaconda3\chromedriver.exe"               #绝对路径
# webdrive_path = "./chromedriver.exe"                                        #相对路径：当前路径
# webdriver.Chrome(webdriv_path)
driver = webdriver.Chrome()                                                            #chromedrive.exe保存在python目录下
# url = "http://www.baidu.com/"                                               #百度
# url = "http://www.renren.com/"                                              #人人网
url = "http://www.lovehhy.net/YuLu/Detail/"                                 #后花园网文-经典语录
driver.get(url)                                           #注意要加 http://
# driver.maximize_window()                                                     #窗口最大化
# driver.minimize_window()                                                     #窗口最小化
driver.save_screenshot("./baidu.png")                                        #截屏并保存

# 以下是：人人网登录，并查看cookies
# username = "18008471236"
# passwd = "lgtony"
# driver.find_element_by_id("email").send_keys(username)
# driver.find_element_by_id("password").send_keys(passwd)
# driver.find_element_by_id("login").click()
#
# #cookies : 登录状态
# cookies = driver.get_cookies()                          # 获取cookie
# print(cookies)
#
# # 字典推导式
# #  # print(cookies)结果如下：(每个数据进行了换行)
# #  [{'domain': '.renren.com', 'httpOnly': False, 'name': 'ick_login', 'path': '/', 'secure': False, 'value': '671efdf4-1fc0-4ed0-99ca-25a1af938ce1'},
# # {'domain': '.renren.com', 'httpOnly': False, 'name': 'taihe_bi_sdk_session', 'path': '/', 'secure': False, 'value': 'cde67ada9f7a4b77f88c489a9e788859'},
# # {'domain': '.renren.com', 'expiry': 1623311060, 'httpOnly': False, 'name': 'taihe_bi_sdk_uid', 'path': '/', 'secure': False, 'value': '39f1a9a27adeebfb1916a1097b88eced'},
# # {'domain': 'www.renren.com', 'httpOnly': False, 'name': 'JSESSIONID', 'path': '/', 'secure': False, 'value': 'abcsNI_bZat7h_Us9lDkx'},
# # {'domain': '.renren.com', 'expiry': 1622879054, 'httpOnly': False, 'name': '_r01_', 'path': '/', 'secure': False, 'value': '1'},
# # {'domain': '.renren.com', 'httpOnly': False, 'name': 'jebecookies', 'path': '/', 'secure': False, 'value': 'fdf5f87d-3a1f-48f8-9b1c-20a7f9b322f1|||||'},
# # {'domain': '.renren.com', 'expiry': 1592034254, 'httpOnly': False, 'name': 'depovince', 'path': '/', 'secure': False, 'value': 'GW'},
# # {'domain': '.renren.com', 'expiry': 1749455054, 'httpOnly': False, 'name': 'anonymid', 'path': '/', 'secure': False, 'value': 'kb91rqrd-mj5spu'}]
# #  # print(content)结果如下：(每个数据进行了换行)
# # {'ick_login': '671efdf4-1fc0-4ed0-99ca-25a1af938ce1',
# #  'taihe_bi_sdk_session': 'cde67ada9f7a4b77f88c489a9e788859',
# #  'taihe_bi_sdk_uid': '39f1a9a27adeebfb1916a1097b88eced',
# #  'JSESSIONID': 'abcsNI_bZat7h_Us9lDkx',
# #  '_r01_': '1',
# #  'jebecookies': 'fdf5f87d-3a1f-48f8-9b1c-20a7f9b322f1|||||',
# #  'depovince': 'GW',
# #  'anonymid': 'kb91rqrd-mj5spu'}
# # 只是将罗列的数据时行了导出，其它数据没有导出
#
# content = {dict["name"] : dict["value"] for dict in cookies }
# print(content)


#   // 根目录   [] 谓语  / 选择元素  @ 提取元素
# xpath_text = driver.find_element_by_xpath("//div[@id='endtext']").text
# xpath_a = driver.find_element_by_xpath("//h3/a")
# print(xpath_a.text,xpath_a.get_attribute("href"))

aaa = driver.find_element_by_xpath("//div[@id='endtext']")
print(type(aaa),aaa.text)

# bbb = driver.find_element_by_id("endtext")
# print(type(bbb),bbb.text)
#
# ccc = driver.find_elements_by_xpath("//div[@id='endtext']")
#
# for i,item in enumerate(ccc):
#     print("第{}条：{}".format(i+1,item.text))

# for i,item in enumerate(ccc):
#     print(i,type(item), item.text)

# i = 0
# for item in bbb:
#     print(i,item.text)
#     i += 1

# print(type(driver))
# dom = driver.find_element_by_xpath("//div[@id='endtext']")        #正确：  <div id="endtext">
# dom = driver.find_element_by_xpath("//dev[@id='footzoon']")       #报错：selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"xpath","selector":"//dev[@id='footzoon']"}
# #   <div class="cat_llb" id="footzoon">
dom = driver.find_element_by_id("footzoon")
# print("driver类型：",type(driver))
# print("dom类型：",type(dom))
dom_class = dom.find_elements_by_css_selector("a")[:5]
dom_title = dom.find_elements_by_xpath("//h3/a")[:5]
dom_text = dom.find_elements_by_xpath("//dev[@id='endtext']")[:5]
# print("dom_class类型：",type(dom_class),dom_class)

list_class_text=[]
list_class_url = []
for i,item in enumerate(dom_class):
    list_class_text.append(item.text)
    list_class_url.append(item.get_attribute("href"))

list_title_text = []
list_title_url = []
for i,item in enumerate(dom_title):
    list_title_text.append(item.text)
    list_title_url.append(item.get_attribute("href"))

list_text = []
for i,item in enumerate(dom_title):
    list_text.append(item.text)

# print("1: ",list_class_text)
# print("2: ",list_class_url)
# print("3: ",list_title_text)
# print("4: ",list_title_url)
# print("5: ",list_text)




# time.sleep(5)                                                               #延迟5秒
driver.quit()