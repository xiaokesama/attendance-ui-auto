from selenium.webdriver.common.by import By

from page_objects.list_page import ListPage
from page_locators.device_page_locator import DevicePageLocators as loc


class DevicePage(ListPage):
    '''设备管理 - 设备列表：机构树、设备查询、添加设备'''

    name = "设备列表"
    menu_path = ['设备管理', '设备列表']

    def open(self):
        '''
        通过左侧菜单进入设备列表
        :return:page_object
        '''
        return self.open_by_menu()

    # ---------- 查询区 ----------
    def input_org(self, org_name):
        '''
        输入机构名称
        :param org_name:机构名称 str
        :return:page_object
        '''
        self.wait_element_is_visible(loc.org_input_loc, '输入机构名称').send_keys(org_name)
        return self

    def input_keyword(self, keyword):
        '''
        输入设备查询关键字（SN号/名称/账号归属/版本）
        :param keyword:关键字 str
        :return:page_object
        '''
        self.wait_element_is_visible(loc.keyword_input_loc, '输入设备查询关键字').send_keys(keyword)
        return self

    def select_status(self, status):
        '''
        选择设备状态
        :param status:设备状态 str
        :return:page_object
        '''
        return self.select_search_option(loc.status_label, status)

    # ---------- 左侧机构树 ----------
    def is_org_tree_visible(self):
        '''
        判断左侧机构树是否展示
        :return:bool
        '''
        return self.is_element_exist(loc.org_tree_loc, timeout=3)

    def get_org_tree_texts(self):
        '''
        获取机构树节点文案
        :return:list[str]
        '''
        return self.get_elements_text(loc.org_tree_node_loc, '获取机构树节点')

    # ---------- 头部与操作区 ----------
    def click_update_org(self):
        '''
        点击「更新机构」
        :return:page_object
        '''
        self.wait_element_is_clickable((By.XPATH, loc.update_org_btn_tpl), '点击更新机构').click_element()
        return self

    def click_add_device(self):
        '''
        点击「添加设备」
        :return:page_object
        '''
        self.wait_element_is_clickable((By.XPATH, loc.add_device_btn_tpl), '点击添加设备').click_element()
        return self

    def click_import(self):
        '''
        点击「导入数据」
        :return:page_object
        '''
        self.wait_element_is_clickable((By.XPATH, loc.import_btn_tpl), '点击导入数据').click_element()
        return self

    def click_long_password(self):
        '''
        点击「长期密码」
        :return:page_object
        '''
        self.wait_element_is_clickable((By.XPATH, loc.long_password_btn_tpl), '点击长期密码').click_element()
        return self

    # ---------- 表格数据 ----------
    def get_device_names(self):
        '''
        获取设备名称列
        :return:list[str]
        '''
        return self.get_column_texts(loc.col_name)

    def get_regions(self):
        '''
        获取设备区域列
        :return:list[str]
        '''
        return self.get_column_texts(loc.col_region)

    def get_device_sns(self):
        '''
        获取标识号(SN号)列
        :return:list[str]
        '''
        return self.get_column_texts(loc.col_sn)

    def get_statuses(self):
        '''
        获取设备状态列
        :return:list[str]
        '''
        return self.get_column_texts(loc.col_status)
