from tkinter import *
def sel():
    selection = "You selected the option " + str(var.get())
    label.config(text = selection)

top = Tk()
var = IntVar()
R1 = Radiobutton(top, text="Option 1", variable=var, value=1, command=sel)
R1.pack( anchor = W )
R2 = Radiobutton(top, text="Option 2", variable=var, value=2,command=sel)
R2.pack( anchor = W )
R3 = Radiobutton(top, text="Option 3", variable=var, value=3,command=sel)
R3.pack( anchor = W)
label = Label(top)
label.pack()
top.mainloop()