import tkinter

window = tkinter.Tk()

window.title("hello")

window.geometry('500x500')


lab = tkinter.Label(window, text="hello" ,fg="#ffffff",bg="#444444")

lab.grid(column=5,row=0)

but= tkinter.Button(window,text="click")

but.grid(column=5,row=5)


window.mainloop()