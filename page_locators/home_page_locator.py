from selenium.webdriver.common.by import By


class HomePageLocators:
    '''首页工作台（/dashboard/analysis）：快捷导航、机构信息、考勤统计、操作文档、访客统计'''

    # 页面路由
    url = '/dashboard/analysis'

    # 整体布局
    layout_loc = (By.CSS_SELECTOR, 'section.layout.ant-layout')

    # 左上角 logo 与平台名称
    logo_loc = (By.CSS_SELECTOR, 'aside .logo')
    logo_name_loc = (By.CSS_SELECTOR, 'aside .logo h1')

    # 顶部欢迎语
    welcome_text_loc = (By.XPATH, "//header//span[contains(text(),'欢迎进入')]")

    # 顶部当前用户
    user_dropdown_loc = (By.CSS_SELECTOR, '.user-wrapper .user-dropdown-menu')

    # 顶部侧边栏折叠按钮
    sider_trigger_loc = (By.CSS_SELECTOR, 'header .trigger')

    # 右侧悬浮的「大屏数据」
    big_screen_loc = (By.CSS_SELECTOR, '.floating-icon')

    # 左侧引导模块
    guide_loc = (By.CSS_SELECTOR, '.guide-model')
    guide_btn_loc = (By.CSS_SELECTOR, '.guide-model .floating-button')
    guide_text_loc = (By.CSS_SELECTOR, '.guide-model .floating-button span')

    # 标签页（首页所在的可关闭标签栏）
    tab_bar_loc = (By.CSS_SELECTOR, '.tab-layout-tabs .ant-tabs-tab')
    tab_active_loc = (By.CSS_SELECTOR, '.tab-layout-tabs .ant-tabs-tab-active')
    tab_close_loc = (By.CSS_SELECTOR, '.tab-layout-tabs .ant-tabs-tab .ant-tabs-close-x')

    # 首页容器
    home_page_loc = (By.CSS_SELECTOR, '.home_page')
    card_loc = (By.CSS_SELECTOR, '.home_bg_card')

    # 卡片标题：快捷导航 / 机构信息 / 今日考勤统计 / 操作文档 / 今日访客统计
    card_title_loc = (By.CSS_SELECTOR, '.home_bg_card .centerText')
    card_title_tpl = "//div[contains(@class,'home_bg_card')]//div[contains(@class,'centerText')][contains(.,'{}')]"

    # 快捷导航：设备列表 / 人员列表 / 考勤数据 / 门禁权限 / 访客预约 / 我的审批
    quick_nav_loc = (By.CSS_SELECTOR, '.nave_list .nave_bar')
    quick_nav_text_loc = (By.CSS_SELECTOR, '.nave_list .nave_bar p')
    quick_nav_tpl = "//div[contains(@class,'nave_list')]//div[contains(@class,'nave_bar')][contains(.,'{}')]"

    # 机构信息：部门数量 / 人员数量 / 设备数量 / 访客预约待审批人数
    brand_item_loc = (By.CSS_SELECTOR, '.mechan_lis_detail')
    brand_item_label_loc = (By.CSS_SELECTOR, '.mechan_lis_detail .visitor_pending_label')
    brand_item_tpl = "//div[contains(@class,'mechan_lis_detail')][.//p[contains(text(),'{}')]]"
    brand_item_value_tpl = "//div[contains(@class,'mechan_lis_detail')][.//p[contains(text(),'{}')]]/p[last()]"

    # 机构二维码
    qr_code_loc = (By.CSS_SELECTOR, '#qrCodeImg')
    qr_copy_icon_loc = (By.CSS_SELECTOR, '.code_box .cop_icon')

    # 今日考勤统计：今日人数 / 异常人数
    attendance_loc = (By.CSS_SELECTOR, '.attendance-stats')
    attendance_card_loc = (By.CSS_SELECTOR, '.attendance-stats .stat-card')
    attendance_card_today_loc = (By.CSS_SELECTOR, '.attendance-stats .stat-card.today-people')
    attendance_card_abnormal_loc = (By.CSS_SELECTOR, '.attendance-stats .stat-card.abnormal-people')
    attendance_card_label_loc = (By.CSS_SELECTOR, '.attendance-stats .stat-card .card-label')
    attendance_card_value_loc = (By.CSS_SELECTOR, '.attendance-stats .stat-card .card-value')

    # 考勤指标：已打卡 / 请假 / 未打卡 / 迟到
    indicator_loc = (By.CSS_SELECTOR, '.attendance-indicators .indicator')
    indicator_label_loc = (By.CSS_SELECTOR, '.attendance-indicators .indicator .indicator-label')
    indicator_value_loc = (By.CSS_SELECTOR, '.attendance-indicators .indicator .indicator-value')
    indicator_tpl = "//div[contains(@class,'indicator')][.//span[contains(@class,'indicator-label')][contains(text(),'{}')]]"

    # 今日访客统计：今日(次) / 昨日(次)
    visitor_chart_loc = (By.CSS_SELECTOR, '.page-header-index-wide .canvas')
    visitor_today_loc = (By.CSS_SELECTOR, '.stat-card.purple .card-value')
    visitor_yesterday_loc = (By.CSS_SELECTOR, '.stat-card.cyan .card-value')

    # 操作文档 / 操作视频
    document_loc = (By.CSS_SELECTOR, '.document_flex .document_text')
    document_video_loc = (By.CSS_SELECTOR, '.document_flex .document_video')

    # 更新公告
    update_title_loc = (By.CSS_SELECTOR, '.update_title')
    update_item_loc = (By.CSS_SELECTOR, '.update_box')
    update_item_title_loc = (By.CSS_SELECTOR, '.update_box .update_item_title')
