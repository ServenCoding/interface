# -*- coding: utf-8 -*-
# @Time    : 2019/1/7  0:30
# @Author  : MrLu！！
# @FileName: Parasing_Excel_data.py.py
# @Software: PyCharm

import requests
from jie_kou.common.Assert import asser

class api_request(asser):

    def __init__(self,method,url,data):
        self.method = method
        self.url = url
        self.data = data

    @property
    def testapi(self):
        #根据不同的访问方式来访问接口
        try:
            if self.method == 'post':
                if self.data == '':
                    print("没有参数")
                else:
                    result = requests.post(self.url,data=(self.data).encode('utf-8'))

            elif self.method == 'get':
                if self.data == '':
                    result = requests.get(self.url)
                else:
                    result = requests.get(self.url,data=(self.data).encode('utf-8'))

            elif self.method == 'delete':
                if self.data == '':
                    print("没有参数")
                else:
                    result = requests.delete(url=self.url,data=(self.data).encode('utf-8'))

            elif self.method == 'put':
                if self.data == '':
                    print("没有参数")
                else:
                    result = requests.put(url=self.url,data=(self.data).encode('utf-8'))

            return result

        except Exception as e:
            print("失败了:%s" %e)

    def getcode(self):
        #获取接口的状态码
        code = self.testapi.status_code
        return code

    def get_content(self):
        #获取返回报文
        content = self.testapi.text
        return content


    def getjson(self):
        #获取接口的Json数据
        json_code = self.testapi.json()
        return json_code
