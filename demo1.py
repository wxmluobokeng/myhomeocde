'''
    作者:老萝卜
    版本:1.0
    日期：2010.5.26
    功能：爬京东商品列表
'''

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time


def spider():
    driver =webdriver.Chrome()
    driver.get("http://www.jd.com/")
    input_tag=driver.find_element_by_id("key")
    input_tag.send_keys("口罩")
    input_tag.send_keys(Keys.ENTER)
    time.sleep(5)
    get_doods(driver)

def show_content(variable_name):
    print('变量类型：{}'.format(type(variable_name)))
    print('变量值：{}'.format(variable_name))
    print()

def get_doods(driver):
    goods=driver.find_elements_by_class_name('gl-item')

    # print(type(goods))
    # print(goods)
    for good in goods:
        # print(type(good))
        # print()
        link1=good.find_element_by_class_name('p-name').text
        show_content(link1)
        # link=good.find_element_by_tag_name('a').get_attribute("href")
        # l1=good.find_elenment_by_css_selector(".p-price")
        # print(type(li))
        # print(li)

        # name=good.find_element_by_css_selector('.p-name em').text.replace("\n","")
        # price=good.find_element_by_css_selector(".p-price i").text
        # commit=good.find_element_by_css_selector(".p-commit a").text
        # print("link:%s,name:%s,价格：%s,评价：%s"%(link,name1,price,commit1))

def main():
    spider()

if __name__=="__main__":
    main()


