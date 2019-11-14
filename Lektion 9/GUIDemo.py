from tkinter import *
from tkinter import messagebox
top = Tk()
def helloCallBack():
    msg = messagebox.showinfo( "Hello Python", "Hello World")
B = Button(top, text = "Hello", command = helloCallBack)
B.pack()
top.mainloop()