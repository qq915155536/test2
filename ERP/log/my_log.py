#  ===========================
# -*- coding:utf-8 -*-
# Time :2021/12/4 10:26
# Author :黄丹丹
# QQ:915155536
# File :my_log.py
#  ===========================
import logging
import colorlog


def my_log():
    logger =logging.getLogger('test_log')
    #解决日志重复打印问题
    if not logger.handlers:
        #设置日志级别
        logger.setLevel(logging.INFO)
        #设置日志格式器
        #1)普通格式
        # fm='【%(asctime)s】  %(filename)s  【%(levelname)s】  line:%(lineno)d  ——>>%(message)s<<——'
        # fmt=logging.Formatter(fmt=fm)
        #2)颜色格式
        fm='%(log_color)s【%(asctime)s】  %(filename)s  【%(levelname)s】  line:%(lineno)d  | %(message)s'
        fmt=colorlog.ColoredFormatter(fm)
        #设置控制台处理器
        sh=logging.StreamHandler()
        #设置文件处理器
        fh=logging.FileHandler(r'D:\My_Project\test2\ERP\log\log_file\test.log',encoding='utf-8')
        #为处理器设置格式器
        sh.setFormatter(fmt)
        fh.setFormatter(fmt)
        #为日志添加处理器
        logger.addHandler(sh)
        logger.addHandler(fh)
    return logger

if __name__ == '__main__':
    logger=my_log()
    logger.debug('debug')
    logger.info('info')
    logger.warning('warning')
    logger.error('error')
    logger.critical('critical')

