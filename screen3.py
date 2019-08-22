from tkinter import *
from tkinter import messagebox
from os import makedirs, path

class CanvasButton:
    def __init__(self, canvas):
        self.canvas = canvas
        '''self.number = IntVar()'''
        self.createWidgets(canvas)

    def createWidgets(self, canvas):
        '''e= StringVar()
        e.set('请输入用户名')
        self.name = Label(canvas,text = '用户名:').place(x=w/2-100,y=h/2-100)'''  # make a label next to entry box
        self.nameInput = Entry(canvas,relief = RAISED)
        self.nameInput.place(x=w/2-115,y=h/2-108,width = 115,height = 25)  # create Entry box
        '''self.password = Label(canvas, text = '密码:').place(x=w/2-100,y=h/2-80)'''
        self.pwInput = Entry(canvas,show='*',relief = RAISED)  # show password as *
        self.pwInput.place(x=w/2-115,y=h/2-43,width = 230, height = 25)
        button = Button(canvas, image=img1, bd=0, command=self.buttonclicked)
        self.id = canvas.create_window(w / 2, h / 2 + 17, window=button)  # create button and put it on canvas window

    def newpage(self):  # exit current window and open a new window
        root.destroy()
        global root1
        root1=Tk()
        img2 = PhotoImage(file='cmd1.png')
        label_img = Label(root1, image=img2)
        label_img.pack()
        app = FullScreenApp(root1)
        app.toggle_fullscreen()
        root1.mainloop()

    def buttonclicked(self,*args):
        #self.number.set('Waiting')
        names = self.nameInput.get()
        passwords = self.pwInput.get()
        if names == '' or passwords =='':
            messagebox.showwarning(title = 'Error',message ='用户名密码不能为空 DomainUser or password must be filled in')
        else:
            with open(namepath,'w') as file_object:  # write username to namepath
                file_object.write(names)
            with open(pwpath,'w') as file_object:  # write password to pwpath
                file_object.write(passwords)
            '''self.newpage()'''
            root.destroy()  # end the window



class FullScreenApp(object):
    def __init__(self, master):
        self.root = master
        self.frame = Frame(self.root)
        self.frame.pack()
        self.state = True
        self.root.protocol("WM_DELETE_WINDOW", self.callback)
    def toggle_fullscreen(self, event=None):
        #self.state = not self.state  # Just toggling the boolean
        self.root.attributes("-fullscreen", self.state)
        self.root.wm_attributes("-topmost", 1)
        return "break"

    def callback(self):
        messagebox.showwarning('请勿关闭窗口')

if __name__ == "__main__":
    root = Tk()
    app = FullScreenApp(root)
    app.toggle_fullscreen()
    if not path.exists('c:\\ittools'):
        makedirs('c:\\ittools') # make dir when path not exist
    namepath = r'c:\ittools\aa.txt'
    pwpath = r'c:\ittools\pp.txt'
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    img = PhotoImage(file = 'a.png')
    img1 = PhotoImage(file = 'Enter.png')
    '''if w ==1920:
        img = PhotoImage(file='1.png')
    elif w == 1366:
        img = PhotoImage(file='2.png')'''

    canvas = Canvas(root, bd=0, height = h, width = w, highlightthickness=0,bg = 'black')
    canvas.pack(fill=BOTH, expand=YES)
    canvas.create_image(w/2+1, h/2, image=img)
    a = CanvasButton(canvas) # create a clickable button on the canvas
    root.bind('<KeyRelease-Return>', a.buttonclicked)
    root.mainloop()