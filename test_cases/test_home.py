import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest

from page_objects.home_page import HomePage
from page_objects.menu_bar import MenuBar
from test_cases.base_case import BaseCase
from test_data.home_data import (
    announcement_min_count,
    attendance_labels,
    brand_items,
    card_titles,
    guide_text,
    platform_name,
    quick_nav_cases,
    welcome_prefix,
)


class TestHome(BaseCase):
    name = "首页工作台"

    @pytest.mark.success
    @pytest.mark.home
    def test_page_load(self, logged_driver):
        '''首页工作台加载完成，平台名称与欢迎语正常展示'''
        hp = HomePage(logged_driver).open()
        assert hp.get_platform_name() == platform_name
        assert welcome_prefix in hp.get_welcome_text()

    @pytest.mark.home
    def test_card_titles(self, logged_driver):
        '''首页五个业务卡片均展示'''
        hp = HomePage(logged_driver).open()
        actual = hp.get_card_titles()
        missing = [title for title in card_titles if title not in actual]
        assert not missing, '首页缺少卡片：{}，实际展示：{}'.format(missing, actual)

    @pytest.mark.home
    def test_brand_info(self, logged_driver):
        '''机构信息中的部门/人员/设备/访客待审批均展示且可解析出数量'''
        hp = HomePage(logged_driver).open()
        for item in brand_items:
            assert hp.get_brand_value(item), '机构信息【{}】未展示'.format(item)
        assert hp.get_brand_count('部门数量') >= 0
        assert hp.get_brand_count('设备数量') >= 0
        assert 'token=' in (hp.get_qr_code_url() or '')

    @pytest.mark.home
    def test_attendance_indicators(self, logged_driver):
        '''今日考勤统计的四个指标均展示'''
        hp = HomePage(logged_driver).open()
        indicators = hp.get_attendance_indicators()
        assert list(indicators.keys()) == attendance_labels
        assert hp.get_attendance_value('today').isdigit()
        assert hp.get_attendance_value('abnormal').isdigit()

    @pytest.mark.home
    def test_visitor_chart(self, logged_driver):
        '''今日访客统计图表渲染，今日/昨日柱状数据可读取'''
        hp = HomePage(logged_driver).open()
        assert hp.get_visitor_chart_count() >= 1
        assert hp.get_visitor_value('today').isdigit()
        assert hp.get_visitor_value('yesterday').isdigit()

    @pytest.mark.home
    def test_announcement(self, logged_driver):
        '''更新公告列表展示，且标题非空'''
        hp = HomePage(logged_driver).open()
        announcements = hp.get_announcements()
        assert len(announcements) >= announcement_min_count
        assert all(item['title'] for item in announcements)

    @pytest.mark.home
    def test_guide_button(self, logged_driver):
        '''左侧引导按钮文案正确'''
        hp = HomePage(logged_driver).open()
        assert hp.get_guide_text() == guide_text
        assert hp.is_big_screen_visible()

    @pytest.mark.smoke
    @pytest.mark.home
    @pytest.mark.parametrize('case', quick_nav_cases)
    def test_quick_nav_jump(self, case, logged_driver):
        '''点击快捷导航后打开对应标签页'''
        hp = HomePage(logged_driver).open()
        hp.click_quick_nav(case['name'])
        menu = MenuBar(logged_driver)
        assert case['name'] in menu.get_tab_texts()
        if case['route']:
            assert case['route'] in hp.get_current_url()

    @pytest.mark.home
    def test_close_tab(self, logged_driver):
        '''快捷导航打开的标签页可以关闭'''
        hp = HomePage(logged_driver).open()
        hp.click_quick_nav('人员列表')
        menu = MenuBar(logged_driver)
        assert '人员列表' in menu.get_tab_texts()
        menu.close_tab('人员列表')
        assert '人员列表' not in menu.get_tab_texts()
