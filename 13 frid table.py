import tkinter
from typing import Text

window = tkinter.Tk()

window.title("login")

#window.geometry("500x500")



lab1 = tkinter.Label(window,text="user name").grid(row=0,column=0)

ent1 = tkinter.Entry(window, width=20).grid(row=0,column=1)

lab1 = tkinter.Label(window,text="password").grid(row=1,column=0)

ent1 = tkinter.Entry(window, width=20).grid(row=1,column=1)

but = tkinter.Button(window,text="submit").grid(columnspan=2)

window.mainloop()