import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest

from page_objects.attendance_page import AttendancePage
from page_objects.menu_bar import MenuBar
from test_cases.base_case import BaseCase
from test_data.attendance_data import empty_keyword, search_cases, table_headers


class TestAttendance(BaseCase):
    name = "考勤管理"

    @pytest.mark.success
    @pytest.mark.attendance
    def test_page_load(self, logged_driver):
        '''通过三层菜单进入考勤组管理，标签页与表头正确'''
        ap = AttendancePage(logged_driver).open()
        assert AttendancePage.tab_name in MenuBar(logged_driver).get_active_tab()
        actual = ap.get_thead_texts()
        missing = [header for header in table_headers if header not in actual]
        assert not missing, '考勤组管理缺少表头：{}，实际：{}'.format(missing, actual)
        assert ap.get_total_count() >= ap.get_row_count()

    @pytest.mark.attendance
    def test_toolbar_buttons(self, logged_driver):
        '''操作区展示「新增考勤组」'''
        ap = AttendancePage(logged_driver).open()
        assert '新增考勤组' in ap.get_toolbar_texts()

    @pytest.mark.attendance
    @pytest.mark.parametrize('case', search_cases)
    def test_search_by_group_name(self, case, logged_driver):
        '''按考勤组名称查询，结果条数不超过查询前'''
        ap = AttendancePage(logged_driver).open()
        total_before = ap.get_total_count()
        ap.input_group_name(case['keyword']).click_search()
        assert ap.get_total_count() <= total_before

    @pytest.mark.attendance
    def test_search_no_result(self, logged_driver):
        '''查询不存在的考勤组时展示空数据'''
        ap = AttendancePage(logged_driver).open()
        ap.input_group_name(empty_keyword).click_search()
        assert ap.is_empty() or ap.get_row_count() == 0

    @pytest.mark.attendance
    def test_group_row_data(self, logged_driver):
        '''考勤组各列数据完整：类型、人数、考勤时间、状态、生效时间均非空'''
        ap = AttendancePage(logged_driver).open()
        assert ap.get_group_names(), '考勤组名称为空'
        assert all(item for item in ap.get_types())
        assert all(item for item in ap.get_person_counts())
        assert all(item for item in ap.get_schedules())
        assert all(item for item in ap.get_statuses())
        assert all(item for item in ap.get_effective_times())

    @pytest.mark.attendance
    def test_reset(self, logged_driver):
        '''点击重置后查询条件清空，数据恢复'''
        ap = AttendancePage(logged_driver).open()
        total_before = ap.get_total_count()
        ap.input_group_name('固定班制').click_search()
        ap.click_reset()
        assert ap.get_total_count() == total_before
