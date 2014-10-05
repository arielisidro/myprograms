__author__ = 'ariel'

from tkinter import *


def stop_program(e):
    root.destroy()


def transfer_text(e):
    label1.configure(text = "Hello world")


root = Tk()

button1 = Button(root,text="Exit")
button1.pack()
button1.bind('<Button-1>',stop_program)

button2 = Button(root,text="Click Me")
button2.pack()
button2.bind('<Button-1>',transfer_text)

label1 = Label(root, text="Nothing to say")
label1.pack()


root.mainloop()




