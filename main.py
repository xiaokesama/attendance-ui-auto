import pytest
import settings
import os
from common.tools import get_opts


if __name__ == '__main__':
    args =['-s', '-v', '--alluredir=./reports/temp',settings.TEST_CASE_DIR]
    arg = get_opts('-m')
    if arg:
        args.insert(0,'-m={}'.format(arg))
    arg = get_opts('--browser')
    if arg:
        args.insert(0,'--browser={}'.format(arg))
    pytest.main(args)
    os.system('allure generate ./reports/temp -o ./reports/report --clean')


# python main.py -m=success