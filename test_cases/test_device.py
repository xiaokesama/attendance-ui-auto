import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest

from page_objects.device_page import DevicePage
from page_objects.menu_bar import MenuBar
from test_cases.base_case import BaseCase
from test_data.device_data import empty_keyword, search_cases, status_options, table_headers, toolbar_buttons


class TestDevice(BaseCase):
    name = "设备管理"

    @pytest.mark.success
    @pytest.mark.device
    def test_page_load(self, logged_driver):
        '''通过左侧菜单进入设备列表，标签页与表头正确'''
        dp = DevicePage(logged_driver).open()
        assert DevicePage.tab_name in MenuBar(logged_driver).get_active_tab()
        actual = dp.get_thead_texts()
        missing = [header for header in table_headers if header not in actual]
        assert not missing, '设备列表缺少表头：{}，实际：{}'.format(missing, actual)
        assert dp.get_total_count() >= dp.get_row_count()

    @pytest.mark.device
    def test_toolbar_buttons(self, logged_driver):
        '''操作区按钮与需求一致'''
        dp = DevicePage(logged_driver).open()
        actual = dp.get_toolbar_texts()
        missing = [button for button in toolbar_buttons if button not in actual]
        assert not missing, '操作区缺少按钮：{}，实际：{}'.format(missing, actual)

    @pytest.mark.device
    def test_org_tree(self, logged_driver):
        '''左侧机构树展示且存在节点'''
        dp = DevicePage(logged_driver).open()
        assert dp.is_org_tree_visible()
        assert dp.get_org_tree_texts(), '机构树没有节点'

    @pytest.mark.device
    @pytest.mark.parametrize('case', search_cases)
    def test_search_by_keyword(self, case, logged_driver):
        '''按设备名称/SN号查询，结果条数不超过查询前'''
        dp = DevicePage(logged_driver).open()
        total_before = dp.get_total_count()
        dp.input_keyword(case['keyword']).click_search()
        assert dp.get_total_count() <= total_before

    @pytest.mark.device
    def test_search_by_status(self, logged_driver):
        '''按设备状态筛选后，状态列取值与所选状态一致'''
        dp = DevicePage(logged_driver).open()
        status = status_options[0]
        dp.select_status(status).click_search()
        assert dp.get_row_count() > 0, '按【{}】筛选后没有数据'.format(status)
        statuses = dp.get_statuses()
        assert all(item == status for item in statuses), '状态列存在不一致数据：{}'.format(statuses)

    @pytest.mark.device
    def test_search_no_result(self, logged_driver):
        '''查询不存在的关键字时展示空数据'''
        dp = DevicePage(logged_driver).open()
        dp.input_keyword(empty_keyword).click_search()
        assert dp.is_empty() or dp.get_row_count() == 0

    @pytest.mark.device
    def test_reset(self, logged_driver):
        '''点击重置后查询条件清空，数据恢复'''
        dp = DevicePage(logged_driver).open()
        total_before = dp.get_total_count()
        dp.input_keyword('ceshi').click_search()
        dp.click_reset()
        assert dp.get_total_count() == total_before
