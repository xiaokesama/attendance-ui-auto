import pytest

# 考勤组管理表头（真实环境实测）
table_headers = ['考勤组名称', '类型', '人数', '考勤时间', '状态', '生效时间', '操作']

# 操作区按钮
toolbar_buttons = ['新增考勤组']

# 查询用例
search_cases = [
    pytest.param({'keyword': '固定班制'}, marks=pytest.mark.attendance, id='按考勤组名称查询'),
]

# 查不到数据时使用的关键字
empty_keyword = '不存在的考勤组_9527'

# 状态取值
status_values = ['已生效', '未生效']

# 菜单层级（三层）
menu_path = ['考勤管理', '考勤规则设置', '考勤组管理']
