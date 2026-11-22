import pytest

# 访客记录表头（真实环境实测）
table_headers = [
    '人员照片',
    '来访单位',
    '访客姓名',
    '手机号码',
    '预约人',
    '被访人手机号',
    '到访时间',
    '通行区域',
    '访问时长',
    '是否出访',
    '审批状态',
    '备注',
    '操作',
]

# 是否出访下拉选项（真实环境实测）
out_visit_options = ['是', '否']

# 预约时间段占位符
date_placeholders = ['开始时间', '结束时间']

# 查询用例
search_cases = [
    pytest.param({'keyword': '苏喂'}, marks=pytest.mark.visitor, id='按访客姓名查询'),
]

# 查不到数据时使用的关键字
empty_keyword = '不存在的访客_9527'

# 菜单层级
menu_path = ['访客管理', '访客记录']
