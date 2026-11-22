from selenium.webdriver.common.by import By


class DevicePageLocators:
    '''设备管理 - 设备列表（/device/generallist）'''

    # 页面路由与标签页名称
    url = '/device/generallist'
    tab_name = '设备列表'

    # 查询区
    org_input_loc = (By.CSS_SELECTOR, 'input[placeholder="请输入机构名称"]')
    keyword_input_loc = (By.CSS_SELECTOR, 'input[placeholder="输入SN号/名称/账号归属/版本查询"]')
    # 设备状态下拉通过表单项标签定位，见 ListPageLocators.select_by_label_tpl
    status_label = '设备状态'

    # 头部按钮
    update_org_btn_tpl = "//button[.//span[contains(text(),'更新机构')]]"

    # 操作区按钮
    add_device_btn_tpl = (
        "//div[contains(@class,'table-operator')]//span[contains(text(),'添加设备')]/ancestor::button[1]"
    )
    import_btn_tpl = (
        "//div[contains(@class,'table-operator')]//span[contains(text(),'导入数据')]/ancestor::button[1]"
    )
    long_password_btn_tpl = (
        "//div[contains(@class,'table-operator')]//span[contains(text(),'长期密码')]/ancestor::button[1]"
    )

    # 左侧机构树
    org_tree_loc = (By.CSS_SELECTOR, '.ant-tree')
    org_tree_node_loc = (By.CSS_SELECTOR, '.ant-tree li .ant-tree-node-content-wrapper')

    # 表格列序（第 1 列为多选框，无表头文案）
    col_name = 2
    col_region = 3
    col_sn = 4
    col_status = 5
    col_operation = 6
