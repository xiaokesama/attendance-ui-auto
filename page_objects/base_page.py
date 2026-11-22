import os
from datetime import datetime
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

from common import logger
import settings


class BasePage:

    name="base页面"
    logger=logger
    settings=settings

    def __init__(self, driver):
        self.driver=driver
        self.element=None
        self.locator=None
        self.action=''

    def get(self,url):
        self.driver.get(url)

    def delay(self,seconds=0.5):
        '''
        延时
        :param seconds:秒
        :return:
        '''
        time.sleep(seconds)
        return self

    def wait_page_load(self):
        '''
        等待页面加载完成
        :param timeout:
        :return:
        '''
        self.driver.implicitly_wait(settings.DEFAULT_IMPLICITLY_WAIT)


    def wait_element_is_visible(self,locator,action='',**kwargs):
        '''
        等待元素可见
        :param locator:定位信息 tuple(by,expression)
        :param action:操作说明 str
        :param kwargs:输入参数 timeout等待时间,poll_frequency轮询时间
        :return:page_object
        '''
        # 类属性定位信息和动作描述为None，则重新赋值，方便传递locator和action到下一个动作,然后点击或者拖动
        self.locator=locator
        self.action=action
        try:
            # 超时时间
            timeout=kwargs.get('timeout',settings.DEFAULT_TIMEOUT)
            # 轮询时间
            poll_frequency=kwargs.get('poll_frequency',0.5)
            # 等待元素可点击，返回元素对象
            self.element=WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.visibility_of_element_located(locator))
        except Exception as e:
            # 出错计入日志
            self.logger.error("在{},{}操作时,等待{}元素【失败】".format(self.name,action,locator))
            # 截图
            self.get_page_screenshot(action)
            raise e
        else:
            # 成功计入日志
            self.logger.debug("在{},{}操作时,等待{}元素【成功】".format(self.name,action,locator))
            # 返回对象
            return self

    def wait_element_is_clickable(self,locator,action='',**kwargs):
        '''
        等待元素可点击
        :param locator:定位信息 tuple(by,expression)
        :param action:操作说明 str
        :param kwargs:输入参数 timeout等待时间,poll_frequency轮询时间
        :return:page_object
        '''
        # 类属性定位信息和动作描述为None，则重新赋值，方便传递locator和action到下一个动作,然后点击或者拖动
        self.locator=locator
        self.action=action
        try:
            # 超时时间
            timeout=kwargs.get('timeout',settings.DEFAULT_TIMEOUT)
            # 轮询时间
            poll_frequency=kwargs.get('poll_frequency',0.5)
            # 等待元素可点击，返回元素对象
            self.element=WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.element_to_be_clickable(locator))
        except Exception as e:
            # 出错计入日志
            self.logger.exception("在{},{}操作时,等待{}元素【失败】".format(self.name,action,locator))
            # 截图
            self.get_page_screenshot(action)
            raise e
        else:
            # 成功计入日志
            self.logger.debug("在{},{}操作时,等待{}元素【成功】".format(self.name,action,locator))
            # 返回对象
            return self

    def wait_element_is_loaded(self,locator,action='',**kwargs):
        '''
        等待元素加载完成
        :param locator:定位信息 tuple(by,expression)
        :param action:操作说明 str
        :param kwargs:输入参数 timeout等待时间,poll_frequency轮询时间
        :return:page_object
        '''
        # 类属性定位信息和动作描述为None，则重新赋值，方便传递locator和action到下一个动作,然后点击或者拖动
        self.locator = locator
        self.action = action
        try:
            # 超时时间
            timeout = kwargs.get('timeout', settings.DEFAULT_TIMEOUT)
            # 轮询时间
            poll_frequency = kwargs.get('poll_frequency', 0.5)
            # 等待元素可点击，返回元素对象
            self.element = WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.presence_of_element_located(locator))
        except Exception as e:
            # 出错计入日志
            self.logger.exception("在{},{}操作时,等待{}元素【失败】".format(self.name, action, locator))
            # 截图
            self.get_page_screenshot(action)
            raise e
        else:
            # 成功计入日志
            self.logger.debug("在{},{}操作时,等待{}元素【成功】".format(self.name, action, locator))
            # 返回对象
            return self

    def send_keys(self,content):
        '''
        输入内容
        :param keys: str
        :return: page_object
        '''
        # 防止wait方法之前调用send_keys方法
        if self.element is None:
            raise RuntimeError("不能在wait方法之前调用元素上的方法")
        try:
            # 清空输入框内容
            self.element.clear()
            # 输入内容
            self.element.send_keys(content)
        except Exception as e:
            # 出错计入日志
            self.logger.exception(
                "在{},{}操作时,对{}元素输入内容{}【失败】".format(self.name,self.action,self.locator,content)
            )
            # 截图
            self.get_page_screenshot(self.action)
            raise e
        else:
            # 成功计入日志
            self.logger.debug(
                "在{},{}操作时,对{}元素输入内容{}【成功】".format(self.name,self.action,self.locator,content)
            )
            # 返回对象
        finally:
            self._clear_cache()

    def get_element(self):
        '''
        获取元素,元素加载完成之后可以获取元素
        :return:
        '''
        if self.element is None:
            raise RuntimeError("不能在wait方法之前调用元素上的方法")
        return self.element

    def click_element(self):
        '''
        点击元素
        :return:
        '''
        if self.element is None:
            raise RuntimeError("不能在wait方法之前调用元素上的方法")
        try:
            self.element.click()
        except Exception as e:
            # 出错计入日志
            self.logger.exception(
                "在{},{}操作时,点击{}元素【失败】".format(self.name,self.action,self.locator)
            )
            # 截图
            self.get_page_screenshot(self.action)
            raise e
        else:
            # 成功计入日志
            self.logger.debug(
                "在{},{}操作时,点击{}元素【成功】".format(self.name,self.action,self.locator)
            )
            # 返回对象
        finally:
            self._clear_cache()

    def click_element_by_js(self):
        '''
        使用js点击元素
        :return:
        '''
        if self.element is None:
            raise RuntimeError("不能在wait方法之前调用元素上的方法")
        try:
            self.driver.execute_script("arguments[0].click();", self.element)
        except Exception as e:
            # 出错计入日志
            self.logger.exception(
                "在{},{}操作时,点击{}元素【失败】".format(self.name,self.action,self.locator)
            )
            # 截图
            self.get_page_screenshot(self.action)
            raise e
        else:
            # 成功计入日志
            self.logger.debug(
                "在{},{}操作时,点击{}元素【成功】".format(self.name,self.action,self.locator)
            )
            # 返回对象
        finally:
            # 操作完成需要清除缓存
            self._clear_cache()

    def get_element_text(self):
        '''
        获取元素文本
        :return:
        '''
        if self.element is None:
            raise RuntimeError("不能在wait方法之前调用元素上的方法")
        try:
            value=self.element.text
        except Exception as e:
            # 出错计入日志
            self.logger.exception(
                "在{},{}操作时,获取{}元素文本【失败】".format(self.name,self.action,self.locator)
            )
            # 截图
            self.get_page_screenshot(self.action)
            raise e
        else:
            # 成功计入日志
            self.logger.debug(
                "在{},{}操作时,获取{}元素文本【成功】".format(self.name,self.action,self.locator)
            )
            # 返回对象
            return value
        finally:
            self._clear_cache()

    def get_element_attr(self,name):
        '''
        获取元素属性
        :param name:属性名称
        :return:属性值
        '''
        if self.element is None:
            raise RuntimeError("不能在wait方法之前调用元素上的方法")
        try:
            value=self.element.get_attribute(name)
        except Exception as e:
            # 出错计入日志
            self.logger.exception(
                "在{},{}操作时,获取{}元素属性{}【失败】".format(self.name,self.action,self.locator,name)
            )
            # 截图
            self.get_page_screenshot(self.action)
            raise e
        else:
            # 成功计入日志
            self.logger.debug(
                "在{},{}操作时,获取{}元素属性{}【成功】".format(self.name,self.action,self.locator,name)
            )
            # 返回对象
            return value
        finally:
            self._clear_cache()

    def switch_to_new_window(self,handle=None,action=''):
        '''
        切换到新窗口
        :param handle:
        :param action:
        :return:
        '''
        try:
            if handle:
                # 切换到新窗口
                self.driver.switch_to.window(handle)
            else:
                # 保存当前窗口
                original_window=self.driver.current_window_handle
                # 循环遍历窗口
                for window_handle in self.driver.window_handles:
                    # 跳过当前窗口
                    if window_handle != original_window:
                        self.driver.switch_to.window(window_handle)
                        break
        except Exception as e:
            # 出错计入日志
            self.logger.exception(
                "在{},{}操作时,切换到新窗口{}【失败】".format(self.name,action,handle)
            )
            # 截图
            self.get_page_screenshot(action)
            raise e
        else:
            # 成功计入日志
            self.logger.debug(
                "在{},{}操作时,切换到新窗口{}【成功】".format(self.name,action,handle)
            )

    # 截屏
    def get_page_screenshot(self,action):
        '''
        截图功能
        获取报错时的页面截图，命名规范： 截图时间_xx页面_xx操作
        :param action:
        :return:
        '''
        img_path=os.path.join(
            self.settings.ERROR_SCREENSHOT_PATH,
            "{}_{}_{}.png".format(
                datetime.now().strftime('%Y-%m-%d_%H-%M-%S'),
                self.name,
                action
            ))
        self.driver.save_screenshot(img_path)
        if self.driver.save_screenshot(img_path):
            self.logger.info("截图成功，截图路径：{}".format(img_path))
        else:
            self.logger.error("截图失败，截图路径：{}".format(img_path))

    def replace_args_by_re(self, json_s, obj):
        '''
        通过正则表达式动态的替换参数
        {"name": "#username#", "age": "#userage#"}  =>  {"name": "admin", "age": "18"}
        :param json_s: 要替换的文本
        :param obj: 带有替换的文本
        :return:
        '''
        # 1.找出所有的槽位中的变量名(若公司项目中#为特殊字符，可将用例和此次#替换为其他特殊符号
        args = re.findall('#(.*?)#', json_s)
        for arg in args:
            # 2.找到obj中对应的属性,若无对应的属性，则返回None
            value = getattr(obj, arg, None)
            if value:
                json_s = json_s.replace('#{}#'.format(arg), str(value))
        return json_s

    def wait_element_is_invisible(self,locator,action='',**kwargs):
        '''
        等待元素不可见/消失
        :param locator:定位信息 tuple(by,expression)
        :param action:操作说明 str
        :param kwargs:输入参数 timeout等待时间,poll_frequency轮询时间
        :return:page_object
        '''
        self.locator = locator
        self.action = action
        try:
            # 超时时间
            timeout = kwargs.get('timeout', settings.DEFAULT_TIMEOUT)
            # 轮询时间
            poll_frequency = kwargs.get('poll_frequency', 0.5)
            WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.invisibility_of_element_located(locator))
        except Exception as e:
            # 出错计入日志
            self.logger.exception("在{},{}操作时,等待{}元素消失【失败】".format(self.name, action, locator))
            # 截图
            self.get_page_screenshot(action)
            raise e
        else:
            # 成功计入日志
            self.logger.debug("在{},{}操作时,等待{}元素消失【成功】".format(self.name, action, locator))
            return self

    def find_elements(self,locator,action=''):
        '''
        查找多个元素，找不到时返回空列表（不抛异常）
        :param locator:定位信息 tuple(by,expression)
        :param action:操作说明 str
        :return:list[WebElement]
        '''
        self.locator = locator
        self.action = action
        try:
            elements = self.driver.find_elements(*locator)
        except Exception as e:
            # 出错计入日志
            self.logger.exception("在{},{}操作时,查找{}元素列表【失败】".format(self.name, action, locator))
            # 截图
            self.get_page_screenshot(action)
            raise e
        else:
            # 成功计入日志
            self.logger.debug(
                "在{},{}操作时,查找{}元素列表【成功】,数量：{}".format(self.name, action, locator, len(elements))
            )
            return elements
        finally:
            self._clear_cache()

    def get_elements_text(self,locator,action=''):
        '''
        获取多个元素的文本
        :param locator:定位信息 tuple(by,expression)
        :param action:操作说明 str
        :return:list[str]
        '''
        elements = self.find_elements(locator, action)
        return [element.text.strip() for element in elements]

    def is_element_exist(self,locator,timeout=2):
        '''
        判断元素是否存在，存在返回True，不存在返回False（不抛异常）
        :param locator:定位信息 tuple(by,expression)
        :param timeout:等待时间 int
        :return:bool
        '''
        try:
            WebDriverWait(self.driver, timeout, 0.5).until(EC.presence_of_element_located(locator))
        except Exception:
            self.logger.debug("判断{}元素是否存在：不存在".format(locator))
            return False
        else:
            self.logger.debug("判断{}元素是否存在：存在".format(locator))
            return True

    def get_current_url(self):
        '''
        获取当前页面url
        :return:str
        '''
        return self.driver.current_url

    def get_title(self):
        '''
        获取当前页面标题
        :return:str
        '''
        return self.driver.title

    def _clear_cache(self):
        '''
        清除缓存
        :return:
        '''
        self.element=None
        self.locator=None
        self.action=''


if __name__ == '__main__':
    from selenium import webdriver
    with webdriver.Chrome() as driver:
        page=BasePage(driver)
        page.driver.get('https://www.baidu.com')


