import tkinter
#import tkinter.messagebox
from tkinter import messagebox


def helloCallBack():
   messagebox.showinfo( "Hello Python", "Hello World")

window = tkinter.Tk();
#window.title = "Python Window"
window.wm_title("Python Window")
window.wm_minsize(300,280)
#print(help(window))



button = tkinter.Button(window, text='Button', command=helloCallBack)
button.pack()

window.mainloop()