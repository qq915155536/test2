#  ===========================
# -*- coding:utf-8 -*-
# Time :2021/9/2 16:32
# Author :A0025-江苏-小丹
# QQ:915155536
# File :my_jsonpath.py
#  ===========================
from jsonpath import jsonpath
import json

# 读取接口响应的json字符串文件1.txt,并转化为dict格式
with open('test.txt', 'r', encoding='utf-8') as f:
    res = json.load(f)
    print(res,type(res))

# 使用jsonpath读取字典里的字段
l = jsonpath(res, '$..snCode')  # 如果取不到返回False
print(l)

