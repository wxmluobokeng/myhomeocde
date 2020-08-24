# -*- coding: utf-8 -*-
# @time :2020/8/18 15:44
# @Author:老萝卜
# @file:1
# @Software:%{PRODUICT_NAME}


from selenium import webdriver

from selenium.webdriver.common.keys import Keys

import time, requests, urllib.request, re, time, os, socket

from bs4 import BeautifulSoup

from selenium.webdriver.chrome.options import Options

sysdate_compact = time.strftime('%Y%m%d', time.localtime(time.time()))

def save_text(filename,data,oprtype="a",encode="utf-8"):
    with open(filename,oprtype,encoding=encode) as file:
        file.write(data)



find = "邓紫棋"

# find = input("下载那个歌手")

try:

    chrome_options = Options()

    chrome_options.add_argument("--window-size=1920,1080")

    # chrome_options.add_argument('--headless')

    # chrome_options.add_argument('--disable-gpu')  # 无头模式

    driver = webdriver.Chrome(chrome_options=chrome_options)

except:

    pass

headers = {

    'Referer': 'http://music.163.com/',

    'Host': 'music.163.com',

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',

    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', }

driver.get("https://music.163.com/")

time.sleep(0.2)

driver.find_element_by_id("srch").send_keys(find)

driver.find_element_by_id("srch").send_keys(Keys.ENTER)

time.sleep(0.2)

save_text(f"music.163.com.{sysdate_compact}_1.html",driver.page_source,"w")
# driver.switch_to_frame(driver.find_element_by_xpath('//iframe[@id="g_iframe"]'))

driver.switch_to.frame("g_iframe")

save_text(f"music.163.com.g_iframe.{sysdate_compact}.html",driver.page_source,"w")

zhao1 = driver.find_element_by_xpath(

    '/html/body/div[3]/div/div[2]/ul/li[1]/a/em')


print("zhao1=",zhao1,"type(zhao1)=",type(zhao1))
zhao1.click()

time.sleep(1)

save_text(f"music.163.com.{sysdate_compact}_2.html",driver.page_source,"w")

zhao2 = driver.find_element_by_xpath(

    '/html/body/div[3]/div/div[2]/ul/li[2]/a/em')

zhao2.click()

time.sleep(1)

save_text(f"music.163.com.{sysdate_compact}_3.html",driver.page_source,"w")

zhao3 = driver.find_element_by_xpath("//span[@class='msk']")

zhao3.click()

save_text(f"music.163.com.{sysdate_compact}_4.html",driver.page_source,"w")

urlnow = driver.current_url

print("urlnow=",urlnow)

give = re.findall("\d+", urlnow)

print("give=",give)

give.remove("163")

artistid = give[0]  # 歌单id提取出来了哈哈哈

print(artistid)

driver.quit()

print("歌手id为", artistid)

l = []

l.append(artistid)

socket.setdefaulttimeout(20)

filewz = os.getcwd()

for i in l:

    os.chdir(filewz)

    http = "https://music.163.com/artist?id=" + str(i)  # i是歌单id

    play_url = http

    s = requests.session()

    response = s.get(play_url, headers=headers, timeout=30).content

    responsetext = s.get(play_url, headers=headers, timeout=30).text

    namere = '"title": ".+",'

    gsname = re.search(namere, responsetext).group()

    gsname = re.sub('"title": "', '', gsname)

    gsname = re.sub('",', '', gsname)

    try:

        if not os.path.isdir(gsname):

            os.mkdir(gsname)  # 如果文件不存在,则建立文件夹

            os.chdir(gsname)

        else:

            os.chdir(gsname)  # 如果文件夹存在，载入文件夹

    # 因为可能有文件夹python无法识别,所有另考虑

    except:

        gsname = "未知歌手"

        if not os.path.isdir(gsname):

            os.mkdir(gsname)

            os.chdir(gsname)

        else:

            os.chdir(gsname)

    s = BeautifulSoup(response, 'lxml')

    main = s.find('ul', {'class': 'f-hide'})

    print(main.find_all('a'))
    lists = []

    for music in main.find_all('a'):
        list = []

        musicUrl = 'http://music.163.com/song/media/outer/url' + music['href'][5:] + '.mp3'


        musicName = music.text

        list.append(musicName)

        list.append(musicUrl)

        lists.append(list)

    print("lists=",lists)

    # for i in lists:
    #
    #     url = i[1]
    #
    #     name = i[0] + ".mp3"
    #
    #     try:
    #
    #         print('正在下载', name)
    #
    #         urllib.request.urlretrieve(url, filename=name)
    #
    #         print('下载成功')
    #
    #     except:
    #
    #         print('下载失败')
    #
