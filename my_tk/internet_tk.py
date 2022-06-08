#  ===========================
# -*- coding:utf-8 -*-
# Time :2021/8/11 18:45
# Author :A0025-江苏-小丹
# QQ:915155536
# File :main.py
#  ===========================
import tkinter

class My_tk:
    def __init__(self):
        self.tk=tkinter.Tk()

    # 设置主窗体
    def main_window(self):
        self.tk.title('疫苗信息管理系统')
        self.tk.geometry('800x500')
        self.tk.mainloop()


    #主窗口
    # def main_window(self):
        # tk.Button(tk, text='登录', bg='white', font=("Arial,12"), width=12, height=1, command=self.login).place(x=260,                                                                                                      y=200)
        # self.tk.Button(self.tk, text='注册', bg='white', font=("Arial,12"), width=12, height=1, command=self.register).place(x=260,                                                                                                                y=240)
        # tk.Button(tk, text='退出', bg='white', font=("Arial,12"), width=12, height=1, command=self.quit_mainloop).place(x=260, y=280)
    #注册界面
    # def register(self):
    #     register = self.tk.Toplevel(app)
    #     register.title('用户注册')
    #     register.geometry("600x400")
    #     tk.Label(register, text="欢迎注册", font=("KaiTi", 40)).place(x=200, y=20)
    #     tk.Label(register, text='添加管理员姓名：', font=("Arial", 9)).place(x=80, y=120)
    #     tk.Label(register, text='确认管理员编号：', font=('Arial', 9)).place(x=80, y=150)
    #     entry1 = tk.Entry(register, font=("Arial, 9"), width=46, )
    #     entry2 = tk.Entry(register, font=("Arial, 9"), width=46, )
    #     entry1.pack()
    #     entry2.pack()
    #     entry1.place(x=180, y=120, width=350, height=25)
    #     entry2.place(x=180, y=150, width=350, height=25)
    #

        # def user_register():
        #     user_name = entry1.get()
        #     user_code = entry2.get()
        #     if user_name == "" or user_code == "":
        #         tkinter.messagebox.showwarning(title="警告", message="用户名或密码不能为空！")
        #     else:
        #         content = "INSERT INTO user_info (user_name, user_code) VALUES ('%s', '%s');" % (user_name, user_code)
        #         self.connect_DBS(database="vaccine_info", content=content)
        #         tkinter.messagebox.showinfo(title="信息", message="注册成功！")
        # tk.Button(register, text="注册", bg='white', font=("Arial,9"), width=12, height=0, command=user_register).place(x=250, y=250)
        #
        #
        # pass
    # def main_loop(self):
    #     self.main_loop()
if __name__ == '__main__':
    test1=My_tk()
    # test1.main_window()
    test1.main_window()

