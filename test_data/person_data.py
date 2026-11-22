import pytest

# 人员列表表头（真实环境实测，已去掉多选框列的空表头）
table_headers = ['注册照片', '姓名', '部门', '手机号码', '卡号', '工号', '名单状态', '人员类型', '操作']

# 操作区按钮
toolbar_buttons = ['新增人员', '导入', '邀请成员', '导出', '人员下发', '名单类型']

# 查询关键字用例
search_cases = [
    pytest.param({'keyword': '张'}, marks=pytest.mark.person, id='按姓名查询'),
    pytest.param({'keyword': '13000000000'}, marks=pytest.mark.person, id='按手机号查询'),
    pytest.param({'keyword': 'EMP001'}, marks=pytest.mark.person, id='按工号查询'),
]

# 查不到数据时使用的关键字
empty_keyword = '自动化测试_不存在的员工_9527'

# 人员列表路由
person_route = '/isystem/depart'

# 新增人员弹窗相关文案
add_person_btn_text = '新增人员'

# 部门树输入框占位符
dept_placeholder = '请输入部门名称'

# 查询输入框占位符
keyword_placeholder = '请输入姓名/工号/手机号/卡号进行搜索'
