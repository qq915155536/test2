#  ===========================
# -*- coding:utf-8 -*-
# Time :2021/11/27 14:08
# Author :A0025-江苏-小丹
# QQ:915155536
# File :read_ini.py
#  ===========================
import configparser

def read_db_conf(environment):
    """
    :param environment: 数据库环境
    :return: 数据库配置字典:conf_dict
    """
    conf=configparser.ConfigParser()
    #读取配置到内存
    #需写绝对路径，若写相对路径，其他地方引用，会报错，找不到配置文件
    conf.read(r'D:\My_Project\test2\ERP\conf\db.ini')
    #读取所有配置信息，元组列表
    res=conf.items(environment)
    #把元组列表转转为字典
    conf_dict=dict(res)
    return conf_dict
    # print(type(conf_dict),conf_dict)

if __name__ == '__main__':
    test_dict=read_db_conf('dev')
    print(test_dict)


