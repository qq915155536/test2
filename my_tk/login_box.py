#  ===========================
# -*- coding:utf-8 -*-
# Time :2021/8/23 18:48
# Author :A0025-江苏-小丹
# QQ:915155536
# File :login_box.py
#  ===========================
import tkinter as tk

window=tk.Tk()
window.title('登 录 窗 口')
window.geometry('800x500')

#登录图片
canvas=tk.Canvas(window, bg='green', height=260, width=300)
image_file=tk.PhotoImage(file='1.gif')
image=canvas.create_image(0,0,anchor='nw',image=image_file)
canvas.pack(side='top')

#输入框标题
tk.Label(window,text='用户名：').place(x=250,y=300)
tk.Label(window,text='密   码：').place(x=250,y=340)

#输入框
username=tk.StringVar()
username.set('test@qq.com')  #设置默认值
password=tk.StringVar()
tk.Entry(window,textvariable=username).place(x=300,y=300)
tk.Entry(window,textvariable=password,show='*').place(x=300,y=340)

#登录、注册按钮
def login():
    login_window=tk.Toplevel(window)
    login_window.title('登录窗口')
    login_window.geometry('500x500')
    user_name=username.get()
    pwd=password.get()

def register():
    reg_window=tk.Toplevel(window)
    reg_window.title('注册窗口')
    reg_window.geometry('500x500')

tk.Button(window,text='登录',command=login).place(x=310,y=400)
tk.Button(window,text='注册',command=register).place(x=350,y=400)





window.mainloop()