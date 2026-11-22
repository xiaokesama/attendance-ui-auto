from page_objects.list_page import ListPage
from page_locators.visitor_page_locator import VisitorPageLocators as loc


class VisitorPage(ListPage):
    '''访客管理 - 访客记录：按姓名、预约时间段、是否出访查询'''

    name = "访客记录"
    menu_path = ['访客管理', '访客记录']

    def open(self):
        '''
        通过左侧菜单进入访客记录
        :return:page_object
        '''
        return self.open_by_menu()

    # ---------- 查询区 ----------
    def input_name(self, name):
        '''
        输入访客姓名
        :param name:访客姓名 str
        :return:page_object
        '''
        self.wait_element_is_visible(loc.name_input_loc, '输入访客姓名').send_keys(name)
        return self

    def select_out_visit(self, option):
        '''
        选择是否出访
        :param option:选项文案 str
        :return:page_object
        '''
        return self.select_search_option(loc.out_visit_label, option)

    def open_date_picker(self):
        '''
        打开预约时间段日历面板（需要点击开始时间输入框）
        :return:page_object
        '''
        self.wait_element_is_clickable(loc.start_date_loc, '打开预约时间段').click_element()
        self.delay(0.3)
        return self

    def is_date_picker_open(self):
        '''
        判断预约时间段日历面板是否展开
        :return:bool
        '''
        return self.is_element_exist(loc.picker_panel_loc, timeout=2)

    def get_calendar_day_count(self):
        '''
        获取日历面板中的可选日期数量
        :return:int
        '''
        return len(self.find_elements(loc.calendar_day_loc, '获取日历日期'))

    def get_date_placeholders(self):
        '''
        获取开始/结束时间的占位符，如 ['开始时间', '结束时间']
        :return:list[str]
        '''
        start = self.wait_element_is_visible(loc.start_date_loc, '获取开始时间').get_element_attr('placeholder')
        end = self.wait_element_is_visible(loc.end_date_loc, '获取结束时间').get_element_attr('placeholder')
        return [start, end]

    # ---------- 表格数据 ----------
    def get_visitor_names(self):
        '''
        获取访客姓名列
        :return:list[str]
        '''
        return self.get_column_texts(loc.col_visitor_name)

    def get_phones(self):
        '''
        获取手机号码列
        :return:list[str]
        '''
        return self.get_column_texts(loc.col_phone)

    def get_bookers(self):
        '''
        获取预约人列
        :return:list[str]
        '''
        return self.get_column_texts(loc.col_booker)

    def get_arrive_times(self):
        '''
        获取到访时间列
        :return:list[str]
        '''
        return self.get_column_texts(loc.col_arrive_time)

    def get_areas(self):
        '''
        获取通行区域列
        :return:list[str]
        '''
        return self.get_column_texts(loc.col_area)

    def get_durations(self):
        '''
        获取访问时长列
        :return:list[str]
        '''
        return self.get_column_texts(loc.col_duration)

    def get_out_visit_statuses(self):
        '''
        获取是否出访列
        :return:list[str]
        '''
        return self.get_column_texts(loc.col_out_visit)

    def get_audit_statuses(self):
        '''
        获取审批状态列
        :return:list[str]
        '''
        return self.get_column_texts(loc.col_audit_status)
