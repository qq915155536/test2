#  ===========================
# -*- coding:utf-8 -*-
# Time :2022/1/29 9:07
# Author :黄丹丹
# QQ:915155536
# File :列表类型.py
#  ===========================

# 1.类型转换(能被for循环遍历的类型：字符串、列表、字典、元组等)
# str='hello'
# str=[1,2,3]
# str={'k1':1,'k2':2}
# str=(1,2,3)
# res=list(str)
# print(res,type(res))

# 2.添加和插入值
# l = [1, 2, 3]
# l.append(4)
# print(l)
# l.insert(0, 9)  # 按索引插入值
# print(l)
# l2=[7,8,9]
# l2='abc'
# l.extend(l2)
# print(l)

# 3.删除
# del l[0]
# print(l)
# l = [1, 2, 3]
# l.pop()
# print(l)
# l = [1, 'abc',2, 3]
# res=l.pop(1)
# print(l,res,type(res))
# l = [1, 'abc',2, 3,[1,2,3]]
# l2=l[:]
# l[4][0]=111
# print(l2)
# print(l[::-1])
# l = [1, 2, 3,1,1]
# print(l.count(10))
# print(l.index(3))
# l=[1,3,3,2,4]
# l.sort()  #只支持同一类型
# print(l)
# l.sort(reverse=True)
# print(l)
# print('a'>'ab')

#队列：先进先出
#堆栈：后进先出