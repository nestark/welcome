from tkinter import *
from screen3 import FullScreenApp
class CanvasButton:
    def __init__(self, canvas):
        self.canvas = canvas
        '''self.number = IntVar()'''
        self.createWidgets(canvas)

    def createWidgets(self, canvas):
        locations=('雍和/惠通','达美','成都','上海','大连','深圳')
        self.shorts=('yh','dm','cd','sh','dl','sz')
        self.intVar = IntVar()
        i = 1
        for location in locations:
            if i<=3:
                Radiobutton(canvas, text=location,variable = self.intVar,# 将Radiobutton绑定到self.intVar变量
                    value=i,font = ('SimHei', 13, 'bold'),bg='grey',fg = 'black',highlightcolor='black',
                            ).place(x=w/2-310+135*i,y=h/2-95)
            else:
                Radiobutton(canvas, text=location, variable=self.intVar,
                            value=i,font = ('SimHei', 13, 'bold'),bg='grey',fg = 'black',highlightcolor='black'
                            ).place(x=w/2-310+135*(i-3), y=h / 2 - 65)
            i+=1
        self.intVar.set(1)
        button = Button(canvas, image=img1, bd=0, command=self.buttonclicked)
        self.id = canvas.create_window(w / 2, h / 2 -15, window=button)  # create button and put it on canvas window

    def buttonclicked(self,*args):
        num = self.intVar.get()
        names = self.shorts[num-1]
        with open(Epath,'w') as file_object:  # write username to namepath
            file_object.write(names)
        root.destroy()  # end the window

if __name__ == "__main__":
    root = Tk()
    app = FullScreenApp(root)
    app.toggle_fullscreen()
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    Epath=r'c:\ittools\zz.txt'
    img = PhotoImage(file='zhichang.png')
    img1 = PhotoImage(file='Enter.png')
    canvas = Canvas(root, bd=0, height=h, width=w, highlightthickness=0, bg='black')
    canvas.pack(fill=BOTH, expand=YES)
    canvas.create_image(w / 2 + 1, h / 2, image=img)
    a = CanvasButton(canvas)  # create a clickable button on the canvas
    root.bind('<KeyRelease-Return>', a.buttonclicked)
    root.mainloop()
