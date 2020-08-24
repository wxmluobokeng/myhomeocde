'''
    作者：老萝卜
    版本：1.0
    功能：爬取某个QQ空间的主面
        用selenium解析
    新增功能：需提前登录QQ，选用点击方式
'''

from selenium import webdriver
from lxml import etree
import time

# url = "https://i.qq.com/"
url = "https://user.qzone.qq.com/192149641"
driver = webdriver.Chrome()
driver.get(url)
# 在web 应用中经常会遇到frame 嵌套页面的应用，使用WebDriver 每次只能在一个页面上识别元素，对于frame 嵌套内的页面上的元素，直接定位是定位是定位不到的。
# 这个时候就需要通过switch_to_frame()方法将当前定位的主体切换了frame 里。
driver.switch_to.frame('login_frame')                       #login_frame 是ID值
# print("-----------选用帐号登录-------------------")
# # 帐号登录，需要图像验证
#  driver.find_element_by_id('switcher_plogin').click()
# qq_id="344977148"
# qq_pwd="wzh20080122"
# driver.find_element_by_id('u').send_keys(qq_id)  #这里填写你的QQ号
# driver.find_element_by_id('p').send_keys(qq_pwd)  #这里填写你的QQ密码
# driver.find_element_by_id('login_button').click()
# time.sleep(2)

print("-----------选用快捷登录-------------------")
# # 快捷登录
a = driver.find_element_by_xpath("//div[@id='qlogin_list']/a/span[4]")
a.click()
time.sleep(2)


driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
time.sleep(2)
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
time.sleep(2)
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
time.sleep(2)

print("----------主人动态内容区----------")
driver.switch_to.frame('QM_Feeds_Iframe')                       #login_frame 是ID值
page_text = driver.page_source
print(type(page_text),page_text)



# page_text = driver.page_source
# print(type(page_text),page_text)
# tree = etree.HTML(page_text)
# #执行解析操作
# li_list = tree.xpath('//ul[@id="feed_friend_list"]/li')
# for li in li_list:
#     text_list = li.xpath('.//div[@class="f-info"]//text()|.//div[@class="f-info qz_info_cut"]//text()')
#     text = ''.join(text_list)
#     print(text+'\n\n\n')


time.sleep(10)
driver.quit()

