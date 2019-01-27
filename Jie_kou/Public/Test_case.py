# -*- coding: utf-8 -*-
# @Time    : 2019/1/3  20:16
# @Author  : MrLu！！
# @FileName: Test_case.py
# @Software: PyCharm

import unittest
from Jie_kou.Interface_global.Global_variable import row_num,CASE
from Jie_kou.Public_encapsulation.Parasing_Excel_data import api_request
from Jie_kou.common.yaml import test_environment
from Jie_kou.common.Log import Logger
from Jie_kou.common.Assert import asser
from Jie_kou.common.write_Excel import Unit

logger =Logger(logger='testCase').getlog()

class jie(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logger.info("开始测试")

    def test_1(self):
        '''
        接口测试Case1
        :return:
        '''
        for i in range(0,row_num-1):
            api = api_request(CASE.method[i],test_environment()+CASE.url[i],CASE.data[i])
            apicode = api.getcode()
            asser.asser_Equla(self,apicode,200,"失败")
            apijson = api.getjson()
            if apicode == CASE.status[i]:
               logger.info("{}.{}:执行成功、数据为:{}、响应码为:{}".format(i + 1, CASE.name[i], apijson,apicode))
               print(apijson)
               Unit.write_xls(apijson)
            else:
                logger.info('{}.{}:测试失败'.format(i + 1, CASE.name[i]))

    # def test_2(self):
    #     self.url = 'https://www.apiopen.top/satinApi?type=1&page=1'
    #     r = requests.get(self.url)
    #     a = json.loads(r.text)
    #     print(a)
    #     print(r.status_code)
    # 'novelSearchApi?name=盗墓笔记'
    #
    # def test_3(self):
    #     self.url = 'https://www.apiopen.top/login?key=00d91e8e0cca2b76f515926a36db68f5&phone=13594347817&passwd=123456'
    #     r = requests.get(self.url)
    #     a = json.loads(r.text)
    #     print(a)
    #     print(r.status_code)

    @classmethod
    def tearDownClass(cls):
        logger.info("测试结束")

if __name__ == '__main__':
    unittest.main()