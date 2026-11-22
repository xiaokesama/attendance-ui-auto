import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest

from page_objects.common_page import CommonPage
from page_objects.person_page import PersonPage
from test_cases.base_case import BaseCase
from test_data.person_data import empty_keyword, search_cases, table_headers, toolbar_buttons


class TestPerson(BaseCase):
    name = "人员列表"

    @pytest.mark.success
    @pytest.mark.person
    def test_page_load(self, logged_driver):
        '''人员列表加载完成，表头与数据正常展示'''
        pp = PersonPage(logged_driver).open()
        pp.wait_table_loaded()
        actual = pp.get_thead_texts()
        missing = [header for header in table_headers if header not in actual]
        assert not missing, '人员列表缺少表头：{}，实际展示：{}'.format(missing, actual)
        assert pp.get_total_count() >= pp.get_row_count()

    @pytest.mark.person
    def test_toolbar_buttons(self, logged_driver):
        '''操作区按钮与需求一致'''
        pp = PersonPage(logged_driver).open()
        pp.wait_table_loaded()
        actual = pp.get_toolbar_texts()
        missing = [button for button in toolbar_buttons if button not in actual]
        assert not missing, '操作区缺少按钮：{}，实际展示：{}'.format(missing, actual)

    @pytest.mark.person
    @pytest.mark.parametrize('case', search_cases)
    def test_search(self, case, logged_driver):
        '''按姓名/手机号/工号查询，结果条数不超过查询前'''
        pp = PersonPage(logged_driver).open()
        pp.wait_table_loaded()
        total_before = pp.get_total_count()
        pp.input_keyword(case['keyword'])
        pp.click_search()
        assert pp.get_total_count() <= total_before

    @pytest.mark.person
    def test_search_no_result(self, logged_driver):
        '''查询不存在的关键字时展示空数据'''
        pp = PersonPage(logged_driver).open()
        pp.wait_table_loaded()
        pp.input_keyword(empty_keyword)
        pp.click_search()
        assert pp.is_empty() or pp.get_row_count() == 0

    @pytest.mark.person
    def test_reset_search(self, logged_driver):
        '''点击重置后查询条件被清空'''
        pp = PersonPage(logged_driver).open()
        pp.wait_table_loaded()
        pp.input_keyword('张')
        pp.click_reset()
        assert not pp.get_keyword()

    @pytest.mark.person
    def test_pagination(self, logged_driver):
        '''总条数超过一页时可以翻页'''
        pp = PersonPage(logged_driver).open()
        pp.wait_table_loaded()
        if pp.get_total_count() <= pp.get_row_count():
            pytest.skip('当前数据不足一页，跳过分页用例')
        first_page = pp.get_person_names()
        pp.goto_page(2)
        assert pp.get_person_names() != first_page

    @pytest.mark.smoke
    @pytest.mark.person
    def test_add_person_modal(self, logged_driver):
        '''点击新增人员打开表单弹窗，取消后可正常关闭'''
        pp = PersonPage(logged_driver).open()
        pp.wait_table_loaded()
        pp.click_add_person()
        common = CommonPage(logged_driver)
        assert common.is_modal_visible()
        common.click_modal_cancel()
        common.delay(0.5)
        assert not common.is_modal_visible()
