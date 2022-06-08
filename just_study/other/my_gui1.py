#  ===========================
# -*- coding:utf-8 -*-
# Time :2022/1/26 14:29
# Author :黄丹丹
# QQ:915155536
# File :my_gui1.py
#  ===========================
import PySimpleGUI as sg
#主题


print(sg.theme_list())
#控件
a='11'
layout=[
    [sg.Text('请选择你想要的主题👇',font=('楷体',12))],
    [sg.Listbox(sg.theme_list(),key='choice',enable_events=True,font=('楷体',12),size=(20,12))],
    [sg.Text('你选择的主题是：',font=('楷体',12)),sg.Text(None,key='text1',font=('楷体',12))]

]
#窗体
window=sg.Window('切换主题工具',layout=layout)

while True:
    event,values=window.read()
    if event in (None,'Exit'):
        break
    sg.theme(values['choice'][0])
    window['text1'].update(values['choice'][0])
    sg.popup_get_text(values['choice'][0],title='主题预览')


window.close()