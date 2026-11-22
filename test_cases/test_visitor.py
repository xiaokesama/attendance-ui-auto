import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest

from page_objects.menu_bar import MenuBar
from page_objects.visitor_page import VisitorPage
from test_cases.base_case import BaseCase
from test_data.visitor_data import (
    date_placeholders,
    empty_keyword,
    out_visit_options,
    search_cases,
    table_headers,
)


class TestVisitor(BaseCase):
    name = "访客管理"

    @pytest.mark.success
    @pytest.mark.visitor
    def test_page_load(self, logged_driver):
        '''通过左侧菜单进入访客记录，标签页与表头正确'''
        vp = VisitorPage(logged_driver).open()
        assert VisitorPage.tab_name in MenuBar(logged_driver).get_active_tab()
        actual = vp.get_thead_texts()
        missing = [header for header in table_headers if header not in actual]
        assert not missing, '访客记录缺少表头：{}，实际：{}'.format(missing, actual)
        assert vp.get_total_count() >= vp.get_row_count()

    @pytest.mark.visitor
    @pytest.mark.parametrize('case', search_cases)
    def test_search_by_name(self, case, logged_driver):
        '''按访客姓名查询，结果条数不超过查询前'''
        vp = VisitorPage(logged_driver).open()
        total_before = vp.get_total_count()
        vp.input_name(case['keyword']).click_search()
        assert vp.get_total_count() <= total_before

    @pytest.mark.visitor
    def test_search_no_result(self, logged_driver):
        '''查询不存在的访客时展示空数据'''
        vp = VisitorPage(logged_driver).open()
        vp.input_name(empty_keyword).click_search()
        assert vp.is_empty() or vp.get_row_count() == 0

    @pytest.mark.visitor
    def test_select_out_visit(self, logged_driver):
        '''是否出访下拉可以筛选，结果条数不超过筛选前'''
        vp = VisitorPage(logged_driver).open()
        total_before = vp.get_total_count()
        vp.select_out_visit(out_visit_options[0]).click_search()
        assert vp.get_total_count() <= total_before

    @pytest.mark.visitor
    def test_date_picker(self, logged_driver):
        '''预约时间段日历面板可以展开，占位符正确'''
        vp = VisitorPage(logged_driver).open()
        assert vp.get_date_placeholders() == date_placeholders
        vp.open_date_picker()
        assert vp.is_date_picker_open()
        assert vp.get_calendar_day_count() > 0

    @pytest.mark.visitor
    def test_pagination(self, logged_driver):
        '''数据超过一页时可以翻页'''
        vp = VisitorPage(logged_driver).open()
        if vp.get_total_count() <= vp.get_row_count():
            pytest.skip('当前数据不足一页，跳过分页用例')
        first_page = vp.get_visitor_names()
        vp.goto_page(2)
        assert vp.get_visitor_names() != first_page

    @pytest.mark.visitor
    def test_row_data(self, logged_driver):
        '''访客记录关键列非空：姓名、手机号、通行区域、是否出访、审批状态'''
        vp = VisitorPage(logged_driver).open()
        assert all(item for item in vp.get_visitor_names())
        assert all(item for item in vp.get_phones())
        assert all(item for item in vp.get_areas())
        assert all(item for item in vp.get_out_visit_statuses())
        assert all(item for item in vp.get_audit_statuses())
