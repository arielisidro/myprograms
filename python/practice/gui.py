__author__ = 'ariel'

from tkinter import *

def stop_program(e):
    root.destroy()


root = Tk()

button1 = Button(root,
                 text="Hello World, click to close")

button1.pack()

button1.bind('<Button-1>',stop_program)

root.mainloop()




