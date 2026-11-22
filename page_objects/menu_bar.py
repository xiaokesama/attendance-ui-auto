from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage
from page_locators.menu_locator import MenuLocators as loc


class MenuBar(BasePage):
    '''框架层操作：左侧菜单栏、顶部标签页'''

    name = "菜单导航"

    # ---------- 菜单栏 ----------
    def get_top_menu_texts(self):
        '''
        获取一级菜单文案（含带子菜单的菜单标题），按页面展示顺序返回
        :return:list[str]
        '''
        self.wait_element_is_visible(loc.menu_root_loc, '等待左侧菜单加载')
        texts = []
        for item in self.find_elements(loc.top_menu_item_loc, '获取一级菜单'):
            # 带子菜单的菜单项文本可能是多行，取第一行
            text = item.text.strip().split('\n')[0].strip()
            if text:
                texts.append(text)
        return texts

    def click_top_menu(self, name):
        '''
        点击不带子菜单的一级菜单，如「首页」「账号管理」
        :param name:菜单文案 str
        :return:page_object
        '''
        locator = (By.XPATH, loc.menu_item_tpl.format(name))
        self.wait_element_is_clickable(locator, '点击菜单{}'.format(name)).click_element()
        self.wait_page_load()
        self.delay(0.5)
        return self

    def is_submenu_open(self, name):
        '''
        判断指定子菜单是否已展开
        :param name:菜单文案 str
        :return:bool
        '''
        locator = (By.XPATH, loc.submenu_open_tpl.format(name))
        return self.is_element_exist(locator, timeout=1)

    def expand_submenu(self, name):
        '''
        展开带子菜单的菜单（已展开则跳过，可安全重复调用）
        :param name:菜单文案 str
        :return:page_object
        '''
        if self.is_submenu_open(name):
            return self
        locator = (By.XPATH, loc.submenu_title_tpl.format(name))
        self.wait_element_is_clickable(locator, '展开菜单{}'.format(name)).click_element()
        self.delay(0.5)
        return self

    def click_menu_link(self, name):
        '''
        点击叶子菜单（带 href 的菜单项）
        :param name:菜单文案 str
        :return:page_object
        '''
        locator = (By.XPATH, loc.menu_link_tpl.format(name))
        self.wait_element_is_clickable(locator, '点击菜单{}'.format(name)).click_element()
        self.wait_page_load()
        self.delay(0.5)
        return self

    def open_menu(self, *names):
        '''
        按层级进入菜单，如 open_menu('考勤管理', '考勤规则设置', '考勤组管理')
        :param names:菜单层级 str
        :return:page_object
        '''
        if not names:
            raise ValueError('菜单层级不能为空')
        for name in names[:-1]:
            self.expand_submenu(name)
        self.click_menu_link(names[-1])
        return self

    def get_submenu_texts(self):
        '''
        获取已展开的子菜单文案（三层结构下子节点可能仍是子菜单）
        :return:list[str]
        '''
        texts = []
        for item in self.find_elements(loc.submenu_item_loc, '获取子菜单'):
            text = item.text.strip().split('\n')[0].strip()
            if text:
                texts.append(text)
        return texts

    def get_selected_menu(self):
        '''
        获取当前选中的菜单文案
        :return:str
        '''
        return self.wait_element_is_visible(loc.selected_menu_loc, '获取选中菜单').get_element_text()

    def is_menu_selected(self, name):
        '''
        判断指定菜单是否处于选中状态
        :param name:菜单文案 str
        :return:bool
        '''
        return name in self.get_selected_menu()

    def collapse_sider(self):
        '''
        折叠/展开左侧菜单栏
        :return:page_object
        '''
        self.wait_element_is_clickable(loc.sider_trigger_loc, '点击折叠菜单栏').click_element()
        self.delay(0.5)
        return self

    def is_sider_collapsed(self):
        '''
        判断左侧菜单栏是否处于折叠状态
        :return:bool
        '''
        class_name = self.wait_element_is_visible(loc.sider_loc, '读取菜单栏状态').get_element_attr('class')
        return 'ant-layout-sider-collapsed' in (class_name or '')

    # ---------- 标签页 ----------
    def get_tab_texts(self):
        '''
        获取已打开的标签页文案
        :return:list[str]
        '''
        texts = []
        for tab in self.find_elements(loc.tab_loc, '获取标签页'):
            text = tab.text.strip().split('\n')[0].strip()
            if text:
                texts.append(text)
        return texts

    def get_active_tab(self):
        '''
        获取当前激活的标签页文案
        :return:str
        '''
        return self.wait_element_is_visible(loc.tab_active_loc, '获取激活标签页').get_element_text()

    def switch_tab(self, name):
        '''
        切换到指定标签页
        :param name:标签页文案 str
        :return:page_object
        '''
        locator = (By.XPATH, loc.tab_tpl.format(name))
        self.wait_element_is_clickable(locator, '切换标签页{}'.format(name)).click_element()
        self.delay(0.5)
        return self

    def close_tab(self, name):
        '''
        关闭指定标签页
        :param name:标签页文案 str
        :return:page_object
        '''
        locator = (By.XPATH, loc.tab_close_tpl.format(name))
        self.wait_element_is_clickable(locator, '关闭标签页{}'.format(name)).click_element()
        self.delay(0.5)
        return self
