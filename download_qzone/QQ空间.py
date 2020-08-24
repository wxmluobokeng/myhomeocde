#由于QQ空间的多样性,很多不兼容,请自己修改相关内容
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
chrome_options = Options()
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')#无头模式
driver= webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://i.qq.com/")
time.sleep(3)
driver.switch_to.frame("login_frame")
#a = driver.find_element_by_xpath("//span[@class='img_out']")
a = driver.find_element_by_xpath("/html/body/div[1]/div[4]/div[8]/div/a[1]/span[4]")
a.click()
time.sleep(2)
pf=input("输入爬取好友QQ号码")
hpf="https://user.qzone.qq.com/"+str(pf)
driver.get(hpf)
time.sleep(1)
shuoshuo=driver.find_element_by_xpath("/html/body/div[5]/div/div[5]/div[1]/div/div/ul/li[5]/a")
shuoshuo.click()
time.sleep(2)
filename=pf+".txt"
for i in range(1,7):
  u=0
  shuoshuoneirong=[]
  driver.switch_to.default_content()#最外表单
  driver.switch_to.frame("app_canvas_frame")#进入说说文字的表单
  time.sleep(3)
  
  shuoshuoneirong=driver.find_elements_by_xpath("//*[@class='content']")#说说文字部分提取
  for u in shuoshuoneirong:
     print(u.text)#打印说说
     with open (filename,"a",encoding="utf-8")as w:
       w.write(u.text)
       w.write("\n")
  time.sleep(3)
  shuoshuoneirong=driver.find_element_by_xpath('//*[@class="mod_pagenav_turn"]/input')
  shuoshuoneirong.send_keys(i)
  time.sleep(0.1)
  shuoshuoneirong.send_keys(Keys.ENTER)
  time.sleep(0.6)
  time.sleep(2)#等待加载
driver.quit()
