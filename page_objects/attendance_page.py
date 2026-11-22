from selenium.webdriver.common.by import By

from page_objects.list_page import ListPage
from page_locators.attendance_page_locator import AttendancePageLocators as loc


class AttendancePage(ListPage):
    '''考勤管理 - 考勤规则设置 - 考勤组管理'''

    name = "考勤组管理"
    menu_path = ['考勤管理', '考勤规则设置', '考勤组管理']

    def open(self):
        '''
        通过左侧三层菜单进入考勤组管理
        :return:page_object
        '''
        return self.open_by_menu()

    # ---------- 查询区 ----------
    def input_group_name(self, group_name):
        '''
        输入考勤组名称
        :param group_name:考勤组名称 str
        :return:page_object
        '''
        self.wait_element_is_visible(loc.group_input_loc, '输入考勤组名称').send_keys(group_name)
        return self

    # ---------- 操作区 ----------
    def click_add_group(self):
        '''
        点击「新增考勤组」
        :return:page_object
        '''
        self.wait_element_is_clickable((By.XPATH, loc.add_group_btn_tpl), '点击新增考勤组').click_element()
        return self

    # ---------- 表格数据 ----------
    def get_group_names(self):
        '''
        获取考勤组名称列
        :return:list[str]
        '''
        return self.get_column_texts(loc.col_group_name)

    def get_types(self):
        '''
        获取类型列
        :return:list[str]
        '''
        return self.get_column_texts(loc.col_type)

    def get_person_counts(self):
        '''
        获取人数列
        :return:list[str]
        '''
        return self.get_column_texts(loc.col_persons)

    def get_schedules(self):
        '''
        获取考勤时间列
        :return:list[str]
        '''
        return self.get_column_texts(loc.col_schedule)

    def get_statuses(self):
        '''
        获取状态列
        :return:list[str]
        '''
        return self.get_column_texts(loc.col_status)

    def get_effective_times(self):
        '''
        获取生效时间列
        :return:list[str]
        '''
        return self.get_column_texts(loc.col_effective_time)
