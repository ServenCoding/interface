# -*- coding: utf-8 -*-
# @Time    : 2019/1/3  20:16
# @Author  : MrLu！！
# @FileName: Test_case.py
# @Software: PyCharm

import unittest
from interface_global.Global_variable import row_num,CASE
from public_en.Parasing_Excel_data import api_request
from common.yaml import test_environment
from common.Log import Logger
from common.Assert import asser
from common.write_Excel import Unit
import json

logger =Logger(logger='testCase').getlog()

class jie(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logger.info("开始测试")

    def test_(self):
        '''
        接口测试Case1
        :return:
        '''
        for i in range(0,row_num-1):
            api = api_request(CASE.method[i],test_environment()+CASE.url[i],CASE.data[i])
            apicode = api.getcode()
            apicontent = api.get_content()
            apijson = api.getjson()
            asser.asser_Equla(self, apicode, 200, "失败")
            asser.asser_In(self, CASE.status[i], apicontent, "断言失败")
            if apicode == 200:
               logger.info("{}.{}:执行成功、数据为:{}、响应码为:{}、断言数据:{}".format(i + 1, CASE.name[i],apijson,apicode,CASE.status))
               print(apicontent)
               Unit.write_xls(apijson)
            else:
                logger.info('{}.{}:测试失败'.format(i + 1, CASE.name[i]))

    @classmethod
    def tearDownClass(cls):
        logger.info("测试结束")