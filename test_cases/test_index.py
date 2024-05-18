import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from page_objects.index_page import IndexPage
from test_cases.base_case import BaseCase
import pytest

from test_data.index_data import success_cases


class TestIndex(BaseCase):
    name = "登录功能"

    @pytest.mark.success
    @pytest.mark.parametrize('case', success_cases)
    def test_search(self,case,driver):
        driver.get("https://www.baidu.com")
        ip = IndexPage(driver)
        ip.search(case['name'])
        assert ip.driver.title == case['title']