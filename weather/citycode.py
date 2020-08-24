# -*- coding: utf-8 -*-
# @time :2020/8/12 10:23
# @Author:老萝卜
# @file:citycode
# @Software:%{PRODUICT_NAME}

import requests
from lxml import etree
import json

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"
}


def save_text(path, content, oprtype="w"):
    with open(path, oprtype, encoding="utf-8") as file:
        file.write(content)


class CityCode:
    def __init__(self):
        self.level_province = ""  #
        self.level_area = ""  # 区域：华东、华中、华北、
        self.province_eng = ""
        self.province_chn = ""
        self.city_eng = ""
        self.city_chn = ""
        self.county_eng = ""
        self.conty_chn = ""
        self.city_code = ""

# 获取城市代码类
class GetCityCode:
    def __init__(self):
        self._start_url = "http://www.weather.com.cn/textFC/hb.shtml"
        self._base_url = "http://www.weather.com.cn/"
        self._dict_citymsg=dict()                   # 城市代码信息表
        self._dict_provincemsg=dict()               # 省信息代码表     ｛省名：[区域,英文,分类码,省url]｝
        self._citydist=dict()

    @property
    def base_url(self):
        return self._base_url

    @base_url.setter
    def base_url(self, url):
        self._base_url = url

    @property
    def start_url(self):
        return self._start_url

    @start_url.setter
    def start_url(self, url):
        self._start_url = url

    # 打开网页返回页面源码
    def getHTMLtext(self, url):
        """请求获得网页内容"""
        try:
            r = requests.get(url, timeout=30)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            # print("成功访问")
            return r.text
        except:
            print("访问错误")
            return ""

    # 解析区域-省名，返回省名列表
    def xpath_area_province(self, pagestr):
        html = etree.HTML(pagestr)
        provincelist = html.xpath("//div[@class='lQCity']/ul/li/a/text()")
        return provincelist

    # 得到该区域所有省名省名列表
    def get_area_province(self, namestr, url):
        ret_list = []
        responsestr = self.getHTMLtext(url)
        if responsestr != "":
            save_text("2.html", responsestr, "a")
            ret_list = self.xpath_area_province(responsestr)
        return ret_list

    # 获取所有区域-省名，返回省名区域字典
    def get_all_area_province(self, pagestr):
        dict_province_area = dict()
        html = etree.HTML(pagestr)
        areaname_list = html.xpath('//ul[@class="lq_contentboxTab2"]/li/span/a/text()')
        areaurl_list = html.xpath('//ul[@class="lq_contentboxTab2"]/li/span/a/@href')
        # print(areaname_list)
        # print(areaurl_list)
        for areaname, areaurl in zip(areaname_list, areaurl_list):
            url = self._base_url[:-1] + areaurl
            provincelist = self.get_area_province(areaname, url)
            if len(provincelist) == 0:
                print(areaname + "无省份，请检查！url={}".format(url))
            for province in provincelist:
                dict_province_area[province] = areaname
        return dict_province_area

    # 解析省快速分类码
    def xpath_lvl_province(self, lvlelement):
        dict_province_lvlstr = dict()               # {"provincename": ["province_eng", "levelname", "urlprovince"]}
        html = etree.fromstring(lvlelement)
        lvlname = html.xpath("//span/text()")
        provincename_list = html.xpath("//a/text()")
        provinceurl_list = html.xpath("//a/@href")
        # print("lvlname=", lvlname, "provincename_list=", provincename_list, "provinceurl_list=", provinceurl_list)
        len1 = len(lvlname)
        if len(lvlname) != 1 or len(provincename_list) == len(provinceurl_list) == 0:
            print("数据格式不对，请检查数据源")
        else:
            for provincename, provinceurl in zip(provincename_list, provinceurl_list):
                start = provinceurl.rfind("/") + 1
                end = provinceurl.rfind(".")
                province_eng = provinceurl[start:end]  # 得到省的英文拼写
                dict_province_lvlstr[provincename] = [province_eng, lvlname[0], self.base_url[:-1] + provinceurl]
        return dict_province_lvlstr

    # 根据访问url,解析城市代码
    def get_citycode(self, content):
        start = content.rfind("/") + 1
        end = content.rfind(".")
        return content[start:end]

    # 解析每个市州各城市或区的信息
    def xpath_citymsglist(self, tableelement,provincename,provincemsglist):
        dict_city=dict()
        save_text("4.html", tableelement, "a")
        html = etree.fromstring(tableelement)
        cityname = html.xpath("//td[@class='rowsPan']/text()")      # 得到市州名称
        county_list = html.xpath("//a/text()")[::2]  # 包含一全"详情"
        countyurl_list = html.xpath("//a/@href")[::2]  # 包含一全"详情"
        # save_text("5.txt",f"cityname={cityname}\ncounty_list={county_list}\nurl={countyurl_list}\n\n\n"+"-"*30+"\n","a")
        for countyname, cityurl in zip(county_list, countyurl_list):
            citycode = self.get_citycode(cityurl)
            # if dict_city.get(countyname)==None:
            #     dict_city[countyname]=["","","","","",[]]
            dict_city[countyname]=[provincename,cityname[0],countyname,citycode,cityurl,provincemsglist]
        return dict_city

    # 解析省内所有城市信息
    def xpath_privinceallcitymsg(self, pagestr,provincename,provincemsglist):
        dict_city = dict()
        save_text("3.html", pagestr)
        html = etree.HTML(pagestr)
        table_list = html.xpath('//div[@class="conMidtab3"]/table')
        table_list=table_list[:int(len(table_list)/7)]          # 每个市州都有7个，7天数据
        for i, tablestr in enumerate(table_list):
            elementstr = etree.tostring(tablestr, encoding="utf-8").decode("utf-8")
            # print("elementstr=",elementstr)
            save_text("4.txt", f"{i}\n" + "-" * 30 + "\n" + elementstr + "\n\n", "a")
            dict_city.update(self.xpath_citymsglist(elementstr,provincename,provincemsglist))
        return dict_city


    # 获取省快速分类信息字典
    def get_all_province_lvl(self, pagestr):
        dict_province_lvlurls = dict()              # {"provincename": ["province_eng", "levelname", "urlprovince"]}   ｛省名：[英文名,快速分类码,链接地址]｝
        html = etree.HTML(pagestr)
        lvl_list = html.xpath('//div[@class="lqcontentBoxheader"]/ul/li')
        # print("lvl_list=",lvl_list)
        for lvlelement in lvl_list:
            elementstr = etree.tostring(lvlelement, encoding="utf-8").decode("utf-8")
            dict_province_lvlurls.update(self.xpath_lvl_province(elementstr))
        # print(dict_province_lvlurls)
        return dict_province_lvlurls

    # 获取省内所有城市信息
    def get_province_allcity(self,provincename,provincemsglist):
        url = provincemsglist[3]
        # print(url)
        content = self.getHTMLtext(url)
        return self.xpath_privinceallcitymsg(content,provincename,provincemsglist)

    # 根据省信息字典中省url，获取城市信息
    def get_all_citycode(self,dict_province):
        dict_city = dict()
        for province,provincemsglist in dict_province.items():
            dict_city.update(self.get_province_allcity(province,provincemsglist))
            print(f"{province}省所有城市信息已获取")
        return dict_city

    # 根据省-区域字典 更新 省信息字典 中区域信息
    def update_provinc_area(self,dict_area):
        for provincename,area in dict_area.items():
            if self._dict_provincemsg.get(provincename)==None:
                self._dict_provincemsg[provincename]=["","","",""]
            self._dict_provincemsg[provincename][0]=area

    # 根据 省快速分类信息字典 更新 省信息字典
    def update_province_lvl(self,dict_lvl):
        for provincename,item in dict_lvl.items():
            if self._dict_provincemsg.get(provincename)==None:
                self._dict_provincemsg[provincename]=['','','','']
            self._dict_provincemsg[provincename][1:4]=item

    # 根据城市信息字典 更新类的城市信息字典
    def update_citymsg(self,dict_city):
        self._dict_citymsg.update(dict_city)

    # 计算得到完整城市信息(含省信息)
    def get_allcitymsg(self):
        straturlstr = self.getHTMLtext(self.start_url)
        if straturlstr != "":
            # 更新区域-省字典
            dict_province_area = self.get_all_area_province(straturlstr)
            # print(dict_province_area)
            self.update_provinc_area(dict_province_area)
            print("获取区域-省份信息并更新完成")

            # 获取快速分类相关信息
            dict_province_lvl = self.get_all_province_lvl(straturlstr)
            # print(dict_province_lvl)
            self.update_province_lvl(dict_province_lvl)
            # print(self._dict_provincemsg)

            print("获取各省快速分类相关信息并更新完成")

            # print(self._dict_provincemsg.get("湖北"))
            # # 获到湖北城市相关信息
            # dict3=self.get_province_allcity("湖北",self._dict_provincemsg.get("湖北"))
            # print(dict3)

            dict_allcitymsg = self.get_all_citycode(self._dict_provincemsg)
            # print(dict_allcitymsg)
            self.update_citymsg(dict_allcitymsg)
            print(self._dict_citymsg)

    def save_json(self,filename,dictname):
        res2 = json.dumps(dictname, indent=4, ensure_ascii=False)
        print(res2)
        with open(filename,"w",encoding="utf-8") as file:
            file.write(res2)
    # def write_to_csv(file_name, data):
    #     """保存为csv文件"""
    #     with open(file_name, 'a', errors='ignore', newline='') as f:
    #         if day == 14:
    #             header = ['日期', '天气', '最低气温', '最高气温', '风向1', '风向2', '风级']
    #         else:
    #             header = ['小时', '温度', '风力方向', '风级', '降水量', '相对湿度', '空气质量']
    #         f_csv = csv.writer(f)
    #         f_csv.writerow(header)
    #         f_csv.writerows(data)


