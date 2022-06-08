#  ===========================
# -*- coding:utf-8 -*-
# Time :2021/8/19 14:41
# Author :A0025-江苏-小丹
# QQ:915155536
# File :my_tk3.py
#  ===========================
import tkinter as tk

window=tk.Tk()
window.title('位置摆放')
window.geometry('800x500')

# pack:top-上  bottom-下  left-左  right-右
# tk.Label(window,text='上').pack(side='top')
# tk.Label(window,text='下').pack(side='bottom')
# tk.Label(window,text='左').pack(side='left')
# tk.Label(window,text='右').pack(side='right')

#grid：row-行  column-列
# for i in range(4):
#     for j in range(3):
#         tk.Label(window,text='测试').grid(row=i,column=j,padx=10,pady=10)

# place:x -横坐标，y-纵坐标，anchor(锚点)=‘nw’-把部件的西北角钉在坐标点上
tk.Button(window,text='测试').place(x=10,y=100,anchor='nw')



window.mainloop()