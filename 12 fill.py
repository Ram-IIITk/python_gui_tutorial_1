import tkinter
from tkinter.constants import BOTTOM, LEFT, RIGHT, TOP
from tkinter.ttk import Button, Frame, Label

window = tkinter.Tk()

window.title("foot and head")

window.geometry("500x500")

frame_top = Frame(window).pack(side=TOP)
frame_foot = Frame(window).pack(side=BOTTOM)

Labelt1 = tkinter.Label(frame_top,text="top1",fg="white",bg="green").pack()
Labelt2 =tkinter.Label(frame_top,text="top2",fg="white",bg="green").pack(fill="x")
Labelt3 = tkinter.Label(frame_foot,text="foot1",fg="#ffffff",bg="#000000").pack(fill="x")
Labelt4 = tkinter.Label(frame_foot,text="foot2",fg="#ffffff",bg="#000000").pack(side=RIGHT,fill="y")


window.mainloop()