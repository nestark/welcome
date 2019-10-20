from tkinter import *
from tkinter import messagebox
from os import makedirs, path, system
import ctypes
import win32api, win32gui
from win32con import WM_INPUTLANGCHANGEREQUEST


class CanvasButton:
    def __init__(self, canvas):
        self.canvas = canvas
        '''self.number = IntVar()'''
        self.createWidgets(canvas)
        self.capslockdetect()
        self.Hide = 1  # Flag for pwInput status
        self.change_Input()
        self.option = StringVar()  # option String for newpage button
        self.right_menu(canvas)

    def createWidgets(self, canvas):
        self.e = StringVar()
        self.vcmd=(canvas.register(self.callback))
        '''self.e.set('Enter your username')'''
        self.nameInput = Entry(canvas, textvariable=self.e, relief=FLAT, font=('SimHei', 12), validate='all',
                             validatecommand=(self.vcmd, '%P'))
        self.nameInput.place(x=w / 2 - 92, y=h / 2 - 76, width=180, height=20)  # create Entry box
        # self.nameInput.focus()
        self.pwInput = Entry(canvas, show='*', relief=FLAT, font=('Calibri', 13), validate='all',
                             validatecommand=(self.vcmd, '%P'))  # show password as *
        self.pwInput.place(x=w / 2 - 92, y=h / 2 + 15, width=180, height=20)
        button = Button(canvas, image=img1, bd=0, command=self.buttonclicked)
        self.button1 = Button(canvas, image=img2, bd=0, bg='white', activebackground='white',
                              command=self.buttonclicked1)
        self.id = canvas.create_window(w / 2 + 8, h / 2 + 107,
                                       window=button)  # create button and put it on canvas window
        self.id1 = canvas.create_window(w / 2 + 98, h / 2 + 25, window=self.button1)
        self.Cap = Label(canvas, bg='WHITE', font=('SimHei', 9))  # create Capslock tips label
        self.nameInput.bind('<Button-1>', self.clear_ent)

    def callback(self, P):
        if str.isascii(P) or P == "":
            return True
        else:
            return False

    def right_menu(self, canvas):
        def nodomain():
            self.option.set('start c:\\ittools\\no.bat')
            self.certify_window()

        def admin():
            self.option.set('start explorer.exe')
            self.certify_window()

        def power_off():
            system('shutdown -s -t 3')  # power off machine

        def popup(event):
            popup_menu.post(event.x_root, event.y_root)  # 在指定位置显示菜单
        canvas.bind('<Button-3>', popup)  # add popup menu to mouse right button
        popup_menu = Menu(canvas, tearoff=0)
        popup_menu.add_command(label='管理模式', command=admin)  # popup menu options
        popup_menu.add_command(label='关机', command=power_off)
        popup_menu.add_command(label='不加域', command=nodomain)

    def certify_window(self):
        def verification():
            password1 = 'vipkid360'
            b = password_entry.get()  # get input password from password_entry
            try:
                if str(b) == password1:  # verify admin password
                    messagebox.showinfo(title='提示', message='密码正确，点击确定后继续')
                    system('taskkill -IM cmd.exe -F')
                    system(self.option.get())
                    root.destroy()
                else:
                    messagebox.showerror(title='错误', message='密码错误，请核对.')
            except ValueError:  # for passwords should have nothing but Int, set exception
                messagebox.showwarning(title='Wrong Value!', message='密码只包含英文')
            else:
                pass
        global root1
        root1 = Toplevel(canvas)
        root1.geometry('150x80+885+465')
        root1.resizable(0, 0)
        root1.title('验证密码')
        root1.wm_attributes("-topmost", 1)
        root1.attributes("-toolwindow", True)
        # root1.focusmodel('active')
        notice_label = Label(root1, text='请输入密码').grid()
        password_entry = Entry(root1, show='*',validate='all',
                             validatecommand=(self.vcmd, '%P'))
        password_entry.grid()
        password_entry.focus()
        confirm_button = Button(root1, text='确定', command=verification).grid()
        root1.mainloop()

    def buttonclicked(self, *args):
        # self.number.set('Waiting')
        syb = '@'
        names = self.nameInput.get()
        passwords = self.pwInput.get()
        if names == '' or passwords == '':
            messagebox.showwarning(title='Error', message='用户名密码不能为空 DomainUser or password must be filled in')
        elif syb in names:
            messagebox.showwarning(title='Error', message='请输入域账号，不是邮箱')
            # detect if user enter correct name not mailbox
        else:
            with open(namepath, 'w') as file_object:  # write username to namepath
                file_object.write(names)
            with open(pwpath, 'w') as file_object:  # write password to pwpath
                file_object.write(passwords)
            '''self.newpage()'''
            root.destroy()  # end the window

    def buttonclicked1(self, *args):
        if self.Hide == 1:
            self.pwInput.config(show='')
            self.button1.config(image=img3)
            self.Hide = 0
        elif self.Hide == 0:
            self.pwInput.config(show='*')
            self.button1.config(image=img2)
            self.Hide = 1

    def capslockdetect(self, *args):
        Dll = ctypes.WinDLL("User32.dll")
        if Dll.GetKeyState(0x14) == 1:
            self.Cap.place(x=w / 2 - 40, y=h / 2 + 40)
            self.Cap.config(text='大写锁定已打开')
        elif Dll.GetKeyState(0x14) == 0:
            self.Cap.place_forget()  # hide tips when capslock off

    def change_Input(self):  # make default input language English
        hwnd = win32gui.GetForegroundWindow()
        win32api.SendMessage(hwnd, WM_INPUTLANGCHANGEREQUEST, 0, 0x0409)

    def clear_ent(self,*args):
        self.nameInput.delete(0, END)


