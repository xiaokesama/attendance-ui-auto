import pytest

# 登录页基础信息（真实环境实测）
platform_name = '智元云联'
login_btn_text = '登 录'
version_prefix = '当前版本'
login_modes = ['账号登录', '验证码登录']

# 正常登录：验证码由后端返回 base64 图片，自动化时需 OCR 识别或人工回填
success_cases = [
    pytest.param(
        {'account': 'admin', 'password': '123456', 'verify_code': '', 'expect_url': '/dashboard/analysis'},
        marks=pytest.mark.login,
        id='正常账号登录',
    ),
]

# 异常登录：账号或密码错误
# error_type: toast 为服务端返回的消息提示，form 为前端表单校验
fail_cases = [
    pytest.param(
        {'account': 'admin', 'password': 'wrong_password', 'verify_code': '', 'expect_message': '密码', 'error_type': 'toast'},
        marks=[pytest.mark.fail, pytest.mark.login],
        id='密码错误',
    ),
    pytest.param(
        {'account': 'not_exist_user', 'password': '123456', 'verify_code': '', 'expect_message': '用户', 'error_type': 'toast'},
        marks=[pytest.mark.fail, pytest.mark.login],
        id='账号不存在',
    ),
    pytest.param(
        {'account': '', 'password': '123456', 'verify_code': '', 'expect_message': '请输入帐户名', 'error_type': 'form'},
        marks=[pytest.mark.fail, pytest.mark.login],
        id='账号为空',
    ),
]

# 协议勾选文案
agreement_text = '软件服务协议'

# 登录成功后的首页卡片，用于断言登录跳转成功
home_card_title = '快捷导航'
