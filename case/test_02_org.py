# -*- coding: utf-8 -*-
# Author:xtgao
# Filename:test_02_org.py
# Time:2021/1/20 4:45 下午
import pytest
import sys
from common.requestFunc import req_fun
from common.operationExcel import OperationExcel
from common.logger import atp_log
import allure

excel_obj_0 = OperationExcel(0, 'data', 'fa_test.xls')
excel_obj_1 = OperationExcel(1, 'data', 'fa_test.xls')


@allure.feature("测试项目模块")
@pytest.mark.skip(reason="no way of currently testing this")
@pytest.mark.parametrize("value0", excel_obj_0.caserun())
def test_01(value0, pytestconfig):
    req_fun(value0, pytestconfig)


@allure.feature("测试机构模块")
@pytest.mark.parametrize("value1", excel_obj_1.caserun())
def test_02(value1, pytestconfig):
    req_fun(value1, pytestconfig)


if __name__ == '__main__':
    atp_log.info('==========FA-Test环境API场景测试==========')
    pytest.main(['-s', 'test_02_org.py'])
