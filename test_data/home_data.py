import pytest

# 首页卡片标题（真实环境实测）
card_titles = ['快捷导航', '机构信息', '今日考勤统计', '操作文档', '今日访客统计']

# 快捷导航（点击后会打开对应标签页）
quick_nav_names = ['设备列表', '人员列表', '考勤数据', '门禁权限', '访客预约', '我的审批']

# 快捷导航跳转用例，route 为跳转后的路由片段（未知时置为 None，仅校验标签页）
quick_nav_cases = [
    pytest.param(
        {'name': '人员列表', 'route': '/isystem/depart'},
        marks=pytest.mark.smoke,
        id='人员列表',
    ),
    pytest.param({'name': '考勤数据', 'route': None}, marks=pytest.mark.home, id='考勤数据'),
    pytest.param({'name': '访客预约', 'route': None}, marks=pytest.mark.home, id='访客预约'),
]

# 机构信息条目
brand_items = ['部门数量', '人员数量', '设备数量', '访客预约待审批人数']

# 今日考勤统计卡片
attendance_cards = ['today', 'abnormal']
attendance_card_labels = {'today': '今日人数', 'abnormal': '异常人数'}

# 考勤指标
attendance_labels = ['已打卡', '请假', '未打卡', '迟到']

# 今日访客统计
visitor_labels = ['today', 'yesterday']

# 更新公告条数（当前线上为 3 条，断言时使用 >= 1 更稳）
announcement_min_count = 1

# 引导按钮文案
guide_text = '展开指引'

# 顶部信息
platform_name = '智元云联'
welcome_prefix = '欢迎进入'
