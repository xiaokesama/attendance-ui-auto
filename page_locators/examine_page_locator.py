from selenium.webdriver.common.by import By


class ExaminePageLocators:
    '''审批管理 - 我的申请（/examine/myapplication）'''

    # 页面路由与标签页名称
    url = '/examine/myapplication'
    tab_name = '我的申请'

    # 该页没有查询区与操作区按钮，只有表格
    # 表格列序
    col_task_type = 1
    col_apply_time = 2
    col_status = 3
    col_operation = 4
