import re

from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage
from page_objects.common_page import CommonPage
from page_locators.person_page_locator import PersonPageLocators as loc


class PersonPage(BasePage):
    '''人员列表页操作：部门树、查询区、操作区、人员表格、分页'''

    name = "人员列表"

    def open(self):
        '''
        直接打开人员列表页
        :return:page_object
        '''
        self.get(self.settings.PROJECT_HOST + loc.url)
        self.wait_element_is_visible(loc.table_loc, '打开人员列表')
        return self

    def wait_table_loaded(self):
        '''
        等待人员表格加载完成
        :return:page_object
        '''
        self.wait_element_is_visible(loc.table_loc, '等待人员表格加载')
        self.wait_element_is_visible(loc.thead_loc, '等待表头加载')
        return self

    # ---------- 查询区 ----------
    def input_keyword(self, keyword):
        '''
        输入查询关键字（姓名/工号/手机号/卡号）
        :param keyword:关键字 str
        :return:page_object
        '''
        self.wait_element_is_visible(loc.keyword_input_loc, '输入查询关键字').send_keys(keyword)
        return self

    def get_keyword(self):
        '''
        获取查询关键字输入框当前内容
        :return:str
        '''
        return self.wait_element_is_visible(loc.keyword_input_loc, '读取查询关键字').get_element_attr('value')

    def click_search(self):
        '''
        点击查询
        :return:page_object
        '''
        self.wait_element_is_clickable(loc.search_btn_loc, '点击查询').click_element()
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

    def select_person_type(self, name):
        '''
        选择人员类型
        :param name:人员类型 str
        :return:page_object
        '''
        self.wait_element_is_clickable(loc.person_type_select_loc, '展开人员类型下拉').click_element()
        locator = (By.XPATH, loc.person_type_tpl.format(name))
        self.wait_element_is_clickable(locator, '选择人员类型{}'.format(name)).click_element()
        self.delay(0.3)
        return self

    # ---------- 操作区 ----------
    def click_add_person(self):
        '''
        点击「新增人员」，打开新增弹窗
        :return:page_object
        '''
        locator = (By.XPATH, loc.add_person_btn_tpl)
        self.wait_element_is_clickable(locator, '点击新增人员').click_element()
        return self

    def click_export(self):
        '''
        点击「导出」
        :return:page_object
        '''
        locator = (By.XPATH, loc.export_btn_tpl)
        self.wait_element_is_clickable(locator, '点击导出').click_element()
        return self

    def get_toolbar_texts(self):
        '''
        获取操作区按钮文案
        :return:list[str]
        '''
        buttons = self.find_elements((By.CSS_SELECTOR, '.table-operator button'), '获取操作区按钮')
        return [button.text.strip() for button in buttons if button.text.strip()]

    # ---------- 部门树 ----------
    def input_dept_name(self, name):
        '''
        在部门树中搜索部门
        :param name:部门名称 str
        :return:page_object
        '''
        self.wait_element_is_visible(loc.dept_search_input_loc, '输入部门名称').send_keys(name)
        return self

    def click_add_dept(self):
        '''
        点击「添加部门」
        :return:page_object
        '''
        locator = (By.XPATH, loc.add_dept_btn_tpl)
        self.wait_element_is_clickable(locator, '点击添加部门').click_element()
        return self

    # ---------- 人员表格 ----------
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
        return len(self.find_elements(loc.row_loc, '获取人员行数'))

    def get_person_names(self):
        '''
        获取当前页人员姓名（第3列：注册照片 / 姓名 / 部门 ...）
        :return:list[str]
        '''
        names = []
        for row in self.find_elements(loc.row_loc, '获取人员列表'):
            cells = row.find_elements(By.TAG_NAME, 'td')
            if len(cells) >= 3:
                names.append(cells[2].text.strip())
        return names

    def is_empty(self):
        '''
        判断表格是否为空数据状态
        :return:bool
        '''
        return self.is_element_exist(loc.empty_loc, timeout=2)

    # ---------- 分页 ----------
    def get_total_count(self):
        '''
        获取分页总条数，如「共24条」-> 24
        :return:int
        '''
        text = self.wait_element_is_visible(loc.pagination_loc, '获取分页信息').get_element_text()
        result = re.search(r'共\s*(\d+)\s*条', text)
        if not result:
            raise AssertionError('未从分页信息中取到总条数：{}'.format(text))
        return int(result.group(1))

    def goto_page(self, page):
        '''
        跳转到指定页码
        :param page:页码 int
        :return:page_object
        '''
        locator = (
            By.XPATH,
            "//ul[contains(@class,'ant-pagination')]//li[contains(@class,'ant-pagination-item')][@title='{}']"
            .format(page),
        )
        self.wait_element_is_clickable(locator, '跳转到第{}页'.format(page)).click_element()
        self.wait_table_loaded()
        return self

    def get_add_person_modal_title(self):
        '''
        获取「新增人员」弹窗标题
        :return:str
        '''
        return CommonPage(self.driver).get_modal_title()
