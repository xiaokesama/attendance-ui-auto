from selenium.webdriver.common.by import By

from page_objects.list_page import ListPage
from page_locators.guard_page_locator import GuardPageLocators as loc


class GuardPage(ListPage):
    '''门禁管理 - 门禁权限：权限组查询与新增'''

    name = "门禁权限"
    menu_path = ['门禁管理', '门禁权限']

    def open(self):
        '''
        通过左侧菜单进入门禁权限
        :return:page_object
        '''
        return self.open_by_menu()

    # ---------- 查询区 ----------
    def input_group_name(self, group_name):
        '''
        输入权限组名称
        :param group_name:权限组名称 str
        :return:page_object
        '''
        self.wait_element_is_visible(loc.group_input_loc, '输入权限组名称').send_keys(group_name)
        return self

    # ---------- 操作区 ----------
    def click_add_group(self):
        '''
        点击「新增权限组」
        :return:page_object
        '''
        self.wait_element_is_clickable((By.XPATH, loc.add_group_btn_tpl), '点击新增权限组').click_element()
        return self

    # ---------- 表格数据 ----------
    def get_group_names(self):
        '''
        获取权限组名称列
        :return:list[str]
        '''
        return self.get_column_texts(loc.col_group_name)

    def get_member_texts(self):
        '''
        获取人员列
        :return:list[str]
        '''
        return self.get_column_texts(loc.col_members)

    def get_periods(self):
        '''
        获取开放周期列
        :return:list[str]
        '''
        return self.get_column_texts(loc.col_period)

    def get_times(self):
        '''
        获取时间列
        :return:list[str]
        '''
        return self.get_column_texts(loc.col_time)

    def get_bound_devices(self):
        '''
        获取绑定设备列
        :return:list[str]
        '''
        return self.get_column_texts(loc.col_devices)
