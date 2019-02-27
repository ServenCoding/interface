# -*- coding: utf-8 -*-
# @Time    : 2019/2/27  18:33
# @Author  : 陆平！！
# @FileName: Assert.py
# @Software: PyCharm

import unittest
from .Log import Logger as logger
import json

logger = logger(logger="Assert").logger

class asser(unittest.TestCase):

    def asser_Equla(self,parameter,validation,msg):
        '''
        断言相等
        :param parameter:
        :param validation:
        :param msg:
        :return:
        '''
        try:
            logger.info("断言相等开始：%r == %r" %(parameter,validation))
            self.assertEqual(parameter,validation,msg=msg)
            logger.info('断言成功：%r == %r' %(parameter,validation))
        except Exception as e:
            logger.info("断言相等失败:%s" %e)

    def asser_In(self, parameter, validation, msg):
        '''
        断言parameter是否在validation中
        :param parameter:
        :param validation:
        :param msg:
        :return:
        '''
        try:
            logger.info("断言parameter是否在validation中：%r In %r" % (parameter, validation))
            self.assertIn(parameter, validation, msg=msg)
            logger.info('断言成功：%r 在 %r' % (parameter, validation))
        except Exception as e:
            logger.info(" 断言parameter是否在validation中失败:%r" % e)

    def asser_NotEqual(self,parameter,validation,msg):
        '''
        断言不相等
        :param parameter:
        :param validation:
        :param msg:
        :return:
        '''
        try:
            logger.info("断言不相等开始：%r == %r" %parameter%validation)
            self.assertNotEqual(parameter,validation,msg=msg)
        except Exception as e:
            logger.info("断言不相等:%s" %e)

    def asser_True(self,parameter,msg):
        '''
        断言参数等于True
        :param parameter:
        :param msg:
        :return:
        '''
        try:
            logger.info("断言参数等于True：%r == True" %parameter)
            self.assertTrue(parameter,msg=msg)
        except Exception as e:
            logger.info("断言参数等于True失败:%s" %e)

    def asser_False(self,parameter,msg):
        '''
        断言参数等于Fales
        :param parameter:
        :param msg:
        :return:
        '''
        try:
            logger.info("断言参数等于Fales：%r == False" %parameter)
            self.assertFalse(parameter,msg=msg)
        except Exception as e:
            logger.info("断言参数不等于False失败:%s" %e)

    def asser_Is(self,parameter,validation,msg):
        '''
        断言parameter是否存在validation里
        :param parameter:
        :param validation:
        :param msg:
        :return:
        '''
        try:
            logger.info("断言parameter是否存在validation里：%r is %r" %parameter%validation)
            self.assertIs(parameter,validation,msg=msg)
        except Exception as e:
            logger.info("断言parameter是否存在validation里失败:%s" %e)

    def asser_NotIs(self,parameter,msg):
        '''
        断言parameter是否为空
        :param parameter:
        :param validation:
        :param msg:
        :return:
        '''
        try:
            logger.info("断言parameter是否为空：%r == None" %parameter)
            self.assertIsNotNone(parameter,msg=msg)
        except Exception as e:
            logger.info(" 断言parameter是否为空失败:%s" %e)