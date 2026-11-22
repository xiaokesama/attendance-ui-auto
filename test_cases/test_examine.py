import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest

from page_objects.examine_page import ExaminePage
from page_objects.menu_bar import MenuBar
from page_locators.list_page_locator import ListPageLocators as list_loc
from test_cases.base_case import BaseCase
from test_data.examine_data import (
    pagination_expected,
    query_button_expected,
    table_headers,
    toolbar_expected,
)


class TestExamine(BaseCase):
    name = "审批管理"

    @pytest.mark.success
    @pytest.mark.examine
    def test_page_load(self, logged_driver):
        '''通过左侧菜单进入我的申请，标签页与表头正确'''
        ep = ExaminePage(logged_driver).open()
        assert ExaminePage.tab_name in MenuBar(logged_driver).get_active_tab()
        actual = ep.get_thead_texts()
        missing = [header for header in table_headers if header not in actual]
        assert not missing, '我的申请缺少表头：{}，实际：{}'.format(missing, actual)

    @pytest.mark.examine
    def test_no_query_and_toolbar(self, logged_driver):
        '''我的申请页是纯列表：没有查询按钮、操作区按钮和分页'''
        ep = ExaminePage(logged_driver).open()
        assert ep.is_element_exist(list_loc.query_btn_loc, timeout=2) is query_button_expected
        assert ep.is_element_exist(list_loc.toolbar_loc, timeout=2) is toolbar_expected
        assert ep.is_element_exist(list_loc.pagination_loc, timeout=2) is pagination_expected

    @pytest.mark.examine
    def test_empty_state(self, logged_driver):
        '''没有申请记录时表格展示空数据，且不报错'''
        ep = ExaminePage(logged_driver).open()
        assert ep.is_empty() or ep.get_row_count() == 0

    @pytest.mark.examine
    def test_status_column(self, logged_driver):
        '''存在申请记录时，状态列非空'''
        ep = ExaminePage(logged_driver).open()
        if ep.get_row_count() == 0:
            pytest.skip('当前账号没有申请记录，跳过状态列校验')
        assert all(item for item in ep.get_statuses())
