#  ===========================
# -*- coding:utf-8 -*-
# Time :2021/11/11 14:23
# Author :A0025-江苏-小丹
# QQ:915155536
# File :login.py
#  ===========================
import requests
from ERP.log.my_log import my_log

logger = my_log()


# 1.请求相应环境的登录接口，获取登录配置字典
def login(conf):
    """
    :param conf: 环境：'dev','test'
    :return: 登录配置字典info_dict
    """
    # 1）用于盛放接口认证、环境地址
    info_dict = {
        'dev': 'http://dev.zbycorp.com:18888/',
        'test': 'http://test.zbycorp.com:18888/',
        'conf': None,
        'conf_url': None
    }
    try:
        info_dict['conf'] = conf
        info_dict['conf_url'] = info_dict[conf]
    except Exception as e:
        logger.error(f'亲，输入的环境地址:{conf}，有误噢！错误信息{e}')

    # 拼接接口地址
    url = info_dict['conf_url'] + 'bfferp/v2/auth/login'
    # 用户名、密码
    param = {
        "userName": "cs001",
        "password": "123456",
        "device": "3239859756"
    }
    # 基础请求头
    base_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36",
        "Content-Type": "application/json;utf-8"}
    # 请求接口
    res = requests.post(url=url, params=param, headers=base_headers)
    # 接口返回数据处理，加入调拨信息字典
    authorization = (res.json()["data"])
    base_headers["Authorization"] = "Bearer " + authorization
    info_dict['base_headers'] = base_headers
    logger.info(f'{conf}环境登录成功！')
    return info_dict


if __name__ == '__main__':
    # 登录环境（dev|test）
    info = login('dev')
    logger.info(info)
