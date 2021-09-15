from tkinter.ttk import *

import tkinter

window = tkinter.Tk()

window.title("check box")

window.geometry("500x500")

chk_state = tkinter.BooleanVar()

chk_state.set(False)

chk = Checkbutton(window,text="select",var=chk_state)

chk.pack()

window.mainloop()