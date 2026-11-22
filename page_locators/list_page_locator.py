from selenium.webdriver.common.by import By


class ListPageLocators:
    '''JeecgBoot 列表页通用元素：查询区、表格、分页、操作区'''

    # 查询区
    search_wrapper_loc = (By.CSS_SELECTOR, '.table-page-search-wrapper')
    query_btn_loc = (By.CSS_SELECTOR, '.table-page-search-submitButtons button.ant-btn-primary')
    reset_btn_tpl = "//span[contains(text(),'重置')]/ancestor::button[1]"

    # 按表单项标签定位下拉框，如 设备状态 / 是否出访
    # 用 [1] 限定第一个匹配项，避免命中表格或分页区中的其他下拉
    select_by_label_tpl = (
        "(//div[contains(@class,'table-page-search-wrapper')]"
        "//div[contains(@class,'ant-form-item')][.//label[contains(text(),'{}')]]"
        "//div[contains(@class,'ant-select-selection')])[1]"
    )
    # 下拉选项
    option_loc = (By.CSS_SELECTOR, '.ant-select-dropdown-menu-item')
    option_tpl = "//li[contains(@class,'ant-select-dropdown-menu-item')][contains(.,'{}')]"

    # 表格
    table_loc = (By.CSS_SELECTOR, '.ant-table')
    thead_loc = (By.CSS_SELECTOR, '.ant-table-thead th')
    row_loc = (By.CSS_SELECTOR, '.ant-table-tbody tr.ant-table-row')
    cell_row_tpl = "//tbody[contains(@class,'ant-table-tbody')]/tr[contains(@class,'ant-table-row')][{}]/td"
    cell_column_tpl = "//tbody[contains(@class,'ant-table-tbody')]/tr[contains(@class,'ant-table-row')]/td[{}]"
    empty_loc = (By.CSS_SELECTOR, '.ant-table-placeholder, .ant-empty')

    # 分页
    pagination_loc = (By.CSS_SELECTOR, '.ant-pagination')
    pagination_item_loc = (By.CSS_SELECTOR, '.ant-pagination-item')
    pagination_item_tpl = (
        "//ul[contains(@class,'ant-pagination')]//li[contains(@class,'ant-pagination-item')][@title='{}']"
    )

    # 操作区
    toolbar_loc = (By.CSS_SELECTOR, '.table-operator')
    toolbar_btn_loc = (By.CSS_SELECTOR, '.table-operator button')
    toolbar_btn_tpl = "//div[contains(@class,'table-operator')]//span[contains(text(),'{}')]/ancestor::button[1]"
