from tkinter import *
from center_window import center_window

root = Tk()

def myClick1():
    myLabel = Label(root, text="I clicked Button 1!")
    myLabel.pack()

def myClick2():
    myLabel = Label(root, text="I clicked Button 2!")
    myLabel.pack()

def myClick3():
    myLabel = Label(root, text="I clicked Button 3!")
    myLabel.pack()

# Button 1
myButton1 = Button(root, text="Button 1", command=myClick1, fg="white", bg="blue", padx=20, pady=10)
myButton1.pack()

# Button 2
myButton2 = Button(root, text="Button 2", command=myClick2, fg="black", bg="yellow", padx=30, pady=15)
myButton2.pack()

# Button 3
myButton3 = Button(root, text="Button 3", command=myClick3, fg="white", bg="green", padx=40, pady=20)
myButton3.pack()

# Centering the window
center_window(root)

root.mainloop()