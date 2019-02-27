# -*- coding: utf-8 -*-

from common.Encapsulation_Excel import readExcel
import os

CASE_ID = 0 #用例ID
CASE_NAME = 1   #用例名称
CASE_METHOD = 2 #请求类型
CASE_URL = 3    #请求地址
CASE_DATA = 4   #用例数据
CASE_STATUS = 5 #用例状态
CASE_KEY = 6    #验证关键字

filedata = os.path.dirname(os.getcwd()) + '\\The_test_case\\q2.xls'

row_num = readExcel(filedata).get_data_nrows()

class CASE():
    ID = readExcel(filedata).get_name(CASE_ID)
    name = readExcel(filedata).get_name(CASE_NAME)
    method = readExcel(filedata).get_name(CASE_METHOD)
    url = readExcel(filedata).get_name(CASE_URL)
    data = readExcel(filedata).get_name(CASE_DATA)
    status = readExcel(filedata).get_name(CASE_STATUS)
    key = readExcel(filedata).get_name(CASE_KEY)



