# -*- coding: utf-8 -*-
# Author:xtgao
# Filename:test_02_org.py
# Time:2021/1/20 4:45 下午
import pytest
import sys
from common.requestFunc import req_fun
from common.operationExcel import OperationExcel
from common.logger import atp_log

excel_obj = OperationExcel(2, 'data', 'fa_test.xls')


@pytest.mark.parametrize("value", excel_obj.caserun())
def test_01(value, pytestconfig):
    req_fun(value, pytestconfig)


if __name__ == '__main__':
    atp_log.info('==========FA-Test环境API场景测试==========')
    pytest.main(['-s', 'test_02_org.py'])
