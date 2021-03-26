import os
import pytest
import json
from common.operationJson import depend_list, read_json_file, write_json_file, depend_data_replace
from common.method import req
from common.operationExcel import OperationExcel, ExcelVariables
from common.assertFunction import assert_func
from common.logger import atp_log
import allure
# atp_log.info('==========FA-Test环境API场景测试==========')
excel_obj = OperationExcel(0, 'data', 'fa_test.xls')
run_list = excel_obj.caserun()


@allure.feature("测试项目模块")
@pytest.mark.parametrize("value", run_list)
def test_01(value, pytestconfig):
    """

    @type pytestconfig: 内置 fixture
    """
    # 第一步 处理URL-----------------------------------------------------------------------

    # 读取json文件取出已有的参数
    load_dict = read_json_file('data', 'fa_test.json')
    # 替换url中的参数
    url = pytestconfig.getini('host_url') + value[ExcelVariables.url]
    url = depend_data_replace(url, load_dict)
    atp_log.info('请求地址【%s】' % url)
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
        'Accept': "application/json",
        "Cookie": pytestconfig.getini('cookie')
        # 'Content-Type':'application/json'
    }
    method = value[ExcelVariables.method]

    # 第二步 处理参数  待处理------------------------------------------------------------------
    params = value[ExcelVariables.params]
    if len(str(params).strip()) == 0:
        pass
    elif len(str(params).strip()) > 0:
        if isinstance(params, dict):
            params = json.dumps(params)
        else:
            pass
    params = depend_data_replace(params, load_dict)

    # 第三步 发送请求 -----------------------------------------------------------------------
    r = req.request(url=url, headers=header, params=params, method=method, verify=False)
    result = r.json()

    # 第四步 处理返回结果 -----------------------------------------------------------------------

    # 1/依赖返回数据,   2/依赖返回key值
    dep_data = value[ExcelVariables.depend_data]
    dep_key = value[ExcelVariables.depend_key]
    if dep_key:
        # 输出之后是这样的格式[{'amount_level_id': 99, 'amount_level_name': '待定'}],把depend_dcit存到json文件中
        load_dict2 = depend_list(dep_data, dep_key, result)
        write_json_file('data', 'fa_test.json', load_dict2)

    # 第五步 断言-----------------------------------------------------------------------
    assert_value = value[ExcelVariables.expect]
    assert_func(result, assert_value)
    status_code = result['code']
    atp_log.info('返回状态码【%s】' % status_code)

    #  第六步 将执行结果写入Excel表格--------------------------------------------------------------
    # case_id = value[ExcelVariables.case_id]
    # excel_obj.write_actual_return(status_code, "断言成功", case_id)


if __name__ == "__main__":
    # pytest.main(['--alluredir', './report/raw'])
    # 执行命令 allure generate ./temp -o ./report --clean ，生成测试报告
    # os.system('allure generate ./report/raw -o ./report --clean')
    pytest.main(['-s', 'test_03_funding.py'])
