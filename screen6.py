from tkinter import *
from tkinter import messagebox
from screen3 import FullScreenApp
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
        self.nameInput.place(x=w/2-115,y=h/2-85,width = 230, height = 25)  # create Entry box
        button = Button(canvas, image=img1, bd=0, command=self.buttonclicked)
        self.id = canvas.create_window(w / 2, h / 2 -15, window=button)  # create button and put it on canvas window

    def buttonclicked(self,*args):
        #self.number.set('Waiting')
        names = self.nameInput.get()
        if names == '':
            messagebox.showwarning(title = 'Error',message ='员工号不能为空 Employee ID must be filled in')
        else:
            with open(Epath,'w') as file_object:  # write username to namepath
                file_object.write(names)
            root.destroy()  # end the window

if __name__ == "__main__":
    root = Tk()
    app = FullScreenApp(root)
    app.toggle_fullscreen()
    Epath = r'c:\ittools\rr.txt'
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    img = PhotoImage(file = 'yuangonghao.png')
    img1 = PhotoImage(file = 'Enter.png')
    canvas = Canvas(root, bd=0, height = h, width = w, highlightthickness=0,bg = 'black')
    canvas.pack(fill=BOTH, expand=YES)
    canvas.create_image(w/2+1, h/2, image=img)
    a = CanvasButton(canvas) # create a clickable button on the canvas
    root.bind('<KeyRelease-Return>', a.buttonclicked)
    root.mainloop()