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
        i = []
        for c in k:
            i.append(c)
        for m in i:
            return m
        for a in range(len(i)):
            worksheet.write(1,a,str(m))
        saveExcel = os.path.dirname(os.getcwd())+"\\The_test_case\\q3.xls"
        workbook.save(saveExcel)

if __name__ == "__main__":
    Unit.write_xls('sadsadasdasdasaq')



