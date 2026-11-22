import pytest

# 门禁权限表头（真实环境实测）
table_headers = ['权限组名称', '人员', '开放周期', '时间', '绑定设备', '操作']

# 操作区按钮
toolbar_buttons = ['新增权限组']

# 查询用例
search_cases = [
    pytest.param({'keyword': '1'}, marks=pytest.mark.guard, id='按权限组名称查询'),
]

# 查不到数据时使用的关键字
empty_keyword = '不存在的权限组_9527'

# 菜单层级
menu_path = ['门禁管理', '门禁权限']
