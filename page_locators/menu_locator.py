from selenium.webdriver.common.by import By


class MenuLocators:
    '''公共框架层：左侧菜单栏 + 顶部多标签页'''

    # 左侧菜单容器
    sider_loc = (By.CSS_SELECTOR, 'aside.ant-layout-sider')
    menu_root_loc = (By.CSS_SELECTOR, 'aside .ant-menu-root')

    # 一级菜单（不含子菜单的菜单项 + 带子菜单的菜单标题，按 DOM 顺序取文案）
    top_menu_item_loc = (By.CSS_SELECTOR, 'aside .ant-menu-root > li')

    # 顶部侧边栏折叠按钮
    sider_trigger_loc = (By.CSS_SELECTOR, 'header .trigger')

    # 一级菜单项（无子菜单，如 首页、账号管理）
    menu_item_loc = (By.CSS_SELECTOR, 'aside .ant-menu-root > li.ant-menu-item')
    menu_item_tpl = "//aside//li[contains(@class,'ant-menu-item')][not(contains(@class,'ant-menu-submenu'))][contains(.,'{}')]"

    # 带子菜单的一级菜单标题
    submenu_title_loc = (By.CSS_SELECTOR, 'aside .ant-menu-submenu-title')
    submenu_title_tpl = "//aside//div[contains(@class,'ant-menu-submenu-title')][contains(.,'{}')]"

    # 展开后的子菜单（本项目为三层结构，子节点可能仍是子菜单）
    submenu_item_loc = (By.CSS_SELECTOR, 'aside ul.ant-menu-sub > li')

    # 已展开的子菜单（用于幂等展开）
    submenu_open_tpl = (
        "//aside//li[contains(@class,'ant-menu-submenu-open')]"
        "[./div[contains(@class,'ant-menu-submenu-title')][contains(.,'{}')]]"
    )

    # 叶子菜单链接
    menu_link_tpl = "//aside//a[contains(.,'{}')]"

    # 当前选中的菜单
    selected_menu_loc = (By.CSS_SELECTOR, 'aside .ant-menu-item-selected')

    # 顶部标签页
    tab_loc = (By.CSS_SELECTOR, '.tab-layout-tabs .ant-tabs-tab')
    tab_active_loc = (By.CSS_SELECTOR, '.tab-layout-tabs .ant-tabs-tab-active')
    tab_tpl = "//div[contains(@class,'tab-layout-tabs')]//div[contains(@class,'ant-tabs-tab')][contains(.,'{}')]"
    tab_close_loc = (By.CSS_SELECTOR, '.tab-layout-tabs .ant-tabs-tab .ant-tabs-close-x')
    tab_close_tpl = (
        "//div[contains(@class,'tab-layout-tabs')]//div[contains(@class,'ant-tabs-tab')][contains(.,'{}')]"
        "//i[contains(@class,'ant-tabs-close-x') or contains(@class,'ant-tabs-tab-remove')]"
    )

    # 标签页右键菜单：刷新 / 关闭左侧 / 关闭右侧 / 关闭其它
    tab_context_menu_loc = (By.CSS_SELECTOR, 'ul.contextmenu')
    tab_context_menu_item_loc = (By.CSS_SELECTOR, 'ul.contextmenu .ant-menu-item')
    tab_context_menu_tpl = "//ul[contains(@class,'contextmenu')]//li[contains(@class,'ant-menu-item')][contains(.,'{}')]"
