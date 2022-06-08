#  ===========================
# -*- coding:utf-8 -*-
# Time :2021/11/27 15:06
# Author :A0025-江苏-小丹
# QQ:915155536
# File :db.py
#  ===========================
from ERP.conf import read_ini
import pymysql


class DB:
    def __init__(self, conf):
        """
        设置数据库环境
        :param conf: 数据库环境
        """
        self.conf = conf

    def execute_sql(self,sql):
        """
        :param sql: 待执行sql语句
        :return: 返回执行结果
        """
        # 获取数据库字典配置
        dict = read_ini.read_db_conf(self.conf)
        # print('这里是数据库字典配置：', dict)
        # 连接数据库
        try:
            my_db = pymysql.connect(**dict)
        except:
            print('数据库连接错误！')
        try:
            # 创建游标
            cur = my_db.cursor()
            # 执行sql语句
            cur.execute(sql)
            my_db.commit()
            res = cur.fetchall()
            my_db.close()
            return res
        except:
            print('sql语句执行错误！')

if __name__ == '__main__':
    sql='SELECT person_id FROM user WHERE user_name="cs001"'
    dev_db=DB('dev')
    print(dev_db.execute_sql(sql))
