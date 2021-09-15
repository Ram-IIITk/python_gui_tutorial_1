from tkinter.ttk import *

import tkinter

window = tkinter.Tk()

window.title("Combo box")

window.geometry("500x500")

com = Combobox(window)

com['value'] = (1,2,3,4,5,'text')

com.current(0)

com.pack()

window.mainloop()