if __name__ == "__main__":
    getcc = GetCityCode()
    straturlstr = getcc.getHTMLtext(getcc.start_url)
    save_text("1.html", straturlstr)
    # print(areapatstr)

    if straturlstr != "":
        # 获取区域- 省信息
        dict1=getcc.get_all_area_province(straturlstr)
        # print(dict1)
        getcc.update_provinc_area(dict1)
        # print(getcc._dict_provincemsg)

        print("获取区域-省份信息并更新完成")

        # 获取快速分类相关信息
        dict2=getcc.get_all_province_lvl(straturlstr)
        # print(dict2)
        getcc.update_province_lvl(dict2)
        # print(getcc._dict_provincemsg)

        print("获取各省快速分类相关信息并更新完成")

        # print(getcc._dict_provincemsg.get("湖北"))
        # # 获到湖北城市相关信息
        # dict3=getcc.get_province_allcity("湖北",getcc._dict_provincemsg.get("湖北"))
        # print(dict3)

        dict4=getcc.get_all_citycode(getcc._dict_provincemsg)
        print(dict4)

        getcc.save_json("provincemsg.json",getcc._dict_provincemsg)

        getcc.save_json("citycodemsg,json",getcc._dict_citymsg)


        # print(dict1)
        # getcc.get_all_province(areapatstr)
