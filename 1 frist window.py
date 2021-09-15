import tkinter

window = tkinter.Tk()

window.title("hello")

window.geometry("500x500")

lab = tkinter.Label(window, text="hello" ,fg="#ffffff",bg="#444444").pack()

window.mainloop()