import openpyxl

# 打开表1，读取对应列数据，存为列表
wk1 = openpyxl.load_workbook(r'C:\Users\zby\Desktop\1.xlsx')
work_sheet1 = wk1['Sheet1']
c1 = work_sheet1['A2':'A25211']
l1 = []
for i in c1:
    l1.append(i[0].value)

# 打开表2，读取对应列数据，存为列表
wk2 = openpyxl.load_workbook(r'C:\Users\zby\Desktop\2.xlsx')
work_sheet2 = wk2['Sheet1']
c2 = work_sheet2['A2':'A24744']
l2 = []
for i in c2:
    l2.append(i[0].value)

# 比对表1、表2数据 （表1包含表2，找出表1中除去表2数据以后，剩下的数据）
for i in l1:
    if i not in l2:
        with open('2.txt', 'a', encoding='utf-8') as f:
            f.write(i + '\n')
