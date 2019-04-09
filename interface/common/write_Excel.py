# -*- coding: utf-8 -*-
# @Time    : 2019/1/25  20:41
# @Author  : 陆平！！
# @FileName: write_Excel.py
# @Software: PyCharm


import os
import itertools
import xlwt
import xlrd

'''
将接口Response返回一次写入Excel
分别获取初始数据的Excel和写入的Excel路径
'''
filedata = os.path.dirname(os.getcwd()) + '\\The_test_case\\interfaceTest.xlsx'
filedata1 = os.path.dirname(os.getcwd()) + '\\The_test_case\\q1.xls'

class Unit:

    def write_xls(k,c):
        '''
        开始创建Excel
        设置初始页
        :return:
        '''
        wb = xlrd.open_workbook(filedata)
        # 选择sheet页
        sheet1 = wb.sheet_by_index(0)
        # 创建写入文件
        workbook = xlwt.Workbook(encoding="ascii")
        # 创建写入sheet页
        worksheet = workbook.add_sheet("My_work", cell_overwrite_ok=True)
        print("新建成功")
        # 写入excel
        for i in range(0, sheet1.nrows):
            values_row1 = sheet1.row_values(i)
            # print(values_row1)
            for s in range(len(values_row1)):
                worksheet.write(i, s, values_row1[s])
        workbook.save(filedata1)

        '''
        设置宽高
        '''
        col_width = 256*20
        try:
            for i in itertools.count():
                worksheet.col(i).width = col_width
        except ValueError:
            pass
        default_book_style = workbook.default_style
        default_book_style.font.height = 20 * 36

        '''
        获取Response返回的接口输入并写入Excel中
        '''
        t = 1
        for row in k:
           worksheet.write(t,8,row)
           t+= 1
        saveExcel = os.path.dirname(os.getcwd())+"\\The_test_case\\q1.xls"
        workbook.save(saveExcel)

        if c == '':
            pass
        else:
            t_1 = 1
            for row_1 in c:
                worksheet.write(t_1, 9, row_1)
                t_1 += 1
            saveExcel = os.path.dirname(os.getcwd()) + "\\The_test_case\\q1.xls"
            workbook.save(saveExcel)

if __name__ == "__main__":
    aa = [['sadsadasdasdasaq']]
    bb = [['cccccccccccccccc']]
    Unit.write_xls(aa,bb)
