from tkinter import *
from screen3 import FullScreenApp


class CanvasButton:
    def __init__(self, canvas):
        self.canvas = canvas
        self.createWidgets(canvas)
        self.software = []

    def createWidgets(self, canvas):
        self.intVar = IntVar()
        self.intVar0 = IntVar()
        self.intVar1 = IntVar()
        self.intVar2 = IntVar()
        self.intVar3 = IntVar()
        self.intVar.set(1)
        self.intVar0.set(1)
        check1 = Checkbutton(canvas, text='微软拼音（默认）', variable=self.intVar1, onvalue=1, offvalue=0,
                             command=self.addtolist, indicatoron=0, font=('YouYuan',13), bd=0)
        check2 = Checkbutton(canvas, text='搜狗拼音（含广告）', variable=self.intVar2, onvalue=1, offvalue=0,
                             command=self.addtolist, indicatoron=0,font=('YouYuan',13), bd=0)
        check3 = Checkbutton(canvas, text='搜狗五笔（含广告）', variable=self.intVar3, onvalue=1, offvalue=0,
                             command=self.addtolist, indicatoron=0, font=('YouYuan',13), bd=0)
        button1 = Radiobutton(canvas, text='不安装（默认）', variable=self.intVar, value=1,indicatoron=0, font=('YouYuan', 13),
                              bd=0).place(x=w / 2 - 590, y=h / 2 - 20)
        button2 = Radiobutton(canvas, text='安装', variable=self.intVar, value=2,indicatoron=0, font=('YouYuan', 13),
                              bd=0).place(x=w / 2 - 410 , y=h / 2 - 20)
        button3 = Radiobutton(canvas, text='不安装（默认）', variable=self.intVar0, value=1, indicatoron=0,
                              font=('YouYuan', 13),
                              bd=0).place(x=w / 2 - 590, y=h / 2 + 85)
        button4 = Radiobutton(canvas, text='安装', variable=self.intVar0, value=2, indicatoron=0, font=('YouYuan', 13),
                              bd=0).place(x=w / 2 - 410, y=h / 2 + 85)
        select1=canvas.create_window(w/2 - 510, h / 2-105, window=check1)
        select2 = canvas.create_window(w / 2 - 350, h / 2-105, window=check2)
        select3 = canvas.create_window(w / 2 - 180, h / 2-105, window=check3)
        button = Button(canvas, image=img1, bd=0, command=self.buttonclicked)
        self.id = canvas.create_window(w / 2 + 40, h / 2 + 198,
                                       window=button)  # create button and put it on canvas window

    def buttonclicked(self, *args):
        num = self.intVar.get()
        names = 1
        with open(Epath, 'w') as file_object:  # write username to namepath
            file_object.write(str(names))
        root.destroy()  # end the window

    def addtolist(self):
        pass


if __name__ == "__main__":
    root = Tk()
    app = FullScreenApp(root)
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    Epath = r'c:\ittools\zz.txt'
    img = PhotoImage(file='screen8.png')
    img1 = PhotoImage(file='denglu.png')
    canvas = Canvas(root, bd=0, height=h, width=w, highlightthickness=0, bg='black')
    canvas.pack(fill=BOTH, expand=YES)
    canvas.create_image(w / 2, h / 2, image=img)
    a = CanvasButton(canvas)  # create a clickable button on the canvas
    root.bind('<KeyRelease-Return>', a.buttonclicked)
    root.mainloop()
