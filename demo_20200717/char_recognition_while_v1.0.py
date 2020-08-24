#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/26 19:47
# @Author : 老萝卜
# @File : char_recognition__whilev1.0.py
# @Software: PyCharm Community Edition

'''


百度AIP安装：pip install baidu-aip -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
'''

import keyboard  # pip install keyboard  # 键盘处理
from PIL import ImageGrab  # pip install pillow    # 图像处理
from aip import AipOcr  # pip install baidu-aip -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
import time

exit_flag = True
while exit_flag:
    # 1、截图（监控键盘）
    # 1.2保存截图
    keyboard.wait(hotkey="f1")  # 利用 Snipaste 软件 的 F1键  进行截图，

    keyboard.wait(hotkey="ctrl+c")  # 将截图内容复制到剪贴板
    # print("222222")
    time.sleep(0.1)  # 必须有时间延迟，否则只能拿到剪贴板中上一次内容

    # keyboard.wait(hotkey="ctrl+alt+esc")
    # 2、保存图片
    img = ImageGrab.grabclipboard()
    img.save("example.jpg")

    """ 你的 APPID AK SK """
    APP_ID = '21627672'
    API_KEY = 'Fa4YKIsucvWA0uQnPgtSTcGZ'
    SECRET_KEY = '7qHBS0Vtclv4cl64krTr2eOxtQ0C4A2a'

    # APP_ID = '17732244'
    # API_KEY = 'K32y2jSOxgkq6LSynoG5MStB'
    # SECRET_KEY = 'ASkTsum1Zt8kTFQGABly2FrHviGFkUIA'


    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

    # def get_file_content(filePath):
    #     with open(filePath, 'rb') as fp:
    #         return fp.read()
    #
    # image = get_file_content('example.jpg')
    #
    # """ 调用通用文字识别, 图片参数为本地图片 """
    # client.basicGeneral(image);

    with open('example.jpg', "rb") as file:
        image = file.read()
    text_res = client.basicGeneral(image);
    # print(text_res)
    text_result = text_res["words_result"]
    text_list = []
    for item in text_result:
        text_list.append(item["words"])
    print(text_list)
    with open(".\\ocr1.txt", "a+", encoding="utf-8") as file1:
        file1.write("\n".join(text_list) + "\n\n")

    # keyboard.wait(hotkey="ctrl+alt+esc")
