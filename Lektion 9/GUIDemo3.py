from tkinter import *
from tkinter import messagebox, CHECKBUTTON

top = Tk()

CheckVar1 = IntVar()


def helloCallBack():
    msg = messagebox.showinfo("Hello Python", input_text.get())


input_text = StringVar()
E1 = Entry(top, textvariable=input_text)

E1.pack()


def doULikeMusic():
    musicS = StringVar()
    if CheckVar1.get():
        musicS = "you do like music"
    else:
        musicS = "you don't like music"
    msg = messagebox.showinfo("Do you like music?", musicS)


C1 = Checkbutton(top, text="Music", command=doULikeMusic, variable=CheckVar1, onvalue=1, offvalue=0, height=5,
                 width=20)


B = Button(top, text="Hello", command=helloCallBack)
B.pack()

C1.pack()
top.mainloop()