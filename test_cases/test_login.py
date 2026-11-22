import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest

from page_objects.login_page import LoginPage
from test_cases.base_case import BaseCase
from test_data.login_data import fail_cases, login_btn_text, login_modes, success_cases, version_prefix


class TestLogin(BaseCase):
    name = "登录功能"

    @pytest.mark.success
    @pytest.mark.login
    def test_login_page_load(self, guest_driver):
        '''登录页默认展示账号登录，且版本号、登录按钮展示正常'''
        lp = LoginPage(guest_driver).open()
        assert lp.get_active_mode() in login_modes
        assert version_prefix in lp.get_version()
        assert lp.get_login_btn_text() == login_btn_text

    @pytest.mark.login
    def test_verify_code_img(self, guest_driver):
        '''验证码图片以 base64 返回，便于接入 OCR 识别'''
        lp = LoginPage(guest_driver).open()
        assert lp.get_verify_code_img().startswith('data:image')

    @pytest.mark.login
    def test_password_eye(self, guest_driver):
        '''点击小眼睛后，密码框在密文与明文之间切换'''
        lp = LoginPage(guest_driver).open()
        assert lp.get_password_input_type() == 'password'
        lp.toggle_password_visible()
        assert lp.get_password_input_type() == 'text'

    @pytest.mark.login
    def test_agree_agreement(self, guest_driver):
        '''协议勾选状态可以切换'''
        lp = LoginPage(guest_driver).open()
        assert lp.is_agreement_checked() is False
        lp.agree_agreement()
        assert lp.is_agreement_checked() is True

    @pytest.mark.login
    def test_switch_login_mode(self, guest_driver):
        '''可以在账号登录与验证码登录之间切换'''
        lp = LoginPage(guest_driver).open()
        lp.switch_login_mode('验证码登录')
        assert lp.get_active_mode() == '验证码登录'

    @pytest.mark.success
    @pytest.mark.login
    @pytest.mark.parametrize('case', success_cases)
    def test_login_success(self, case, guest_driver):
        '''登录成功：验证码依赖 OCR 或人工回填，未回填时跳过'''
        if not case['verify_code']:
            pytest.skip('验证码未配置：请在 test_data/login_data.py 中回填识别结果')
        lp = LoginPage(guest_driver).open()
        lp.login(case['account'], case['password'], case['verify_code'])
        assert case['expect_url'] in lp.get_current_url()

    @pytest.mark.fail
    @pytest.mark.login
    @pytest.mark.parametrize('case', fail_cases)
    def test_login_fail(self, case, guest_driver):
        '''登录失败：前端表单校验可直接断言，服务端校验需要验证码'''
        if case['error_type'] == 'toast' and not case['verify_code']:
            pytest.skip('验证码未配置：请在 test_data/login_data.py 中回填识别结果')
        lp = LoginPage(guest_driver).open()
        lp.login(case['account'], case['password'], case['verify_code'])
        if case['error_type'] == 'form':
            assert case['expect_message'] in lp.get_form_error()
        else:
            assert case['expect_message'] in lp.get_error_message()
