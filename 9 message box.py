from tkinter.ttk import *

import tkinter

from tkinter import messagebox

window = tkinter.Tk()

window.title("check box")

window.geometry("500x500")

def click():

    msg_head = tkinter.Label(window,text="ena da varatha",width=100) 

    msg_head.pack()

    messagebox.showinfo("message title","content")

    msg_foot = tkinter.Label(window,width=50) 

    msg_foot.pack()

bt  = Button(window,text="click",command=click)

bt.pack()

window.mainloop()