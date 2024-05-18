import pytest

success_cases = [
{
    'title':'章子怡_百度搜索',
    'name':'章子怡'
},
pytest.param({
    'title':'章子怡_百度搜索',
    'name':'章子怡'
},marks=pytest.mark.first)
]
success_cases[0]=pytest.param(success_cases[0],marks=pytest.mark.first)
