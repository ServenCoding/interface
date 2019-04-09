# -*- coding: utf-8 -*-
# @Time    : 2019/1/14  21:24
# @Author  : 陆平！！
# @FileName: Mysql.py
# @Software: PyCharm


import MySQLdb
import MySQLdb.cursors

mysql_info = {"host":'8888888888',
              "port":3306,
              "user":"root",
              "passwd":"123456",
              "db":"ssss",
              "charset":"utf8"}
class MysqlUtil():
    '''
    连接数据库信息：mysql_info
    创建数据库游标：mysql_execute
    查询数据中字符串：mysql_string
    查询一组数据：mysql_getrows
    关闭数据库：mysql_close
    查询某个字段对应的字符串：mysql_getstring
    '''
    def __init__(self):
        self.mysql_info = mysql_info
        self.conn = MysqlUtil.__getConnect(self.mysql_info)

    @staticmethod
    def __getConnect(mysql_info):
        '''静态方法,连接数据库'''
        try:
            conn = MySQLdb.connect(host=mysql_info['host'],
                                   port=mysql_info['port'],
                                   user=mysql_info['user'],
                                   passwd=mysql_info['passwd'],
                                   db=mysql_info['db'],
                                   charset=mysql_info['charset'])
            return conn
        except Exception as e:
            print("数据库连接异常:%r" % e)

    def mysql_execute(self,sql):
        '''执行sql'''
        cur = self.conn.cursor()
        try:
            cur.execute(sql)
        except Exception as e:
            '''执行Sql发生异常后,进行回滚'''
            self.conn.rollback()
            print("执行Sql异常：%r" % e)
        else:
            '''执行Sql无异常时关闭并提交'''
            cur.close()
            self.conn.commit()

    def mysql_getrows(self,sql):
        '''返回查询结果'''
        cur = self.conn.cursor()
        try:
            cur.execute(sql)
        except Exception as e:
            print("执行sql语句出现异常：%s" %e)
        else:
            rows = cur.fetchall()
            cur.close()
            return rows

    def mysql_dict(self,sql):
        '''返回查询的字典'''
        cur = self.conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        try:
            cur.execute(sql)
        except Exception as e:
            print("执行Sql语句异常：%s" %e)
        else:
            rows = list(cur.fetchall())
            cur.close()
            return rows

    def mysql_getstring(self,sql):
        '''查询某字段对应值'''
        rows = self.mysql_getrows(sql)
        if rows != None:
            for row in rows:
                for i in row:
                    return i

    def mysql_close(self):
        '''关闭Mysql'''
        try:
            self.conn.close()
        except Exception as e:
            print("关闭数据库异常:%s" %e)

if __name__ == "__main__":
    mysql = MysqlUtil()
    sql = "SELECT * FROM t_hotel_event WHERE id = 1"
    # mysql.mysql_execute(sql)
    print(mysql.mysql_dict(sql))
    print(mysql.mysql_getstring(sql))
    print(mysql.mysql_close())
