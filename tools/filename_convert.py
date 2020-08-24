# -*- coding: utf-8 -*-
# @time :2020/7/13 14:56
# @Author:老萝卜
# @file:filename_convert
# @Software:%{PRODUICT_NAME}

'''
    filename_convert：文件名中存在异常字符转换成全角字符，防止文件保存时报错

'''

def filename_convert(filename_old):
    '''
    对文件和文件夹命bai名是不能使du用以下9个字符： / \ : * " < > | ？
    具体命名规则如下：
    ①zhi 文件名或文dao件夹名可以由1～256个西文字符或128个汉字（包括空格）组成，不能多于256个字符。
    ② 文件名可以有扩展名，也可以没有。有些情况下系统会为文件自动添加扩展名。一般情况下，文件名与扩展名中间用符号“.”分隔。
    ③ 文件名和文件夹名可以由字母、数字、汉字或~、!、@、#、$、%、^、&、( )、_、-、{}、’等组合而成。
    ④ 可以有空格，可以有多于一个的圆点。
    ⑤ 文件名或文件夹名中不能出现以下字符：\、/、:、*、?、"、<、>、| 。
    ⑥ 不区分英文字母大小写。
    '''
    filename_new =filename_old.replace("<","˂")
    filename_new =filename_new.replace(">", "˃")
    filename_new =filename_new.replace("/", "／")
    filename_new =filename_new.replace("\\", "∖")
    filename_new =filename_new.replace("|", "│")
    filename_new =filename_new.replace(":", "：")
    filename_new =filename_new.replace("\"", "“")
    filename_new =filename_new.replace("*","×")
    filename_new=filename_new.replace("?", "？")
    return filename_new


def main():
    # 文件名异常字符转换成全解字符
    filename_old="123?456.*ww"
    filename_new=filename_convert(filename_old)
    print(filename_new)

if __name__ == "__main__":
    main()