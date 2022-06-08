#  ===========================
# -*- coding:utf-8 -*-
# Time :2021/9/2 15:17
# Author :A0025-江苏-小丹
# QQ:915155536
# File :test.json.py
#  ===========================

import json

with open('user_data/1.json','w',encoding='utf-8') as f:
    d={
        'name':'zhang',
        'age':18
    }
    json.dump(d,f)

with open('user_data/1.json','r',encoding='utf-8') as f:
    d=json.load(f)
    age=d['age']
    print(type(age),age)
    print(type(d),d)
