'''
    作者：老萝卜
    版本：1.0
    功能：爬取某个QQ空间的相片
        用selenium解析
        需提前登录QQ，选用点击方式
'''

from selenium import webdriver
from lxml import etree
import time


def open_qzone(url):
    driver = webdriver.Chrome()
    driver.get("https://i.qq.com/")
    # 在web 应用中经常会遇到frame 嵌套页面的应用，使用WebDriver 每次只能在一个页面上识别元素，对于frame 嵌套内的页面上的元素，直接定位是定位是定位不到的。
    # 这个时候就需要通过switch_to_frame()方法将当前定位的主体切换了frame 里。
    driver.switch_to.frame('login_frame')                       #login_frame 是ID值
    print("-----------选用快捷登录-------------------")
    a = driver.find_element_by_xpath("//div[@id='qlogin_list']/a/span[4]")
    a.click()
    time.sleep(1)
    return driver

# driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
# time.sleep(2)
# driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
# time.sleep(2)
# driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
# time.sleep(2)

def open_qzonephoto(url):
    driver = open_qzone(url)
    driver.get(url)
    # photo = driver.find_element_by_xpath("//*[@id='menuContainer']/div/ul/li/a[@title='相册']")
    photo = driver.find_element_by_xpath("//*[@id='menuContainer']/div/ul/li[3]/a")
    # photo = driver.find_element_by_xpath("/html/body/div[5]/div/div[5]/div[1]/div/div/ul/li[5]/a")
    # print(photo.text)
    # print(photo.get_attribute("href"))
    photo.click()
    time.sleep(2)




# page_text = driver.page_source
# print(type(page_text),page_text)
# tree = etree.HTML(page_text)
# #执行解析操作
# li_list = tree.xpath('//ul[@id="feed_friend_list"]/li')
# for li in li_list:
#     text_list = li.xpath('.//div[@class="f-info"]//text()|.//div[@class="f-info qz_info_cut"]//text()')
#     text = ''.join(text_list)
#     print(text+'\n\n\n')


# time.sleep(10)
# driver.quit()
#

def main():
    url = "https://user.qzone.qq.com/192149641"
    open_qzonephoto(url)

if __name__ == "__main__":
    main()