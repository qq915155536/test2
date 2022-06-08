#  ===========================
# -*- coding:utf-8 -*-
# Time :2022/3/14 16:09
# Author :黄丹丹
# QQ:915155536
# File :demo1.py
#  ===========================
import openpyxl
wk=openpyxl.load_workbook('1.xlsx')
print(wk.sheetnames)
ws=wk['my_sheet1']
ws.delete_cols(idx=4,amount=5)
wk.save('1.xlsx')

for i in ws.rows:
    for j in i :
        print(j.value)