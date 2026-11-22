import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest

from page_objects.guard_page import GuardPage
from page_objects.menu_bar import MenuBar
from test_cases.base_case import BaseCase
from test_data.guard_data import empty_keyword, search_cases, table_headers, toolbar_buttons


class TestGuard(BaseCase):
    name = "门禁管理"

    @pytest.mark.success
    @pytest.mark.guard
    def test_page_load(self, logged_driver):
        '''通过左侧菜单进入门禁权限，标签页与表头正确'''
        gp = GuardPage(logged_driver).open()
        assert GuardPage.tab_name in MenuBar(logged_driver).get_active_tab()
        actual = gp.get_thead_texts()
        missing = [header for header in table_headers if header not in actual]
        assert not missing, '门禁权限缺少表头：{}，实际：{}'.format(missing, actual)
        assert gp.get_total_count() >= gp.get_row_count()

    @pytest.mark.guard
    def test_toolbar_buttons(self, logged_driver):
        '''操作区展示「新增权限组」'''
        gp = GuardPage(logged_driver).open()
        assert toolbar_buttons[0] in gp.get_toolbar_texts()

    @pytest.mark.guard
    @pytest.mark.parametrize('case', search_cases)
    def test_search_by_group_name(self, case, logged_driver):
        '''按权限组名称查询，结果条数不超过查询前'''
        gp = GuardPage(logged_driver).open()
        total_before = gp.get_total_count()
        gp.input_group_name(case['keyword']).click_search()
        assert gp.get_total_count() <= total_before

    @pytest.mark.guard
    def test_search_no_result(self, logged_driver):
        '''查询不存在的权限组时展示空数据'''
        gp = GuardPage(logged_driver).open()
        gp.input_group_name(empty_keyword).click_search()
        assert gp.is_empty() or gp.get_row_count() == 0

    @pytest.mark.guard
    def test_permission_row_data(self, logged_driver):
        '''权限组各列数据完整：人员、开放周期、时间、绑定设备均非空'''
        gp = GuardPage(logged_driver).open()
        assert gp.get_group_names(), '权限组名称为空'
        assert all(item for item in gp.get_member_texts())
        assert all(item for item in gp.get_periods())
        assert all(item for item in gp.get_times())
        assert all(item for item in gp.get_bound_devices())

    @pytest.mark.guard
    def test_add_group_button_enabled(self, logged_driver):
        '''「新增权限组」按钮展示且处于可用状态'''
        gp = GuardPage(logged_driver).open()
        assert gp.get_toolbar_texts() == toolbar_buttons
        assert gp.is_toolbar_button_enabled(toolbar_buttons[0])
