# -*- coding: utf-8 -*-
# @Time    : 2019/2/27  23:15
# @Author  : 陆平！！
# @FileName: lll.py
# @Software: PyCharm
import sys
import os
import xlrd
import xlwt
# print('hello')
# print(sys.path)
# cur_path = os.path.dirname(os.getcwd())
# attachmentPath = cur_path + '\\report\\'
# attachmentPath1 = cur_path + '\\log\\'
# print(attachmentPath1)
# print(attachmentPath)
#
# saveExcel = os.path.dirname(os.getcwd())
# print(saveExcel)

import requests
# 演示用，一般随便搞个就可以，此地址会返回404，但不影响观看请求体
url = "http://dev.pms.lvyuetravel.com/api/rms/intelligence/holiday/add_hotel_special_holiday.json"

# 折中方案，参数按如下方式组织，也是模拟multipart/form-data的核心
params = {"year":"2019","hotelId":"727","groupId":"0","dateList":[{"holidayStartDate":"2019-10-22",
     "holidayEndDate":"2019-10-22"},
    {"holidayStartDate":"2019-10-23",
     "holidayEndDate":"2019-10-23"}],"dateType":"2"}
print(type(params))

res = requests.post(url, data=params)
# 查看请求体是否符合要求，有具体接口可以直接用具体接口，成功则符合要求，此处主要是演示用
print(res.request.body)
# 查看请求头
print(res.request.headers)
print(res.text)


def info(abc,a,b):
    start = abc.index(a)
    if start>=0:
        start+=len(a)
        end = abc.index(b)
        print(abc[0:start-4])
        return abc[start:end]

aa = info('terlet is good jobs','er','od')
print('11111')
print(aa)
print(222222222222)
for i in range(1,10):
    for v in range(1,i+1):
        print("%d * %d = %d\t" % (v,i,i*v),end=' ')
    print()

print("111111")

s = 0
for i in range(101):
    s = s+i
print(s)




