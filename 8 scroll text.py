from tkinter.ttk import *

import tkinter

from tkinter import scrolledtext

window = tkinter.Tk()

window.title("check box")

window.geometry("500x500")

txt = scrolledtext.ScrolledText(window,width=40,height=10)
txt.pack()

#txt = tkinter.scrolledtext.ScrolledText(window,width=40,height=10)

window.mainloop()