#  ===========================
# -*- coding:utf-8 -*-
# Time :2021/8/14 9:40
# Author :A0025-江苏-小丹
# QQ:915155536
# File :test3.py
#  ===========================
import tkinter as tk
import tkinter.messagebox

# 主窗口
window = tk.Tk()
window.title('My_window')
window.geometry('800x800')

# <<——————————————————————分割线—————————————————————————————>>
# Scale尺度表
l1 = tk.Label(window, bg='yellow', width=20, text='测试')
l1.pack()


# 选择函数
def print_select1(num):
    l1.config(text='你选择的值是：' + num)


# label-名字，from、to—尺度范围，HORIZONTAL—水平显示,length-长度-像素，showvalue-0不显示具体选择的值
# tickinterval-间隔几个单位显示，resolution-保留几位小数，
s = tk.Scale(window, label='try me', from_=1, to=10, orient=tk.HORIZONTAL,
             length=200, showvalue=0, tickinterval=2, resolution=0.1, command=print_select1)
s.pack()

# <<——————————————————————分割线—————————————————————————————>>
# Checkbutton多选框
l2 = tk.Label(window, bg='blue', width=20, text='测试')
l2.pack()

# 选择函数
var1 = tk.IntVar()
var2 = tk.IntVar()


def print_select2():
    if (var1.get() == 1) & (var2.get() == 0):
        l2.config(text='I love only Python')
    elif (var1.get() == 0) & (var2.get() == 1):
        l2.config(text='I love only C++')
    elif (var1.get() == 0) & (var2.get() == 0):
        l2.config(text='I do not love either')
    else:
        l2.config(text='I love only both')


# text-按钮文本，当勾选时，把1复制给variable指定的变量var1
c1 = tk.Checkbutton(window, text='Python', variable=var1, onvalue=1, offvalue=0,
                    command=print_select2)

c2 = tk.Checkbutton(window, text='C++', variable=var2, onvalue=1, offvalue=0,
                    command=print_select2)
c1.pack()
c2.pack()

# <<——————————————————————分割线—————————————————————————————>>
# Canvas 画布

canvas = tk.Canvas(window, bg='green', height=260, width=300)
image_file = tk.PhotoImage(file='1.gif')
# 图片的锚点 钉在指定的坐标
image = canvas.create_image(150, 130, anchor='center', image=image_file)
x0, y0, x1, y1 = 50, 50, 80, 80
# 线
line = canvas.create_line(x0, y0, x1, y1)
# 圆
oval = canvas.create_oval(x0, y0, x1, y1, fill='red')
# 扇形(start、extent,控制扇形的角度)
arc = canvas.create_arc(x0 + 30, y0 + 30, x1 + 30, y1 + 30, start=0, extent=180)
# 正方形
rect = canvas.create_rectangle(100, 30, 100 + 20, 30 + 20)
canvas.pack()


# 移动函数
def move_it():
    # 移动rect,x移动0，y移动2
    canvas.move(rect, 0, 2)


b1 = tk.Button(window, text='move', command=move_it)
# 放置的位置
b1.pack(side='left')
# <<——————————————————————分割线—————————————————————————————>>
# Menubar菜单
l3 = tk.Label(window, bg='red', width=20, text='')
l3.pack()

# 定义点击调用的函数
num = 0


def do_job():
    global num
    l3.config(text='do' + str(num))
    num += 1


# 生成菜单对象
menubar = tk.Menu()
# tearoff:0,1:菜单选项是否可分割
filemenu = tk.Menu(menubar, tearoff=0, )  # 文件菜单
menubar.add_cascade(label='文件', menu=filemenu)
# 文件菜单下拉功能按钮
filemenu.add_command(label='新建', command=do_job)
filemenu.add_command(label='打开', command=do_job)
filemenu.add_command(label='保存', command=do_job)
# 文件菜单分割线
filemenu.add_separator()
filemenu.add_command(label='退出', command=window.quit)

# 停留上层的功能按钮
submenu = tk.Menu(filemenu)
filemenu.add_cascade(label='导入', menu=submenu, underline=0)
submenu.add_command(label='导入文件', command=do_job)

editemenu = tk.Menu(menubar, tearoff=0, )  # 编辑菜单
menubar.add_cascade(label='编辑', menu=editemenu)
# 编辑菜单下拉功能按钮
editemenu.add_command(label='剪切', command=do_job)
filemenu.add_separator()
editemenu.add_command(label='复制', command=do_job)
editemenu.add_command(label='粘贴', command=do_job)

# 把配置好的菜单对象放到窗口上
window.config(menu=menubar)
# <<——————————————————————分割线—————————————————————————————>>
# Frame框架
frm = tk.Frame(window)
frm.pack()
frm_l = tk.Frame(frm)
frm_r = tk.Frame(frm)
frm_l.pack(side='left')
frm_r.pack(side='right')

b2 = tk.Button(frm_l, text=' on the frm_l_1').pack()
b3 = tk.Button(frm_l, text=' on the frm_l_2').pack()
b4 = tk.Button(frm_r, text=' on the frm_r_1').pack()


# <<——————————————————————分割线—————————————————————————————>>
# messagebox弹窗
def my_click():
    # tk.messagebox.showinfo(title='测试窗口',message='showinfo!')
    # tk.messagebox.showwarning(title='测试窗口',message='showwarning！')
    # tk.messagebox.showerror(title='测试窗口',message='showerror！')
    # print(tk.messagebox.askquestion(title='测试窗口', message='askquestion！'))  #return 'yes' ,'no'
    # print(tk.messagebox.askyesno(title='测试窗口', message='askyesno！'))  #return 'True' ,'Fales'
    # print(tk.messagebox.askretrycancel(title='测试窗口', message='askretrycancel！'))  #return 'True' ,'Fales'
    print(tk.messagebox.askokcancel(title='测试窗口', message='askretrycancel！'))  # return 'True' ,'Fales'


b5 = tk.Button(window, text='点 我', command=my_click).pack()

# <<——————————————————————分割线—————————————————————————————>>





window.mainloop()
