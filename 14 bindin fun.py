import tkinter

window = tkinter.Tk()

window.title("hello")

window.geometry("500x500")



def click():
     
     lab = tkinter.Label(window, text="hello" ,fg="#ffffff",bg="#444444").pack()
    

but = tkinter.Button(window,text="click",command=click)


but.pack()

window.mainloop()