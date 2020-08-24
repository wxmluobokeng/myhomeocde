#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/19 19:22
# @Author : 老萝卜
# @File : module_20190717_v1.0.py
# @Software: PyCharm Community Edition


'''
    功能：淘宝登录（用微博登录，如果用淘宝帐号登录，需要验证，未解决）
    知识点：
        1、selenium :创建：调用谷歌、关闭、等待、关闭、销毁
        2、基于类的编程:重写构造方法，定义类的属性、类的方法
        3、使用密码配置文件:将用户名、密码写到一个文件，导出此文件，再用文件名.变量名引用
'''

# 从selenium框架中导入浏览器驱动
from selenium import webdriver

# 让浏览器在执行过程中等待加载数据
from selenium.webdriver.support.ui import WebDriverWait

# 时间包(与上面功能相似，本次用两种方法等待)
import time

# 淘宝帐号的配置文件(保存帐号和密码的文件)
import settings

# 基于类的编程

class Taobao_Info:
    # 重写构造方法
    def __init__(self):
        # 让浏览器自动的指定页面,声明变量
        url = "https://login.taobao.com/member/login.jhtml"   # 淘宝登录url

        # 声明属性   在类后面可以引用
        self.url= url

        # 调用浏览器去驱动去控制浏览器
        # self.brower= webdriver.Chrome(executable_path="驱动的完整路径")  # 定义驱动的完整路径,不要此参数，驱动需要拷贝到python目录下
        self.brower= webdriver.Chrome()

        # 让浏览器等待加载，时长为10秒
        self.wait = WebDriverWait(self.brower,10)

    # 登录淘宝的类方法
    def login(self):
        # 打开淘宝登录页
        self.brower.get(self.url)

        # 找到密码登录按钮
        if self.brower.find_element_by_link_text("密码登录"):    # 找到网页中控件
            self.brower.find_element_by_link_text("密码登录").click()

        if self.brower.find_element_by_xpath('//*[@id="fm-login-id"]'):
            taobao_user = self.brower.find_element_by_xpath('//*[@id="fm-login-id"]')
            taobao_user.send_keys(settings.user_taobao)
            print("settings.user_taobao=",settings.user_taobao)

        if self.brower.find_element_by_xpath('//*[@id="fm-login-password"]'):
            taobao_pwd = self.brower.find_element_by_xpath('//*[@id="fm-login-password"]')
            taobao_pwd.send_keys(settings.pwd_taobao)
            print("settings.pwd_taobao=", settings.pwd_taobao)

        # 找到登录按钮并点击
        # if self.brower.find_element_by_link_text("登录"):
        #     self.brower.find_element_by_link_text("登录").click()
        if self.brower.find_element_by_xpath('//*[@id="login-form"]/div[4]/button'):
            self.brower.find_element_by_xpath('//*[@id="login-form"]/div[4]/button').click()

        # # 用微博登录
        # # 找到微博登录按钮，xpath是一种网面选择器，通过xpath能够找到网页中的数据及控件
        # if self.brower.find_element_by_xpath("//*[@id='login-form']/div[5]/a[1]"):          #选择微博登录
        #     self.brower.find_element_by_xpath("//*[@id='login-form']/div[5]/a[1]").click()
        #
        # # 找到微博帐号输入框
        # if self.brower.find_element_by_xpath("//*[@id='pl_login_logged']/div/div[2]/div/input"):
        #     weibo_user= self.brower.find_element_by_xpath("//*[@id='pl_login_logged']/div/div[2]/div/input")
        #     weibo_user.send_keys(settings.user_weibo)
        #
        # # 找到微博密码输入框
        # if self.brower.find_element_by_xpath("//*[@id='pl_login_logged']/div/div[3]/div/input"):
        #     weibo_pwd=self.brower.find_element_by_xpath("//*[@id='pl_login_logged']/div/div[3]/div/input")
        #     weibo_pwd.send_keys(settings.pwd_weibo)
        #
        # # 找到登录按钮并点击
        # if self.brower.find_element_by_link_text("登录"):
        #     self.brower.find_element_by_link_text("登录").click()

if __name__ == "__main__":
    Taobao_Info().login()
    time.sleep(0)
    Taobao_Info().brower.close()
    Taobao_Info().brower.quit()