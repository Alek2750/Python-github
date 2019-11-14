from tkinter import *
from tkinter import ttk, messagebox
top = Tk()
def helloCallBack():
    msg = messagebox.showinfo( "Hello Python", input_text.get())
# This is used to take input from user
# and show it in Entry Widget.
# Whatever data that we get from keyboard
# will be treated as string.
input_text = StringVar()

L1 = Label(top, text="User Name")
L1.pack()
E1 = Entry(top,textvariable = input_text)
E1.pack()
B = Button(top, text = "Hello", command = helloCallBack)
B.pack()
top.mainloop()
