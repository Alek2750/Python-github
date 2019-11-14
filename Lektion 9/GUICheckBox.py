from tkinter import *
from tkinter import CHECKBUTTON, messagebox
top = Tk()
CheckVar1 = IntVar()
def helloCallBack():
    msg = messagebox.showinfo( "CheckVar", CheckVar1.get())
C1 = Checkbutton(top, text = "Music", command = helloCallBack,
variable = CheckVar1, onvalue = 1, offvalue = 0, height=5,
width = 20)
C1.pack()
top.mainloop()