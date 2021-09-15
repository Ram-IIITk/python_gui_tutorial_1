import tkinter
from typing import Text

window = tkinter.Tk()

window.title("hello")

window.geometry("500x500")

Text = tkinter.Entry(window,width=15)

def click():
    res = Text.get()

    #tkinter.Label(text= res).pack()

    t = tkinter.Label(window,text= res).pack()
    

but = tkinter.Button(window,text="click",command=click)

Text.pack()

but.pack()



window.mainloop()