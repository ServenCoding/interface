# -*- coding: utf-8 -*-
# @Time    : 2019/1/9  20:02
# @Author  : MrLu！！
# @FileName: Run_Set.py
# @Software: PyCharm

import time
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from public_en.Email import Mail
from HTMLTestRunner3 import HTMLTestRunner
import unittest
def report():
    if len(sys.argv) > 1:
        report_name = os.path.dirname(os.getcwd()) + '\\report\\'  + sys.argv[1] + '_result.html'
        print(report_name)
    else:
        now = time.strftime("%Y-%m-%d_%H_%M_%S_")
        report_name = os.path.dirname(os.getcwd()) + '\\report\\'+now+'Interface_Report.html'
        print(report_name)

    return report_name

if __name__=="__main__":
    fp = open (report(), 'wb')
    runner = HTMLTestRunner(stream=fp,
        title=u'Interface报告',description=u"环境: ")
    os_discover = os.path.dirname(os.path.abspath('.'))
    discover = unittest.defaultTestLoader.discover (os_discover + '\\public\\',
                                                    pattern="Test_case.py")
    runner.run (discover)
    Mail("plu@ling-ban.com").mail_outbox()
    fp.close ()
