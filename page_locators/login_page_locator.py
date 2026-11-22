from selenium.webdriver.common.by import By


class LoginPageLocators:
    '''登录页（智元云联）：账号 / 密码 / 验证码 三种登录要素'''

    # 页面路由
    url = '/user/login'

    # 登录表单
    login_form_loc = (By.CSS_SELECTOR, '.user-layout-login')

    # 账号输入框
    account_input_loc = (By.CSS_SELECTOR, '.user-layout-login input[placeholder="请输入帐户名"]')

    # 密码输入框
    password_input_loc = (By.CSS_SELECTOR, '.user-layout-login input[placeholder="请输入密码"]')

    # 验证码输入框
    verify_code_input_loc = (By.CSS_SELECTOR, '.verify-input input[placeholder="请输入验证码"]')

    # 验证码图片
    verify_img_loc = (By.CSS_SELECTOR, '.verify-img img')

    # 密码明文 / 密文切换
    password_eye_loc = (By.CSS_SELECTOR, '.ant-input-password-icon')

    # 协议勾选框
    agree_checkbox_loc = (By.CSS_SELECTOR, '.ant-checkbox-wrapper input.ant-checkbox-input')

    # 登录按钮
    login_btn_loc = (By.CSS_SELECTOR, 'button.login-button')

    # 登录按钮文案（注意按钮文案中间带空格）
    login_btn_text = '登 录'

    # 当前选中的登录方式（账号登录 / 验证码登录）
    active_mode_loc = (By.CSS_SELECTOR, '.login-mode p.active-way')

    # 登录方式切换，用于替换文案：账号登录、验证码登录
    mode_tab_tpl = "//div[contains(@class,'login-mode')]/p[contains(text(),'{}')]"

    # 版本号（当前版本:V2.1）
    version_loc = (By.XPATH, "//*[contains(text(),'当前版本')]")

    # 底部协议链接
    agreement_link_loc = (By.XPATH, "//a[contains(text(),'软件服务协议')]")

    # 表单校验提示（如必填项未填）
    form_error_loc = (By.CSS_SELECTOR, '.ant-form-explain')
