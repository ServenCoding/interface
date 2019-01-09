# -*- coding: utf-8 -*-

import requests

class api_request():

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

    def getjson(self):
        #获取接口的Json数据
        json_code = self.testapi.json()
        return json_code
