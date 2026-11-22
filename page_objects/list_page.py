import re

from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage
from page_objects.home_page import HomePage
from page_objects.menu_bar import MenuBar
from page_locators.list_page_locator import ListPageLocators as loc


class ListPage(BasePage):
    '''
    列表页通用操作（查询、表格、分页、操作区）

    说明：本项目的详情页路由不响应直接访问，会被路由守卫重定向回首页，
    因此各业务页统一通过左侧菜单进入（见 menu_path 与 open_by_menu）。
    '''

    name = "列表页"

    # 进入该页面的菜单层级，由子类覆盖
    menu_path = None

    def open_by_menu(self):
        '''
        先打开首页，再按 menu_path 逐级点击菜单进入当前页面
        :return:page_object
        '''
        if not self.menu_path:
            raise ValueError('{} 未配置 menu_path'.format(self.name))
        HomePage(self.driver).open()
        MenuBar(self.driver).open_menu(*self.menu_path)
        self.wait_table_loaded()
        return self

    def wait_table_loaded(self):
        '''
        等待表格与表头加载完成
        :return:page_object
        '''
        self.wait_element_is_visible(loc.table_loc, '等待表格加载')
        self.wait_element_is_visible(loc.thead_loc, '等待表头加载')
        return self

    # ---------- 查询区 ----------
    def click_search(self):
        '''
        点击查询
        :return:page_object
        '''
        self.wait_element_is_clickable(loc.query_btn_loc, '点击查询').click_element()
        self.wait_table_loaded()
        return self

    def click_reset(self):
        '''
        点击重置
        :return:page_object
        '''
        locator = (By.XPATH, loc.reset_btn_tpl)
        self.wait_element_is_clickable(locator, '点击重置').click_element()
        self.wait_table_loaded()
        return self

    def select_search_option(self, label, option):
        '''
        按表单项标签展开下拉并选择选项
        :param label:表单项标签 str，如 设备状态
        :param option:选项文案 str
        :return:page_object
        '''
        select_locator = (By.XPATH, loc.select_by_label_tpl.format(label))
        self.wait_element_is_clickable(select_locator, '展开{}下拉'.format(label)).click_element()
        option_locator = (By.XPATH, loc.option_tpl.format(option))
        self.wait_element_is_clickable(option_locator, '选择{}'.format(option)).click_element()
        self.delay(0.3)
        return self

    # ---------- 表格 ----------
    def get_thead_texts(self):
        '''
        获取表头文案（已去掉多选框列的空表头）
        :return:list[str]
        '''
        texts = self.get_elements_text(loc.thead_loc, '获取表头')
        return [text for text in texts if text]

    def get_row_count(self):
        '''
        获取当前页数据行数
        :return:int
        '''
        return len(self.find_elements(loc.row_loc, '获取数据行'))

    def get_cell_texts(self, row=1):
        '''
        获取指定行的所有单元格文本
        :param row:行号，从 1 开始 int
        :return:list[str]
        '''
        locator = (By.XPATH, loc.cell_row_tpl.format(row))
        return self.get_elements_text(locator, '获取第{}行单元格'.format(row))

    def get_column_texts(self, index):
        '''
        获取指定列的所有单元格文本
        :param index:列号，从 1 开始 int
        :return:list[str]
        '''
        locator = (By.XPATH, loc.cell_column_tpl.format(index))
        return self.get_elements_text(locator, '获取第{}列'.format(index))

    def is_empty(self):
        '''
        判断表格是否为空数据状态
        :return:bool
        '''
        return self.is_element_exist(loc.empty_loc, timeout=2)

    # ---------- 分页 ----------
    def get_total_count(self):
        '''
        获取分页总条数，如「共7条」-> 7
        :return:int
        '''
        text = self.wait_element_is_visible(loc.pagination_loc, '获取分页信息').get_element_text()
        result = re.search(r'共\s*(\d+)\s*条', text)
        if not result:
            raise AssertionError('未从分页信息中取到总条数：{}'.format(text))
        return int(result.group(1))

    def get_page_count(self):
        '''
        获取可点击的页码数量
        :return:int
        '''
        return len(self.find_elements(loc.pagination_item_loc, '获取页码'))

    def goto_page(self, page):
        '''
        跳转到指定页码
        :param page:页码 int
        :return:page_object
        '''
        locator = (By.XPATH, loc.pagination_item_tpl.format(page))
        self.wait_element_is_clickable(locator, '跳转到第{}页'.format(page)).click_element()
        self.wait_table_loaded()
        return self

    # ---------- 操作区 ----------
    def get_toolbar_texts(self):
        '''
        获取操作区按钮文案
        :return:list[str]
        '''
        buttons = self.find_elements(loc.toolbar_btn_loc, '获取操作区按钮')
        return [button.text.strip() for button in buttons if button.text.strip()]

    def click_toolbar_button(self, name):
        '''
        点击操作区按钮
        :param name:按钮文案 str
        :return:page_object
        '''
        locator = (By.XPATH, loc.toolbar_btn_tpl.format(name))
        self.wait_element_is_clickable(locator, '点击操作区按钮{}'.format(name)).click_element()
        return self

    def is_toolbar_button_enabled(self, name):
        '''
        判断操作区按钮是否可用（没有 disabled 属性即为可用）
        :param name:按钮文案 str
        :return:bool
        '''
        locator = (By.XPATH, loc.toolbar_btn_tpl.format(name))
        disabled = self.wait_element_is_visible(locator, '读取按钮{}状态'.format(name)).get_element_attr('disabled')
        return disabled is None
