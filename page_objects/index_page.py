from time import sleep
from page_objects.base_page import BasePage
from page_locators.index_page_locator import IndexPageLocators as loc


# 这个页面只能调用被封装的函数
class IndexPage(BasePage):

    # 查询操作
    def search(self, keywords):
        # self是BasePage对象， self.driver是webdriver对象,他们调用各自的方法
        # 输入关键字
        self.wait_element_is_loaded(loc.search_box_loc).delay(1).send_keys(keywords)
        # 点击搜索按钮
        self.wait_element_is_clickable(loc.search_btn_loc).delay(1).click_element()
        # 等待页面加载
        self.wait_page_load()
        sleep(1)