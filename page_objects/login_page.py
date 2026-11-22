from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage
from page_objects.common_page import CommonPage
from page_locators.login_page_locator import LoginPageLocators as loc


class LoginPage(BasePage):
    '''登录页操作：账号 / 密码 / 验证码登录'''

    name = "登录页"

    def open(self):
        '''
        打开登录页
        :return:page_object
        '''
        self.get(self.settings.PROJECT_HOST + loc.url)
        self.wait_element_is_visible(loc.login_form_loc, '打开登录页')
        return self

    # ---------- 单个元素输入 ----------
    def input_account(self, account):
        '''
        输入账号
        :param account:账号 str
        :return:page_object
        '''
        self.wait_element_is_visible(loc.account_input_loc, '输入账号').send_keys(account)
        return self

    def input_password(self, password):
        '''
        输入密码
        :param password:密码 str
        :return:page_object
        '''
        self.wait_element_is_visible(loc.password_input_loc, '输入密码').send_keys(password)
        return self

    def input_verify_code(self, verify_code):
        '''
        输入验证码
        :param verify_code:验证码 str
        :return:page_object
        '''
        self.wait_element_is_visible(loc.verify_code_input_loc, '输入验证码').send_keys(verify_code)
        return self

    # ---------- 登录方式与协议 ----------
    def is_agreement_checked(self):
        '''
        判断是否已勾选《软件服务协议》与《隐私保护协议》
        :return:bool
        '''
        self.wait_element_is_visible(loc.agree_checkbox_loc, '读取协议勾选状态')
        return self.get_element().is_selected()

    def agree_agreement(self):
        '''
        勾选协议（已勾选时不重复点击）
        :return:page_object
        '''
        if not self.is_agreement_checked():
            self.wait_element_is_clickable(loc.agree_checkbox_loc, '勾选协议').click_element()
        self.delay(0.2)
        return self

    def switch_login_mode(self, mode='验证码登录'):
        '''
        切换登录方式
        :param mode:账号登录 / 验证码登录 str
        :return:page_object
        '''
        locator = (By.XPATH, loc.mode_tab_tpl.format(mode))
        self.wait_element_is_clickable(locator, '切换登录方式{}'.format(mode)).click_element()
        self.delay(0.3)
        return self

    def get_active_mode(self):
        '''
        获取当前选中的登录方式
        :return:str
        '''
        return self.wait_element_is_visible(loc.active_mode_loc, '获取当前登录方式').get_element_text()

    # ---------- 密码框与验证码图片 ----------
    def toggle_password_visible(self):
        '''
        切换密码明文/密文显示
        :return:page_object
        '''
        self.wait_element_is_clickable(loc.password_eye_loc, '切换密码显示状态').click_element()
        return self

    def get_password_input_type(self):
        '''
        获取密码框的 type 属性，用于断言明文/密文
        :return:str
        '''
        return self.wait_element_is_visible(loc.password_input_loc, '读取密码框类型').get_element_attr('type')

    def get_verify_code_img(self):
        '''
        获取验证码图片（base64），便于接入 OCR 或人工识别
        :return:str
        '''
        return self.wait_element_is_visible(loc.verify_img_loc, '获取验证码图片').get_element_attr('src')

    def get_version(self):
        '''
        获取页面底部版本号
        :return:str
        '''
        return self.wait_element_is_visible(loc.version_loc, '获取版本号').get_element_text()

    def get_login_btn_text(self):
        '''
        获取登录按钮文案
        :return:str
        '''
        return self.wait_element_is_visible(loc.login_btn_loc, '获取登录按钮文案').get_element_text()

    # ---------- 登录动作 ----------
    def submit(self):
        '''
        点击登录按钮
        :return:page_object
        '''
        self.wait_element_is_clickable(loc.login_btn_loc, '点击登录按钮').click_element()
        self.wait_page_load()
        return self

    def login(self, account, password, verify_code, agree=True):
        '''
        完整登录流程
        :param account:账号 str
        :param password:密码 str
        :param verify_code:验证码 str
        :param agree:是否勾选协议 bool
        :return:page_object
        '''
        self.input_account(account)
        self.input_password(password)
        self.input_verify_code(verify_code)
        if agree:
            self.agree_agreement()
        self.submit()
        return self

    def get_error_message(self):
        '''
        获取登录失败时的消息提示
        :return:str
        '''
        return CommonPage(self.driver).get_message_text()

    def get_form_error(self):
        '''
        获取表单校验提示，如「请输入帐户名」
        :return:str
        '''
        return self.wait_element_is_visible(loc.form_error_loc, '获取表单校验提示').get_element_text()

