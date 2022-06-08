#  ===========================
# -*- coding:utf-8 -*-
# Time :2022/1/26 10:45
# Author :黄丹丹
# QQ:915155536
# File :my_gui.py
#  ===========================


import PySimpleGUI as sg

# 参考链接：https://mp.weixin.qq.com/s/ydvlYGjM4k8eUMKOxSUTFA

# 查看所有主题
# sg.preview_all_look_and_feel_themes()

# 切换某一主题
# sg.change_look_and_feel('DarkPurple6')

# 设置主题
sg.theme('DarkAmber')

layout = [
    [sg.Text('用户名：'), sg.Input(key='user')],
    [sg.Text('密  码：'), sg.Input(key='pwd')],
    [sg.Text('你的输入是：'), sg.Text(key='my_text')],
    [sg.Combo(['男','女'])],
    [sg.Button('登录'), sg.Button('退出')]
]

window = sg.Window('我的测试主页', layout=layout,font=('楷体',16),default_element_size=(25,1))

while True:
    event, values = window.read()
    print(event)
    print(values)
    if event in (None, '退出'):
        break
    else:
        window['my_text'].update(values['user'] + '/' + values['pwd'])
window.close()
