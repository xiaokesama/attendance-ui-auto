import settings
from common import logger


# 开始测试的通用的前后操作
class BaseCase:

    name=None
    logger=logger
    settings=settings

    # 前置条件
    @classmethod
    def setup_class(cls):
        cls.logger.info("=========={}测试开始==========".format(cls.name))

    # 后置条件
    @classmethod
    def teardown_class(cls):
        cls.logger.info("=========={}测试结束==========".format(cls.name))