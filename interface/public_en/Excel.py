# -*- coding: utf-8 -*-
# @Time    : 2019/1/6  12:27
# @Author  : MrLu！！
# @FileName: Excel.py
# @Software: PyCharm

# from common.Log import run_log as logger
import xlrd

class OperationExcel(object):

    def __init__(self,file_name):
        self.file_name = file_name

    # 获取sheets的内容
    def get_data(self):
        xls = xlrd.open_workbook(self.file_name)
        tables = xls.sheet_by_index(0)
        return tables

    def get_data_nrows(self):
        # 获取Excel总行数
        nrows = self.get_data().nrows
        return nrows

    def get_data_ncols(self):
        # 获取Excel总列数
        ncols = self.get_data().ncols
        return ncols
