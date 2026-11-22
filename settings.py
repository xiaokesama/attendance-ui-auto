import os

# 根目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 测试用例路径
TEST_CASE_DIR = os.path.join(BASE_DIR, 'test_cases')

# 项目域名
PROJECT_HOST= 'http://172.168.80.102'

# url
INTERFACE_URL = {
    'login': '/user/login',
    'dashboard': '/dashboard/analysis',
    'person': '/isystem/depart',
}

# 日志配置
LOG_CONFIG = {
    'name': 'test123',
    'filename': os.path.join(BASE_DIR, 'logs/test123.log'),
    'mode':'a',
    'encoding':'utf-8',
    'debug':True
}

# 隐式等待时间
IMPLICITLY_WAIT = 5

# 超时时间
DEFAULT_TIMEOUT = 10

# 默认隐式等待时间
DEFAULT_IMPLICITLY_WAIT = 10

# 错误截屏路径
ERROR_SCREENSHOT_PATH = os.path.join(BASE_DIR, 'screen_shot')

# 测试账户信息
TEST_NORMAL_USERNAME = '13845621562'
TEST_NORMAL_PASSWORD = '123456'

# 智元云联测试账户信息
TEST_ADMIN_USERNAME = 'admin'
TEST_ADMIN_PASSWORD = '123456'
