import re

from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage
from page_locators.home_page_locator import HomePageLocators as loc


class HomePage(BasePage):
    '''首页工作台操作：快捷导航、机构信息、今日考勤统计、操作文档、今日访客统计'''

    name = "首页工作台"

    def open(self):
        '''
        打开首页工作台
        :return:page_object
        '''
        self.get(self.settings.PROJECT_HOST + loc.url)
        self.wait_element_is_visible(loc.home_page_loc, '打开首页工作台')
        self.wait_element_is_visible(loc.card_title_loc, '等待首页卡片加载')
        return self

    def is_login_page(self):
        '''
        当前是否被重定向到登录页（未登录或登录态过期）
        :return:bool
        '''
        return '/user/login' in self.get_current_url()

    # ---------- 顶部信息 ----------
    def get_platform_name(self):
        '''
        获取左上角平台名称
        :return:str
        '''
        return self.wait_element_is_visible(loc.logo_name_loc, '获取平台名称').get_element_text()

    def get_welcome_text(self):
        '''
        获取顶部欢迎语，如「欢迎进入 智元云联」
        :return:str
        '''
        return self.wait_element_is_visible(loc.welcome_text_loc, '获取顶部欢迎语').get_element_text()

    def get_login_user(self):
        '''
        获取顶部当前登录用户
        :return:str
        '''
        return self.wait_element_is_visible(loc.user_dropdown_loc, '获取当前登录用户').get_element_text()

    # ---------- 卡片 ----------
    def get_card_titles(self):
        '''
        获取首页所有卡片标题
        :return:list[str]
        '''
        return self.get_elements_text(loc.card_title_loc, '获取首页卡片标题')

    def is_card_exist(self, title):
        '''
        判断指定标题的卡片是否存在
        :param title:卡片标题 str
        :return:bool
        '''
        locator = (By.XPATH, loc.card_title_tpl.format(title))
        return self.is_element_exist(locator, timeout=3)

    # ---------- 快捷导航 ----------
    def get_quick_nav_texts(self):
        '''
        获取快捷导航文案
        :return:list[str]
        '''
        return self.get_elements_text(loc.quick_nav_text_loc, '获取快捷导航')

    def click_quick_nav(self, name):
        '''
        点击快捷导航，如「人员列表」
        :param name:导航名称 str
        :return:page_object
        '''
        locator = (By.XPATH, loc.quick_nav_tpl.format(name))
        self.wait_element_is_clickable(locator, '点击快捷导航{}'.format(name)).click_element()
        self.wait_page_load()
        self.delay(0.5)
        return self

    # ---------- 机构信息 ----------
    def get_brand_value(self, label):
        '''
        获取机构信息的原始文案，如 部门数量 -> 已创建16个
        :param label:条目名称 str
        :return:str
        '''
        locator = (By.XPATH, loc.brand_item_value_tpl.format(label))
        return self.wait_element_is_visible(locator, '获取机构信息{}'.format(label)).get_element_text()

    def get_brand_count(self, label):
        '''
        获取机构信息的数量，如 部门数量 -> 16
        :param label:条目名称 str
        :return:int
        '''
        text = self.get_brand_value(label)
        result = re.search(r'\d+', text)
        if not result:
            raise AssertionError('机构信息【{}】未取到数量，原始文案：{}'.format(label, text))
        return int(result.group())

    def get_qr_code_url(self):
        '''
        获取机构二维码图片上携带的注册链接
        :return:str
        '''
        return self.wait_element_is_visible(loc.qr_code_loc, '获取机构二维码').get_element_attr('title')

    # ---------- 今日考勤统计 ----------
    def get_attendance_value(self, card='today'):
        '''
        获取今日考勤统计卡片的数值
        :param card:today 今日人数 / abnormal 异常人数 str
        :return:str
        '''
        card_locator = loc.attendance_card_today_loc if card == 'today' else loc.attendance_card_abnormal_loc
        locator = (By.CSS_SELECTOR, '{} .card-value'.format(card_locator[1]))
        return self.wait_element_is_visible(locator, '获取考勤统计数值').get_element_text()

    def get_attendance_indicators(self):
        '''
        获取考勤指标，返回 {'已打卡': '0', '请假': '0', '未打卡': '0', '迟到': '0'}
        :return:dict
        '''
        self.wait_element_is_visible(loc.indicator_loc, '等待考勤指标加载')
        labels = self.get_elements_text(loc.indicator_label_loc, '获取考勤指标名称')
        values = self.get_elements_text(loc.indicator_value_loc, '获取考勤指标数值')
        return dict(zip(labels, values))

    def get_indicator_value(self, label):
        '''
        获取单个考勤指标的数值
        :param label:指标名称 str
        :return:str
        '''
        locator = (By.XPATH, loc.indicator_tpl.format(label))
        return self.wait_element_is_visible(locator, '获取考勤指标{}'.format(label)).get_element_text()

    # ---------- 今日访客统计 ----------
    def get_visitor_value(self, day='today'):
        '''
        获取访客统计数值
        :param day:today 今日 / yesterday 昨日 str
        :return:str
        '''
        locator = loc.visitor_today_loc if day == 'today' else loc.visitor_yesterday_loc
        return self.wait_element_is_visible(locator, '获取访客统计数值').get_element_text()

    def get_visitor_chart_count(self):
        '''
        获取访客统计图表（echarts canvas）数量
        :return:int
        '''
        return len(self.find_elements(loc.visitor_chart_loc, '获取访客统计图表'))

    # ---------- 操作文档 / 更新公告 ----------
    def get_document_texts(self):
        '''
        获取操作入口文案，如 ['操作文档', '操作视频']
        :return:list[str]
        '''
        return self.get_elements_text(loc.document_loc, '获取操作入口文案')

    def click_document(self):
        '''
        点击「操作文档」
        :return:page_object
        '''
        self.wait_element_is_clickable(loc.document_loc, '点击操作文档').click_element()
        return self

    def click_document_video(self):
        '''
        点击「操作视频」
        :return:page_object
        '''
        self.wait_element_is_clickable(loc.document_video_loc, '点击操作视频').click_element()
        return self

    def get_announcements(self):
        '''
        获取更新公告列表，返回 [{'title': 标题, 'time': 时间}]
        :return:list[dict]
        '''
        self.wait_element_is_visible(loc.update_item_loc, '等待更新公告加载')
        result = []
        for item in self.find_elements(loc.update_item_loc, '获取更新公告'):
            paragraphs = item.find_elements(By.TAG_NAME, 'p')
            title = paragraphs[0].text.strip() if paragraphs else ''
            time_text = paragraphs[1].text.strip() if len(paragraphs) > 1 else ''
            result.append({'title': title, 'time': time_text})
        return result

    # ---------- 大屏 / 引导 ----------
    def is_big_screen_visible(self):
        '''
        判断右侧「大屏数据」入口是否展示
        :return:bool
        '''
        return self.is_element_exist(loc.big_screen_loc, timeout=3)

    def click_big_screen(self):
        '''
        点击「大屏数据」
        :return:page_object
        '''
        self.wait_element_is_clickable(loc.big_screen_loc, '点击大屏数据').click_element()
        return self

    def get_guide_text(self):
        '''
        获取引导按钮文案，如「展开指引」
        :return:str
        '''
        return self.wait_element_is_visible(loc.guide_text_loc, '获取引导按钮文案').get_element_text()

    def click_guide(self):
        '''
        点击引导按钮展开/收起指引
        :return:page_object
        '''
        self.wait_element_is_clickable(loc.guide_btn_loc, '点击引导按钮').click_element()
        self.delay(0.5)
        return self
