'''
    功能：爬QQ朋友圏-相片
'''


def print_debugmsg(str_msg,para=1):
    '''
        打印调试信息
        :param massga: 调试信息
        :param para: 参数：0,不打印，1打印
    :return: 
    '''
    if para==1:
        print("时间：{};信息：{}".format(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),str_msg))

def printnote(str_msg,debug_para=0):
    '''
        打印备注信息
        :param massage: 备注信息
        :param debug_flag: 参数 0：打印，1：不处理
    :return:
    '''
    if debug_para==0:
        print("----------",str_msg,'----------')

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

printnote("设置浏览器参数并打开")
chrome_options = Options()
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')    #无头模式
driver= webdriver.Chrome(chrome_options=chrome_options)
# driver= webdriver.Chrome()
driver.get("https://i.qq.com/")
time.sleep(3)
printnote("选择登录方式:快捷登录")
driver.switch_to.frame("login_frame")
input("输入后继续：")
#a = driver.find_element_by_xpath("//span[@class='img_out']")
a = driver.find_element_by_xpath("/html/body/div[1]/div[4]/div[8]/div/a[1]/span[4]")
a.click()
time.sleep(2)

printnote("输入朋友QQ号，打开朋友的QQ空间")
pf=input("输入爬取好友QQ号码")
hpf="https://user.qzone.qq.com/"+str(pf)
print_debugmsg("开始执行打开朋友的QQ空间")
driver.get(hpf)
time.sleep(1)
print_debugmsg("打开朋友的QQ空间成功")
input("输入后下一步")
print_debugmsg("开始定位说说并打开")
# shuoshuo=driver.find_element_by_xpath("/html/body/div[5]/div/div[5]/div[1]/div/div/ul/li[5]/a")
# shuoshuo=driver.find_element_by_xpath("//*[@id='menuContainer']/div/ul/li[5]/a")            #说说
menu_list = driver.find_elements_by_xpath("//*[@id='menuContainer']/div/ul/li")
i = 1
for item in menu_list:
    print(i,":",item.text)
    if (item.text)=="说说":
        break
    i += 1

str_xpath="//*[@id='menuContainer']/div/ul/li[{}]/a".format(i)
print("str_xpath：",str_xpath)
shuoshuo=driver.find_element_by_xpath(str_xpath)            #说说
print(shuoshuo)
shuoshuo.click()
time.sleep(2)
# print_debugmsg("打开了说说")


input("输入后退出")

driver.quit()

