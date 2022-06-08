#  ===========================
# -*- coding:utf-8 -*-
# Time :2021/10/9 14:14
# Author :A0025-江苏-小丹
# QQ:915155536
# File :进度条.py
#  ===========================
import sys
import time
for i in range(1,101):
    print('\r',end='')
    print('进度：{}%：'.format(i),'▋'*(i//4),end='')
    sys.stdout.flush()
    time.sleep(0.05)
