from selenium.webdriver.common.by import By


class GuardPageLocators:
    '''门禁管理 - 门禁权限（/guard/permission）'''

    # 页面路由与标签页名称
    url = '/guard/permission'
    tab_name = '门禁权限'

    # 查询区
    group_input_loc = (By.CSS_SELECTOR, 'input[placeholder="权限组名称"]')

    # 操作区按钮
    add_group_btn_tpl = (
        "//div[contains(@class,'table-operator')]//span[contains(text(),'新增权限组')]/ancestor::button[1]"
    )

    # 表格列序
    col_group_name = 1
    col_members = 2
    col_period = 3
    col_time = 4
    col_devices = 5
    col_operation = 6