class FullScreenApp(object):
    def __init__(self, master):
        self.root = master
        '''self.frame = Frame(self.root, bd=0, highlightthickness=0)
        self.frame.pack()
        self.state = True'''
        self.toggle_fullscreen()
        self.root.protocol("WM_DELETE_WINDOW", self.callback)

    def toggle_fullscreen(self, event=None):
        # self.state = not self.state  # Just toggling the boolean
        # self.root.attributes("-fullscreen", self.state)
        self.root.state("zoomed")  # make the maximize window
        self.root.wm_attributes("-topmost", 1)  # make the window on the top
        self.root.overrideredirect(3)  # remove all the tool bar
        # self.root.attributes("-toolwindow", True)
        # return "break"

    def callback(self):
        messagebox.showwarning(title='禁止', message='请勿关闭窗口')


if __name__ == "__main__":
    root = Tk()
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    app = FullScreenApp(root)
    if not path.exists('c:\\ittools'):
        makedirs('c:\\ittools')  # make dir when path not exist
    namepath = r'c:\ittools\aa.txt'
    pwpath = r'c:\ittools\pp.txt'
    img = PhotoImage(file='a.png')
    img1 = PhotoImage(file='denglu.png')
    img2 = PhotoImage(file='eye.png')
    img3 = PhotoImage(file='uneye.png')
    '''if w ==1920:
        img = PhotoImage(file='1.png')
    elif w == 1366:
        img = PhotoImage(file='2.png')'''
    canvas = Canvas(root, bd=0, height=h, width=w, highlightthickness=0, bg='#0a0a0c', relief='ridge')
    canvas.pack(fill=BOTH, expand=YES)
    canvas.create_image(w / 2 + 1, h / 2, image=img)
    a = CanvasButton(canvas)  # create a clickable button on the canvas
    root.bind('<KeyRelease-Caps_Lock>', a.capslockdetect)  # Detect if CapsLock on
    root.bind('<KeyRelease-Return>', a.buttonclicked)
    root.mainloop()
