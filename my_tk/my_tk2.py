#  ===========================
# -*- coding:utf-8 -*-
# Time :2021/8/17 14:07
# Author :A0025-江苏-小丹
# QQ:915155536
# File :my_tk2.py
#  ===========================
import tkinter as tk

main_window = tk.Tk()
main_window.title('疫苗管理系统')
main_window.geometry('600x400')


def login():
    dl_window = tk.Toplevel(main_window)
    dl_window.title('用户登录')
    dl_window.geometry('600x400')
    tk.Label(dl_window, text="欢迎登录", font=("KaiTi", 40)).place(x=200, y=20)
    tk.Label(dl_window, text='管理员姓名：', font=("Arial", 9)).place(x=80, y=120)
    tk.Label(dl_window, text='管理员编号：', font=('Arial', 9)).place(x=80, y=150)
    entry1 = tk.Entry(dl_window, font=("Arial, 9"), width=46)
    entry2 = tk.Entry(dl_window, font=("Arial, 9"), width=46, show="*")
    entry1.pack()
    entry2.pack()
    entry1.place(x=180, y=120, width=350, height=25)
    entry2.place(x=180, y=150, width=350, height=25)
    dl_window.mainloop()


def register():
    pass


def quit():
    main_window.quit()



tk.Label(main_window,text='欢迎使用',width=24, height=5,font=("Arial,24"),fg='black',bg='blue').pack(side='top')

tk.Button(main_window, text='登录', bg='white', font=("Arial,12"), width=12, height=1, command=login).place(
    x=240, y=200)
tk.Button(main_window, text='注册', bg='yellow', font=("Arial,12"), width=12, height=1, command=register).place(
    x=240, y=240)
tk.Button(main_window, text='退出', bg='violet', font=("Arial,12"), width=12, height=1, command=quit).place(
    x=240, y=280)

if __name__ == '__main__':
    main_window.mainloop()
