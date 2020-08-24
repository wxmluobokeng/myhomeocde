'''
     功能：爬取小说正文（V2)
     版本：1.0
     主要实现：通过selenium 访问网页
'''

# 1、导入框架
from selenium import webdriver

class down_story:
    def __init__(self,url,path):
        self.url=url
        self.path=path
        self.dom_id_sign = "blog-post"     #<div id="blog-post" class="col-lg-9">
        self.dom_class_sign = "p[class='lead']"            #<p class="lead">
        self.driver = webdriver.Chrome()

    def get_text(self):
        # driver = webdriver.Chrome()
        self.driver.get(self.url)

        result = ""
        dom = self.driver.find_element_by_id(self.dom_id_sign)  # 找到主体部分
        dom_class = dom.find_elements_by_css_selector(self.dom_class_sign)
        # dom_text = dom.find_elements_by_xpath("//p[@class='lead']")
        # dom_title = dom.find_elements_by_css_selector("//dev[@class='box']")
        dom_title = dom.find_element_by_xpath("//div[@class='box']/p").text

        # print(dom_class[0].text)
        # print(dom_title)

        self.driver.quit()
        if len(dom_class)>0:
            result=dom_class[0].text

        return result

    def save_story(self,path,text):
        with open(path, "w") as f:
            f.write(text)


def main():
    url= "http://kuihua2020.com/v/txt/2020022665050.html"
    story = down_story(url,".\\1.txt")
    text = story.get_text()
    if text!="":
        story,save_story(self.path,text)
        print("下载成功！")
    else:
        print("下载失败！")
    # print(text)


if __name__ == "__main__":
    main()