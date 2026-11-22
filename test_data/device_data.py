import pytest

# 设备列表表头（真实环境实测，首列为多选框，无表头文案）
table_headers = ['设备名称', '设备区域', '标识号(SN号)', '设备状态', '操作']

# 操作区按钮
toolbar_buttons = ['添加设备', '导入数据', '长期密码']

# 头部按钮
header_buttons = ['更新机构']

# 设备状态下拉选项（真实环境实测）
status_options = ['离线', '在线']

# 查询用例
search_cases = [
    pytest.param({'keyword': 'ceshi'}, marks=pytest.mark.device, id='按设备名称查询'),
]

# 查不到数据时使用的关键字
empty_keyword = '不存在的设备_9527'

# 菜单层级
menu_path = ['设备管理', '设备列表']
