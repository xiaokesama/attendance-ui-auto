import tempfile

import pytest
from selenium import webdriver

import settings
from page_objects.home_page import HomePage
from page_locators.home_page_locator import HomePageLocators as home_loc


# 打开浏览器，关闭浏览器。封装操作在这里
@pytest.fixture(scope='class')
def driver():
    with webdriver.Chrome() as wd:
        # 最大化游览器
        wd.maximize_window()
        # 返回游览器对象，不能使用return，return返回之后会关闭游览器，无法进行后续操作
        yield wd


# 未登录的浏览器：独立 user-data-dir，避免复用本机已登录的会话，用于登录页用例
@pytest.fixture(scope='class')
def guest_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--user-data-dir={}'.format(tempfile.mkdtemp(prefix='chrome_guest_')))
    options.add_argument('--start-maximized')
    with webdriver.Chrome(options=options) as wd:
        yield wd


# 已登录的浏览器：直接复用本机浏览器里已有的登录态，未登录时跳过需要登录态的用例
@pytest.fixture(scope='class')
def logged_driver(driver):
    home = HomePage(driver)
    home.get(settings.PROJECT_HOST + settings.INTERFACE_URL['dashboard'])
    home.wait_page_load()
    home.delay(1.5)
    # 登录验证码无法自动识别，因此这里不做自动登录，只校验登录态
    if home.is_login_page():
        pytest.skip('当前浏览器未登录，且登录验证码无法自动识别，跳过需要登录态的用例')
    home.wait_element_is_visible(home_loc.card_title_loc, '等待首页加载完成')
    return driver
