#  ===========================
# -*- coding:utf-8 -*-
# Time :2022/4/20 17:29
# Author :黄丹丹
# QQ:915155536
# File :main.py
#  ===========================
import os

def test():
    os.system('python ./joke_request1.py 1>joke_log.txt')
    os.system('python ./joke_request2.py 1>>joke_log.txt')


if __name__ == '__main__':
    test()
