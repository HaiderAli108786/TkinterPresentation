from tkinter import *
from center_window import center_window

root = Tk()

# Creating a Label Widget
myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My Name Is ...")

# Rows and columns are relative
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)

# Centering the window
center_window(root)

root.mainloop()