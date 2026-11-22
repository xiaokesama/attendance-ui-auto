from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage
from page_locators.common_locator import CommonLocators as loc


class CommonPage(BasePage):
    '''全站公共组件操作：消息提示、弹窗、下拉菜单'''

    name = "公共组件"

    # ---------- 消息提示 ----------
    def get_message_text(self):
        '''
        获取顶部消息提示文案，如「登录成功」
        :return:str
        '''
        return self.wait_element_is_visible(loc.message_text_loc, '获取消息提示').get_element_text()

    def wait_message_disappear(self, timeout=5):
        '''
        等待消息提示自动消失
        :return:page_object
        '''
        return self.wait_element_is_invisible(loc.message_loc, '等待消息提示消失', timeout=timeout)

    # ---------- 弹窗 ----------
    def is_modal_visible(self):
        '''
        判断弹窗是否可见
        :return:bool
        '''
        return self.is_element_exist(loc.modal_loc, timeout=3)

    def get_modal_title(self):
        '''
        获取弹窗标题
        :return:str
        '''
        return self.wait_element_is_visible(loc.modal_title_loc, '获取弹窗标题').get_element_text()

    def click_modal_ok(self):
        '''
        点击弹窗的确定按钮
        :return:page_object
        '''
        self.wait_element_is_clickable(loc.modal_ok_loc, '点击弹窗确定').click_element()
        return self

    def click_modal_cancel(self):
        '''
        点击弹窗的取消按钮
        :return:page_object
        '''
        self.wait_element_is_clickable(loc.modal_cancel_loc, '点击弹窗取消').click_element()
        return self

    def close_modal(self):
        '''
        点击弹窗右上角关闭
        :return:page_object
        '''
        self.wait_element_is_clickable(loc.modal_close_loc, '关闭弹窗').click_element()
        return self

    # ---------- 二次确认框 ----------
    def get_confirm_title(self):
        '''
        获取二次确认框标题
        :return:str
        '''
        return self.wait_element_is_visible(loc.confirm_title_loc, '获取确认框标题').get_element_text()

    def click_confirm_ok(self):
        '''
        确认框点击确定
        :return:page_object
        '''
        self.wait_element_is_clickable(loc.confirm_ok_loc, '确认框点击确定').click_element()
        return self

    # ---------- 下拉菜单 ----------
    def get_dropdown_texts(self):
        '''
        获取展开的下拉菜单项文案
        :return:list[str]
        '''
        return self.get_elements_text(loc.dropdown_item_loc, '获取下拉菜单')

    def click_dropdown_item(self, text):
        '''
        点击下拉菜单项
        :param text:菜单项文案 str
        :return:page_object
        '''
        locator = (By.XPATH, loc.dropdown_item_tpl.format(text))
        self.wait_element_is_clickable(locator, '点击下拉项{}'.format(text)).click_element()
        return self
