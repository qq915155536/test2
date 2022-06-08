#  ===========================
# -*- coding:utf-8 -*-
# Time :2022/1/27 10:03
# Author :黄丹丹
# QQ:915155536
# File :lol_request.py
#  ===========================
import requests
import os

# 获取英雄id、name等信息
url_main = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}
res_main = requests.get(url=url_main, headers=header)
# print(res.json(),type(res.json()))
hero_dict = res_main.json()
l = hero_dict['hero']  # 英雄信息列表
# print(l)
# 循环遍历英雄id，英雄名字
for i in l:
    hero_id = i['heroId']
    hero_name = i['name'] + '—' + i['title']
    print(hero_id, hero_name)
    print(f'开始抓取《{hero_name}》的皮肤>>>>>>')

    # 新建对应英雄文件路径，用于保存图片
    path = 'lol_skin/' + hero_name
    if not os.path.exists(path):
        os.makedirs(path)
    # 请求英雄皮肤主页
    url_hero = f'https://game.gtimg.cn/images/lol/act/img/js/hero/{hero_id}.js'
    # url_hero = f'https://game.gtimg.cn/images/lol/act/img/js/hero/1.js'
    res1 = requests.get(url_hero)
    # print(res.json())
    skin_list = res1.json()['skins']
    # print(skin_list)
    # 遍历该英雄的皮肤url地址及皮肤名
    for k in skin_list:
        # 如果皮肤url主图为空，则跳过
        if k['mainImg'] == '':
            pass
        else:
            skin_url, skin_name = k['mainImg'], k['name']
            # print(skin_url, skin_name)
            res2 = requests.get(url=skin_url)
            # 图片路径
            jpg_path = path + '/' + r'{}.jpg'.format(skin_name)
            try:
                with open(jpg_path, 'wb') as f:
                    f.write(res2.content)
                    print(f'保存{skin_name}皮肤成功！')
            except:
                with open('lol_skin/失败皮肤日志.txt', 'a', encoding='utf-8') as g:
                    g.write(f'保存{skin_name}皮肤失败！' + '\n')
                continue
