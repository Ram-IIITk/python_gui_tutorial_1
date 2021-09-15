import tkinter

import os

window = tkinter.Tk()

window.title("hello")
#<module> (e:\py-tkinter\edureka\17 image and icon.py:11)  <module> (e:\py-tkinter\edureka\im.jpg)
window.geometry("500x500")

im = tkinter.PhotoImage(file="e:\py-tkinter\edureka\im.png")

but = tkinter.Label(window,image= im)
but.pack()

window.mainloop()