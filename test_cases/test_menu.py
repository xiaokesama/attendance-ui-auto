import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest

from page_objects.home_page import HomePage
from page_objects.menu_bar import MenuBar
from test_cases.base_case import BaseCase
from test_data.menu_data import (
    expand_cases,
    home_tab_name,
    module_menus,
    three_level_menu,
    top_menus,
)


class TestMenu(BaseCase):
    name = "菜单导航"

    @pytest.mark.success
    @pytest.mark.menu
    def test_top_menus(self, logged_driver):
        '''左侧一级菜单与后台配置一致'''
        HomePage(logged_driver).open()
        menu = MenuBar(logged_driver)
        actual = menu.get_top_menu_texts()
        missing = [name for name in top_menus if name not in actual]
        assert not missing, '左侧缺少菜单：{}，实际展示：{}'.format(missing, actual)

    @pytest.mark.menu
    @pytest.mark.parametrize('case', expand_cases)
    def test_expand_submenu(self, case, logged_driver):
        '''展开一级菜单后展示子菜单，子菜单文案与配置一致'''
        HomePage(logged_driver).open()
        menu = MenuBar(logged_driver)
        menu.expand_submenu(case['menu'])
        actual = menu.get_submenu_texts()
        assert actual, '展开【{}】后未取到子菜单'.format(case['menu'])
        if case['children']:
            missing = [name for name in case['children'] if name not in actual]
            assert not missing, '【{}】缺少子菜单：{}，实际：{}'.format(case['menu'], missing, actual)

    @pytest.mark.menu
    @pytest.mark.parametrize('module,children', list(module_menus.items()))
    def test_module_submenu(self, module, children, logged_driver):
        '''五个业务模块展开后，子菜单与后台配置一致'''
        HomePage(logged_driver).open()
        menu = MenuBar(logged_driver)
        menu.expand_submenu(module)
        actual = menu.get_submenu_texts()
        missing = [name for name in children if name not in actual]
        assert not missing, '【{}】缺少子菜单：{}，实际：{}'.format(module, missing, actual)

    @pytest.mark.menu
    def test_three_level_menu(self, logged_driver):
        '''三层菜单可以逐级展开并展示叶子菜单'''
        HomePage(logged_driver).open()
        menu = MenuBar(logged_driver)
        menu.expand_submenu(three_level_menu['parent'])
        menu.expand_submenu(three_level_menu['child'])
        actual = menu.get_submenu_texts()
        missing = [name for name in three_level_menu['leaves'] if name not in actual]
        assert not missing, '缺少叶子菜单：{}，实际：{}'.format(missing, actual)

    @pytest.mark.menu
    def test_selected_menu(self, logged_driver):
        '''进入首页后左侧菜单「首页」处于选中态'''
        HomePage(logged_driver).open()
        menu = MenuBar(logged_driver)
        assert menu.is_menu_selected(home_tab_name)

    @pytest.mark.menu
    def test_collapse_sider(self, logged_driver):
        '''顶部按钮可以折叠/展开左侧菜单栏'''
        HomePage(logged_driver).open()
        menu = MenuBar(logged_driver)
        before = menu.is_sider_collapsed()
        menu.collapse_sider()
        assert menu.is_sider_collapsed() is not before
        menu.collapse_sider()
        assert menu.is_sider_collapsed() is before

    @pytest.mark.menu
    def test_open_home_tab(self, logged_driver):
        '''首页标签页默认打开且为激活态'''
        HomePage(logged_driver).open()
        menu = MenuBar(logged_driver)
        assert home_tab_name in menu.get_tab_texts()
        assert home_tab_name in menu.get_active_tab()
