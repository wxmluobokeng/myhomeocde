'''
    作者：老萝卜
    功能：实现爬取QQ朋友圈
    2020-06-22：建立类,实现快捷登录

'''
from selenium import webdriver
import time

class qzone_class:
    Qzone_url = "https://i.qq.com/"
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driverstat=1     # 0:已注销；1:未登录；2:已登录；3:已登录朋友的QQ空间

    def driver_reload(self):
        '''
            激活webdrive,采用快捷方式登录QQ空间
        :return:
        '''
        self.driver.get(Qzone_url)
        time.sleep(3)
        self.driver.switch_to.frame("login_frame")
        # a = self.driver.find_element_by_xpath("//span[@class='img_out']")
        a = self.driver.find_element_by_xpath("/html/body/div[1]/div[4]/div[8]/div/a[1]/span[4]")
        a.click()
        time.sleep(2)
        self.driverstat=2

    def openqzone(self,qq_id):
        hpf = "https://user.qzone.qq.com/" + str(qq_id)
        # print_debugmsg("开始执行打开朋友的QQ空间")
        self.driver.get(hpf)
        time.sleep(1)
        self.driverstat=3

    def get_mainmenu(self):
        menu_dict= {}
        menu_list = self.driver.find_elements_by_xpath("//*[@id='menuContainer']/div/ul/li")  # 获取主菜单
        i=1
        for item in menu_list:
            menu_dict[item.text]=i
        return menu_dict

    def get_menu_xpath(self,menu_title):
        menu_list = self.driver.find_elements_by_xpath("//*[@id='menuContainer']/div/ul/li")  # 获取主菜单
        i=0
        li_num = 0
        for item in menu_list:
            i += 1
            if item.text == menu_title:
                li_num=i
                break
        if li_num==0:
            str_xpath="//*[@id='menuContainer']/div/ul/li[{}]/a".format(li_num)
        else:
            str_xpath=""
        return str_xpath

    def go_menucontent(self,menu_str):
        str_xpath=self.get_menu_xpath(menu_str)
        shuoshuo = self.driver.find_element_by_xpath(str_xpath)
        shuoshuo.click()
        time.sleep(2)



def main():
    pass

if __name__ == "__main__":
    main()

