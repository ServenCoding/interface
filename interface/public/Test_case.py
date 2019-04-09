# -*- coding: utf-8 -*-
# @Time    : 2019/1/3  20:16
# @Author  : MrLu！！
# @FileName: Test_case.py
# @Software: PyCharm

import unittest
import xlrd
import xlwt
import json
import os
from interface_global.Global_variable import row_num,CASE
from public_en.Parasing_Excel_data import api_request
from common.yaml import test_environment,test_environment_1
from common.Log import Logger
from common.Assert import asser
from common.write_Excel import Unit
from common import Mysql
from ddt import ddt,unpack,data

logger =Logger(logger='testCase').getlog()

class jie(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logger.info("开始测试")

    def test_(self):
        '''
        接口测试Case
        :return:
        '''
        l = []
        sq = []
        for i in range(0,row_num-1):
            if CASE.data[i] == '':
                if CASE.sql[i] == '':
                   api = api_request(CASE.method[i], test_environment() + CASE.url[i], CASE.data[i])
                   '''
                   获取接口返回状态
                   '''
                   apicode = api.getcode()
                   apicontent = api.get_content()
                   print(type(apicontent))
                   # print(api.gethead)
                   '''
                   将接口返回数据转化为python识别的str
                   '''
                   text1 = json.dumps(apicontent)
                   text = json.loads(text1)
                   '''
                   将返回的数据存到列表中
                   '''
                   l.append(text)
                   '''
                   将返回值转化成dict
                   '''
                   apijson = api.getjson()
                   asser.asser_Equla(self, apicode, 200, "失败")
                   asser.asser_In(self, CASE.status[i], apicontent, "断言失败")
                   if apicode == 200:
                       logger.info("{}.{}:执行成功、数据为:{}、响应码为:{}、断言数据:{}".format(i + 1, CASE.name[i], apijson, apicode,
                                                                              CASE.status))
                       print("{}.{}:执行成功、数据为:{}\t".format(i + 1, CASE.name[i], text))
                       Unit.write_xls(l,sq)
                   else:
                       logger.info('{}.{}:测试失败'.format(i + 1, CASE.name[i]))
                else:
                   api = api_request(CASE.method[i], test_environment_1() + CASE.url[i], CASE.data[i])
                   '''
                   获取接口返回状态
                   '''
                   apicode = api.getcode()
                   apicontent = api.get_content()
                   print(type(apicontent))
                   # print(api.gethead)
                   '''
                   将接口返回数据转化为python识别的str
                   '''
                   text1 = json.dumps(apicontent)
                   text = json.loads(text1)
                   '''
                   将返回的数据存到列表中
                   '''
                   l.append(text)
                   '''
                   将返回值转化成dict
                   '''
                   apijson = api.getjson()
                   asser.asser_Equla(self, apicode, 200, "失败")
                   asser.asser_In(self, CASE.status[i], apicontent, "断言失败")
                   '''
                   执行SQl语句
                   '''
                   mysql = Mysql.MysqlUtil().mysql_dict(CASE.sql[i])
                   # mysql_1 = MysqlUtil.mysql_dict(mysql)
                   sq.append(str(mysql))

                   if apicode == 200:
                       logger.info("{}.{}:执行成功、数据为:{}、响应码为:{}、断言数据:{}、SQL语句为:{}".format(i + 1, CASE.name[i], apijson, apicode,
                                                                              CASE.status,mysql))
                       print("{}.{}:执行成功、数据为:{}\t、SQL语句为:{}".format(i + 1, CASE.name[i], text,mysql))
                       # print("11111")
                       # print(type(l))
                       # print(type(text))
                       # print(type(str(mysql)))
                       # print(type(sq))
                       # print("22222")
                       Unit.write_xls(l,sq)

                   else:
                       logger.info('{}.{}:测试失败'.format(i + 1, CASE.name[i]))
            else:
               if CASE.sql[i] == '':
                    print(1)
                    # for i in range(0, row_num - 1):
                    b = json.loads(CASE.data[i])
                    api = api_request(CASE.method[i], test_environment() + CASE.url[i], b)
                    '''
                    获取接口返回状态
                    '''
                    apicode = api.getcode()
                    apicontent = api.get_content()
                    # print(type(apicontent))
                    # print(type(CASE.data[i]))
                    print(type(CASE.status[i]))
                    '''
                    将接口返回数据转化为python识别的str
                    '''
                    text1 = json.dumps(apicontent)
                    text = json.loads(text)
                    '''
                    将返回的数据存到列表中
                    '''
                    l.append(text)
                    '''
                    将返回值转化成dict
                    '''
                    apijson = api.getjson()
                    asser.asser_Equla(self, apicode, 200, "失败")
                    asser.asser_In(self, CASE.status[i], apicontent, "断言失败")

                    if apicode == 200:
                        logger.info("{}.{}:执行成功、数据为:{}、响应码为:{}、断言数据:{}".format(i + 1, CASE.name[i], apijson, apicode,
                                                                                 CASE.status))
                        print("{}.{}:执行成功、数据为:{}\t".format(i + 1, CASE.name[i], text))
                        Unit.write_xls(l)
                    else:
                        logger.info('{}.{}:测试失败'.format(i + 1, CASE.name[i]))
               else:
                   print(1)
                   # for i in range(0, row_num - 1):
                   b = json.loads(CASE.data[i])
                   api = api_request(CASE.method[i], test_environment() + CASE.url[i], b)
                   '''
                   获取接口返回状态
                   '''
                   apicode = api.getcode()
                   apicontent = api.get_content()
                   # print(type(apicontent))
                   # print(type(CASE.data[i]))
                   print(type(CASE.status[i]))
                   '''
                   将接口返回数据转化为python识别的str
                   '''
                   text1 = json.dumps(apicontent)
                   text = json.loads(text)
                   '''
                   将返回的数据存到列表中
                   '''
                   l.append(text)
                   '''
                   将返回值转化成dict
                   '''
                   apijson = api.getjson()
                   asser.asser_Equla(self, apicode, 200, "失败")
                   asser.asser_In(self, CASE.status[i], apicontent, "断言失败")
                   '''
                   执行SQl语句
                   '''
                   mysql = MysqlUtil.mysql_execute(CASE.sql[i])
                   mysql_1 = MysqlUtil.mysql_dict(mysql)
                   sq.append(mysql_1)

                   if apicode == 200:
                       logger.info("{}.{}:执行成功、数据为:{}、响应码为:{}、断言数据:{}、SQL语句为:".format(i + 1, CASE.name[i], apijson, apicode,
                                                                              CASE.status,CASE.sql))
                       print("{}.{}:执行成功、数据为:{}\t SQL语句为:".format(i + 1, CASE.name[i], text,))
                       Unit.write_xls(l,sq)
                   else:
                       logger.info('{}.{}:测试失败'.format(i + 1, CASE.name[i]))

    @classmethod
    def tearDownClass(cls):
        logger.info("测试结束")


if __name__ == "__name__":
    unittest.main()