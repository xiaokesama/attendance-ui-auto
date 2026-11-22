from selenium.webdriver.common.by import By


class CommonLocators:
    '''全站公共组件：消息提示、弹窗、下拉菜单、分页、空数据、加载中'''

    # 顶部全局消息提示
    message_loc = (By.CSS_SELECTOR, '.ant-message-notice')
    message_text_loc = (By.CSS_SELECTOR, '.ant-message-notice-content')

    # 弹窗
    modal_loc = (By.CSS_SELECTOR, '.ant-modal')
    modal_title_loc = (By.CSS_SELECTOR, '.ant-modal-title')
    modal_body_loc = (By.CSS_SELECTOR, '.ant-modal-body')
    modal_ok_loc = (By.CSS_SELECTOR, '.ant-modal-footer button.ant-btn-primary')
    modal_cancel_loc = (By.CSS_SELECTOR, '.ant-modal-footer button.ant-btn-default')
    modal_close_loc = (By.CSS_SELECTOR, '.ant-modal-close')

    # 二次确认框
    confirm_loc = (By.CSS_SELECTOR, '.ant-modal-confirm')
    confirm_title_loc = (By.CSS_SELECTOR, '.ant-modal-confirm-title')
    confirm_ok_loc = (By.CSS_SELECTOR, '.ant-modal-confirm-btns button.ant-btn-primary')

    # 下拉菜单
    dropdown_loc = (By.CSS_SELECTOR, '.ant-dropdown:not(.ant-dropdown-hidden)')
    dropdown_item_loc = (By.CSS_SELECTOR, '.ant-dropdown:not(.ant-dropdown-hidden) .ant-dropdown-menu-item')
    dropdown_item_tpl = "//div[contains(@class,'ant-dropdown')][not(contains(@class,'ant-dropdown-hidden'))]//li[contains(@class,'ant-dropdown-menu-item')][contains(.,'{}')]"

    # 加载中
    spin_loc = (By.CSS_SELECTOR, '.ant-spin-spinning')

    # 空数据
    empty_loc = (By.CSS_SELECTOR, '.ant-empty')
