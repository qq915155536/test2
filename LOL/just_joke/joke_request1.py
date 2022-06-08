#  ===========================
# -*- coding:utf-8 -*-
# Time :2022/3/6 9:32
# Author :黄丹丹
# QQ:915155536
# File :joke_request.py
#  ===========================
import requests



# 1.360借条
base_headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    'Referer': 'https://www.360jie.com.cn/'
}

url = 'https://mkt.xjietiao.com/activity/pcguide/cdsms'
# params={'mobile':'15557195251'}
params = {
          'mobile': 18983212555,
          'callback': 'jQuery11110481999382197849_1646529884149',
          'terminal': 'eed7868cda31ee3fcc53f930239475e9',
          '_': 1646529884151
          }
res = requests.get(url=url, params=params, headers=base_headers)
print(res.text)
