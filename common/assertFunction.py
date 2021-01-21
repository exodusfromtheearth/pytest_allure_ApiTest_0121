# -*- coding: utf-8 -*-
# Author:xtgao
# Filename:assertFunction.py
# Time:2021/1/19 7:00 下午
import json


def assert_func(result, assert_value):
    """设置断言"""
    assert result['code'] == 200, "状态码不等于200"
    if assert_value:
        assert_list = assert_value.split(",")
        for i in assert_list:
            # assert_result = True
            assert i in json.dumps(result, ensure_ascii=False), "断言失败"
