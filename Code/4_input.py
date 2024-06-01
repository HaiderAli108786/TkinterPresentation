from tkinter import *
from center_window import center_window

root = Tk()

e = Entry(root, width=50)
e.pack()
e.insert(0, "Enter Your Name")

def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()
    
    
myButton = Button(root, text="Enter your name", command=myClick) 
# fg="blue", bg="#000000", padx=50, pady=50, state=DISABLED
myButton.pack()

# Centering the window
center_window(root)

root.mainloop()