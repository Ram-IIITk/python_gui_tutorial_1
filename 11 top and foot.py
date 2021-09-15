import tkinter
from tkinter.constants import BOTTOM, LEFT, RIGHT, TOP
from tkinter.ttk import Button, Frame, Label

window = tkinter.Tk()

window.title("foot and head")

window.geometry("500x500")

frame_top = Frame(window).pack(side=TOP)
frame_foot = Frame(window).pack(side=BOTTOM)

Labelt1 = Button(frame_top,text="top1").pack()
Labelt2 = Button(frame_top,text="top2").pack(side=BOTTOM)
Labelt3 = Button(frame_foot,text="foot1").pack(side=LEFT)
Labelt4 = Button(frame_foot,text="foot2").pack(side=RIGHT)


window.mainloop()