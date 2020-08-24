'''
     功能：爬取小说正文（V2）
     版本：2.0
     主要实现：通过selenium 访问网页
        增加超时处理（成功，但解析不出内容）

'''

# 1、导入框架
from selenium import webdriv
class down_story:
    def __init__(self,url,path):
        self.url=url
        self.path=path
        # driver = webdriver.Chrome()
        # driver.get(self.url)
        self.dom_id_sign = "blog-post"     #<div id="blog-post" class="col-lg-9">
        self.dom_class_sign = "p[class='lead']"            #<p class="lead">
        self.driver = webdriver.Chrome()

    def get_text(self):
        # driver = webdriver.Chrome()
        # 两个同时设置才行
        # 实现效果:加载状态停止，进行代码下一步操作
        self.driver.set_page_load_timeout(60)
        self.driver.set_script_timeout(60)  # 这两种设置都进行才有效
        open_status = 0
        try:
            self.driver.get(self.url)
        except:
            self.driver.execute_script('window.stop()')
            open_status= 1

        result = ""
        if  open_status==0:
            dom = self.driver.find_element_by_id(self.dom_id_sign)  # 找到主体部分
            dom_class = dom.find_elements_by_css_selector(self.dom_class_sign)
            # dom_text = dom.find_elements_by_xpath("//p[@class='lead']")
            # dom_title = dom.find_elements_by_css_selector("//dev[@class='box']")
            dom_title = dom.find_element_by_xpath("//div[@class='box']/p").text

            # print(dom_class[0].text)
            # print(dom_title)

            self.driver.quit()

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