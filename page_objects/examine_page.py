from page_objects.list_page import ListPage
from page_locators.examine_page_locator import ExaminePageLocators as loc


class ExaminePage(ListPage):
    '''审批管理 - 我的申请：只有表格，没有查询区与操作区按钮'''

    name = "我的申请"
    menu_path = ['审批管理', '我的申请']

    def open(self):
        '''
        通过左侧菜单进入我的申请
        :return:page_object
        '''
        return self.open_by_menu()

    # ---------- 表格数据 ----------
    def get_task_types(self):
        '''
        获取审批任务类型列
        :return:list[str]
        '''
        return self.get_column_texts(loc.col_task_type)

    def get_apply_times(self):
        '''
        获取审批申请时间列
        :return:list[str]
        '''
        return self.get_column_texts(loc.col_apply_time)

    def get_statuses(self):
        '''
        获取状态列
        :return:list[str]
        '''
        return self.get_column_texts(loc.col_status)

    def get_first_application(self):
        '''
        获取第一条申请记录，返回单元格文本列表
        :return:list[str]
        '''
        return self.get_cell_texts(1)
