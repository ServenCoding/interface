# -*- coding: utf-8 -*-
# @Time    : 2019/1/25  20:41
# @Author  : 陆平！！
# @FileName: write_Excel.py
# @Software: PyCharm


import xlwt
import os

Title = {"1":["结果如下"]}
class Unit():

    def write_xls(k):
        workbook = xlwt.Workbook(encoding="ascii")
        worksheet = workbook.add_sheet("My_work",cell_overwrite_ok=True)
        num = [x for x in Title]
        num.sort()
        lTitle = []
        for a in num:
            t = [int(a)]
            for b in Title[a]:
                t.append(b)
            lTitle.append(t)
        for i, p in enumerate(lTitle):
            for j, q in enumerate(p):
                worksheet.write(i,j,q)
        worksheet.write(1, 0, label=str(k))
        saveExcel = os.path.dirname(os.getcwd())+"\\The_test_case\\q3.xls"
        workbook.save(saveExcel)




