#  ===========================
# -*- coding:utf-8 -*-
# Time :2022/5/7 11:17
# Author :黄丹丹
# QQ:915155536
# File :purchase.py
#  ===========================

import requests
import datetime
from ERP.login import login
from ERP.log.my_log import my_log

logger = my_log()
info_dict = {}


# 1.生产采购导入
def purchase_add():
    # 去除Content-Type，设置此处需要的headers
    add_headers = info_dict['base_headers']
    del add_headers['Content-Type']
    # 1)拼接接口url
    url = info_dict['conf_url'] + 'purchasedata/v1/purchaseOrder/addByExport'
    # 2）接口参数
    file_data = None
    if info_dict['conf'] == 'dev':
        file_data = {'file': open('生产采购导入模板-dev.xlsx', 'rb')}
    elif info_dict['conf'] == 'test':
        file_data = {'file': open('生产采购导入模板-test.xlsx', 'rb')}
    else:
        logger.error('conf，环境输入有误！')
    # 3）请求接口，导入订单
    logger.info('导入订单进行中>>>  >>>  >>>')
    res = requests.post(url=url, headers=add_headers, files=file_data)
    # 3）接口返回数据处理(断言)
    status = res.json()['status']
    if status == 0:
        logger.info(res.json()['msg'])
    else:
        logger.error(res.json())


# 2.查询出最新的新增的采购订单号：
def ask_purchase_order_code():
    # 1)拼接接口url
    url = info_dict['conf_url'] + 'purchasedata/v1/purchaseOrder/list?pageNo=1&pageSize=1000'
    # 2）接口参数
    # 获取当前日期
    date = str(datetime.date.today())
    data = {
        "companyId": 10,
        "beginDate": date,
        "endDate": date,
        "purchaseType": 900
    }
    # 3）请求接口，查询出最新的一条生产采购订单
    logger.info('查询订单进行中>>>  >>>  >>>')
    res = requests.post(url=url, headers=info_dict['base_headers'], json=data)
    # 4）接口返回数据处理(断言)
    try:
        purchaseordercode = res.json()['data'][0]['purchaseOrderCode']
        logger.info(f'最新的生产采购订单号为：{purchaseordercode}')
    except Exception as e:
        logger.error('查询订单接口失败！', e)


# 主执行函数：
def main_purchase(conf):
    global info_dict
    info_dict = login(conf)
    purchase_add()
    ask_purchase_order_code()


if __name__ == '__main__':
    # 1）导入指定环境的采购订单
    main_purchase('dev')
    # main_purchase('test')
