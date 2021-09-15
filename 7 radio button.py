from tkinter.ttk import *

import tkinter

window = tkinter.Tk()

window.title("check box")

window.geometry("500x500")

but1  = Radiobutton(window,text="python",value=1)

but2 = Radiobutton(window,text="C",value=2)

but3  = Radiobutton(window,text="R",value=3)

but1.pack()

but2.pack()

but3.pack()

window.mainloop()