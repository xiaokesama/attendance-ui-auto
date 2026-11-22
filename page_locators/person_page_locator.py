from selenium.webdriver.common.by import By


class PersonPageLocators:
    '''人员列表（/isystem/depart）：左侧部门树 + 右侧人员表格'''

    # 页面路由
    url = '/isystem/depart'

    # 左侧部门树
    dept_search_input_loc = (By.CSS_SELECTOR, 'input[placeholder="请输入部门名称"]')
    add_dept_btn_tpl = "//button[.//span[contains(text(),'添加部门')]]"

    # 查询区
    search_wrapper_loc = (By.CSS_SELECTOR, '.table-page-search-wrapper')
    keyword_input_loc = (
        By.CSS_SELECTOR,
        '.table-page-search-wrapper input[placeholder="请输入姓名/工号/手机号/卡号进行搜索"]',
    )
    person_type_select_loc = (By.CSS_SELECTOR, '.table-page-search-wrapper .ant-select')
    person_type_option_loc = (By.CSS_SELECTOR, '.ant-select-dropdown-menu-item')
    person_type_tpl = "//li[contains(@class,'ant-select-dropdown-menu-item')][contains(.,'{}')]"
    search_btn_loc = (By.CSS_SELECTOR, '.table-page-search-submitButtons button.ant-btn-primary')
    reset_btn_tpl = "//span[contains(text(),'重置')]/ancestor::button[1]"

    # 操作区
    toolbar_loc = (By.CSS_SELECTOR, '.table-operator')
    add_person_btn_tpl = "//div[contains(@class,'table-operator')]//span[contains(text(),'新增人员')]/ancestor::button[1]"
    import_btn_tpl = "//div[contains(@class,'table-operator')]//span[contains(text(),'导入')]/ancestor::button[1]"
    invite_btn_tpl = "//div[contains(@class,'table-operator')]//span[contains(text(),'邀请成员')]/ancestor::button[1]"
    export_btn_tpl = "//div[contains(@class,'table-operator')]//span[contains(text(),'导出')]/ancestor::button[1]"
    download_tpl_btn_tpl = "//button[.//span[contains(text(),'下载模板')]]"

    # 人员表格
    table_loc = (By.CSS_SELECTOR, '.ant-table')
    thead_loc = (By.CSS_SELECTOR, '.ant-table-thead th')
    row_loc = (By.CSS_SELECTOR, '.ant-table-tbody tr.ant-table-row')
    empty_loc = (By.CSS_SELECTOR, '.ant-table-placeholder, .ant-empty')

    # 分页
    pagination_loc = (By.CSS_SELECTOR, '.ant-pagination')
    pagination_total_loc = (By.CSS_SELECTOR, '.ant-pagination-total-text')
    pagination_item_loc = (By.CSS_SELECTOR, '.ant-pagination-item')
    pagination_next_loc = (By.CSS_SELECTOR, '.ant-pagination-next')
