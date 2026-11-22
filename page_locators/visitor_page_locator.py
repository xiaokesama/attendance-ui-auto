from selenium.webdriver.common.by import By


class VisitorPageLocators:
    '''访客管理 - 访客记录（/visitor/visitorlist）'''

    # 页面路由与标签页名称
    url = '/visitor/visitorlist'
    tab_name = '访客记录'

    # 查询区
    name_input_loc = (By.CSS_SELECTOR, 'input[placeholder="姓名"]')
    # 预约时间段（日期区间）
    start_date_loc = (By.XPATH, "(//input[contains(@class,'ant-calendar-range-picker-input')])[1]")
    end_date_loc = (By.XPATH, "(//input[contains(@class,'ant-calendar-range-picker-input')])[2]")
    date_picker_loc = (By.CSS_SELECTOR, '.ant-calendar-picker')
    picker_panel_loc = (By.CSS_SELECTOR, '.ant-calendar-picker-container')
    calendar_day_loc = (By.CSS_SELECTOR, '.ant-calendar-date')
    # 是否出访下拉通过表单项标签定位，见 ListPageLocators.select_by_label_tpl
    out_visit_label = '是否出访'

    # 表格列序
    col_photo = 1
    col_company = 2
    col_visitor_name = 3
    col_phone = 4
    col_booker = 5
    col_host_phone = 6
    col_arrive_time = 7
    col_area = 8
    col_duration = 9
    col_out_visit = 10
    col_audit_status = 11
    col_remark = 12
    col_operation = 13
