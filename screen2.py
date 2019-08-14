import tkinter as tk
from tkinter import *

if __name__ == '__main__':
    root = tk.Tk()
    root.wm_title('Entry')
    root.attributes("-fullscreen",1)  # 设置窗口大小  并初始化桌面位置
    #root.resizable(width=True, height=True)  # 宽不可变 高可变  默认True



    fram1 = Frame(root, width = 50)
    e = StringVar()
    e.set('请输入你的密码')
    fram1.grid()
    #fram1.grid_propagate(0)
    Entry(fram1, textvariable=e, show='*').grid()

    fram2 = Frame(root)
    e = StringVar()
    e.set('请输入用户名')
    Entry(fram2, textvariable=e).grid()
    fram2.grid()
    #fram2.grid_propagate(0)

    OKbutton = Button(root,text='OK',anchor = 's', width = 20)
    OKbutton.grid(sticky = 's')

    w = root.winfo_screenwidth()
    if w == 1920:
        img = PhotoImage(file='1.png')
    elif w == 1366:
        img = PhotoImage(file='2.png')
    bkimg = Label(root,image=img)
    bkimg.grid()

    root.mainloop()
