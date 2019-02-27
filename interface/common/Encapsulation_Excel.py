# -*- coding: utf-8 -*-

from public_en.Excel import OperationExcel

class readExcel(OperationExcel):

    # 分别获取每一列的数值
    def get_name(self, column_numerical):
        if column_numerical <= self.get_data_ncols():
            ColumnName = []
            for i in range(1, self.get_data_nrows()):
                ColumnName.append(self.get_data().cell_value(i, column_numerical))
            return ColumnName
        else:
            print("输入的column_numerical不合法！")
