from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import time

class FullScreenApp(object):
    def __init__(self, master):
        self.root = master
        self.frame = Frame(self.root)
        self.frame.pack()
        self.root.protocol("WM_DELETE_WINDOW", self.callback)
    def toggle_fullscreen(self):
        self.root.attributes("-fullscreen", True)
        self.root.wm_attributes("-topmost", 1)
        return "break"

    def callback(self):
        messagebox.showwarning('请勿关闭窗口')

if __name__ == "__main__":
    root1 = Tk()
    def resize_image(event):
        new_width = event.width
        new_height = event.height
        image = copy_of_image.resize((new_width, new_height))
        photo = ImageTk.PhotoImage(image)
        label_img.config(image=photo)
        label_img.image = photo  # avoid garbage collection
    img2 = Image.open(r'loading.gif')
    '''img2.seek(99)'''  # skip to the second frame
    '''try:
        while 1:
            img2.seek(img2.tell() + 1)
            print(img2.tell())
            time.sleep(1)
            # do something to img2
    except EOFError:
        pass  # end of sequence'''
    copy_of_image = img2.copy()
    photo = ImageTk.PhotoImage(img2)
    label_img = Label(root1, image=photo)
    label_img.bind('<Configure>', resize_image)
    label_img.pack(fill=BOTH, expand=YES)
    app = FullScreenApp(root1)
    #app.toggle_fullscreen()
    root1.mainloop()