from tkinter.ttk import *

import tkinter

from tkinter import messagebox

window = tkinter.Tk()

window.title("check box")

window.geometry("500x500")

spin = Spinbox(window,from_ = 0, to = 50,width=20)

spin.pack()

window.mainloop()