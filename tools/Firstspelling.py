# -*- coding: utf-8 -*-
# @time :2020/7/13 15:07
# @Author:老萝卜
# @file:Firstspelling
# @Software:%{PRODUICT_NAME}

'''
    使用前提：需要安装 pinyin 包
    firstspelling_chinese(str_soucce):返回所有汉字的首拼，并大写，其它字符保持不变
'''

import pinyin

def firstspelling_chinese(str_source):
    '''
        返回所有汉字的首拼，并大写，其它字符保持不变
    :param str_source:
    :return:
    '''
    result = pinyin.get_initial(str_source, delimiter="").upper()
