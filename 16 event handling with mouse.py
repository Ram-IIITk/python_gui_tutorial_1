import tkinter
from tkinter.constants import CENTER, LEFT, RIGHT

window = tkinter.Tk()

window.title("hello")

window.geometry("500x500")



def left_click(event):
     
    tkinter.Label(window, text="left" ,fg="#ffffff",bg="#444444").pack()

def right_click(event):
     
    tkinter.Label(window, text="right" ,fg="#ffffff",bg="#444444").pack()
    
def middle_click(event):
     
    tkinter.Label(window, text="middle" ,fg="#ffffff",bg="#444444").pack()

window.bind("<Button-1>",left_click)

window.bind("<Button-2>",middle_click)

window.bind("<Button-3>",right_click)

window.mainloop()