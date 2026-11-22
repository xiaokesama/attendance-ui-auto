from selenium.webdriver.common.by import By


class AttendancePageLocators:
    '''考勤管理 - 考勤规则设置 - 考勤组管理（/attendance/rules）'''

    # 页面路由与标签页名称
    url = '/attendance/rules'
    tab_name = '考勤组管理'

    # 查询区
    group_input_loc = (By.CSS_SELECTOR, 'input[placeholder="考勤组名称"]')

    # 操作区按钮
    add_group_btn_tpl = (
        "//div[contains(@class,'table-operator')]//span[contains(text(),'新增考勤组')]/ancestor::button[1]"
    )

    # 表格列序
    col_group_name = 1
    col_type = 2
    col_persons = 3
    col_schedule = 4
    col_status = 5
    col_effective_time = 6
    col_operation = 7
