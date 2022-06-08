#  ===========================
# -*- coding:utf-8 -*-
# Time :2021/12/3 15:35
# Author :黄丹丹
# QQ:915155536
# File :pick_complete_new.py
#  ===========================

import requests
from ERP.conf.db import DB
from ERP.login import login


# 1)根据拣货单号，更改拣货方式pda,并查询出拣货单id
def update_is_use_pda(conf,picking_code):
    sql_01 = f"""
            UPDATE zby_wmsdata.wms_picking_bill_main 
            SET is_use_pda = 0
            WHERE picking_code='{picking_code}'
           """
    sql_02 = f"""
            select id 
            from  zby_wmsdata.wms_picking_bill_main
            WHERE picking_code='{picking_code}'
"""
    #生成对应环境的数据库对象
    my_db=DB(conf)
    print(f'执行如下sql>>{sql_01}')

    my_db.execute_sql(sql_01)
    # 查询出拣货单id
    print(f'执行如下sql>>{sql_02}')
    res=my_db.execute_sql(sql_02)
    pick_id = res[0][0]
    l = []
    l.append(pick_id)
    info_dict['pick_id'] = l
    return info_dict


# #2)调用拣货完成接口
def pick_complete(conf_url):
    # 1)拼接接口url
    url = conf_url + 'wmsdata/v1/pickingBill/completePickingBill'
    # 2）入参准备
    data = info_dict['pick_id']
    # 3）请求接口，执行拣货完成操作
    res = requests.post(url=url, headers=info_dict['base_headers'], json=data)
    # 3）接口返回数据处理
    print(res.json())


# 主执行函数
def main_pick(info_dict,picking_code):
    update_is_use_pda(info_dict['conf'],picking_code)
    pick_complete(info_dict['conf_url'])


if __name__ == '__main__':
    # 1)登录指定环境
    # info_dict = login('dev')
    info_dict = login('test')

    # 2）拣货完成主程序
    test_picking_code = 'JHD2022060200156'
    main_pick(info_dict, test_picking_code)

