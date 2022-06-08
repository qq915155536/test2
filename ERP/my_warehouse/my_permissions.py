#  ===========================
# -*- coding:utf-8 -*-
# Time :2021/8/17 15:26
# Author :A0025-江苏-小丹
# QQ:915155536
# File :my_permissions.py
#  ===========================
import requests
from ERP.login import login
from ERP.conf.db import DB


# 根据输入的用户名，查询出其对应的person_id
def find_person_id(info_dict):
    user_name = input('请输入你要更改权限的用户名 >>>').strip()
    # 拼接sql
    sql = f"SELECT person_id FROM user WHERE user_name='{user_name}'"
    my_db = DB(info_dict['conf'])
    try:
        res = my_db.execute_sql(sql)
        person_id = res[0][0]
        return person_id
    except:
        return '你输入的用户不存在！'


# 根据用户person_id获取其对应的仓库权限
def get_warehouse(info_dict):
    # conf_url:测试环境
    # person_id：人员的person_id
    # 拼接接口地址
    person_id = find_person_id(info_dict)
    url = info_dict['conf_url'] + f'masterdata/v1/userWarehouseAnthority/listWarehouseInfoByPersonId/{person_id}'
    res = requests.post(url=url, headers=info_dict['base_headers'])
    print('该用户的仓库权限如下:')
    print(res.json())


# 更新仓库库权限
def update_warehouse(info_dict, person, warehouse):
    """
    :param info_dict: 登录配置字典
    :param person: 要变更人的person_id列表
    :param warehouse: 赋予权限的仓库id列表
    :return:
    """
    # 拼接接口地址
    url = info_dict['conf_url'] + 'masterdata/v1/userWarehouseAnthority/updateUserWarehouseAnthority'
    # 接口入参
    data = {"defaultWarehouseId": [], "personIdList": person, "warehouseIdList": warehouse}
    # 调用更新仓库权限接口
    res = requests.post(url=url, json=data, headers=info_dict['base_headers'])
    print(res.json())


if __name__ == '__main__':
    # 登录对应测试环境
    info_dict = login('dev')
    # 查询出对应人员的person_id
    # person_id=find_person_id(info_dict)
    # print(type(person_id),person_id)

    # 查询出对应人员的仓库权限
    get_warehouse(info_dict)

    # 更新对应人员的仓库权限
    # person = [1912]
    # warehouse = [26]  # [26-杭州五洲仓,11-FBA仓]
    # update_warehouse(info_dict,person,warehouse)
