#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/8/8 11:16
# @Author : 老萝卜
# @File : 操作二进制文件-times_3.py
# @Software: PyCharm Community Edition

# filename="Kalimba.mp3"
# with open(filename) as file:
#     print(file.read())
# # Traceback (most recent call last):
# #   File "E:/python-course/homework_zero_class/lesson16/操作二进制文件-times_1.py", line 10, in <module>
# #     print(file.read(100))
# # UnicodeDecodeError: 'gbk' codec can't decode byte 0xd1 in position 165: illegal multibyte sequence

# b 二进制文件

filename="Kalimba.mp3"
with open(filename,"rb") as file:
    print(file.read(100))
# b'ID3\x03\x00\x00\x00\x03Y1GEOB\x00\x00\x00\x19\x00\x00\x00\x00\x00SfMarkers\x00\x0c\x00\x00\x00d\x00\x00\x00\x00\x00\x00\x00COMM\x00\x00\x00\x17\x00\x00\x00eng\x00Ninja Tune RecordsPRIV\x00\x00\x00)\x00\x00WM/MediaClas'

# 读二进制 rb
# 写二进制 wb
# 追加二进制 ab

with open(filename,'rb') as file_obj:
    # 将读取到的内容写出来
    # 定义一个新的文件
    new_name = 'abc.mp3'
    with open(new_name,'wb') as new_obj:
        chuck = 1024 *100
        while True:
            # 从已有的文件读取内容
            content = file_obj.read(chuck)
            # 内容读取完毕，循环结束
            if not content:
                break
            new_obj.write(content)

