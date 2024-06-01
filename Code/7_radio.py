from tkinter import *
from PIL import ImageTk, Image
from center_window import center_window

root = Tk()
root.title('Radio buttons')
root.iconbitmap('images/mango.ico')

TOPPINGS = [
	("Pepperoni", "Pepperoni"),
	("Cheese", "Cheese"),
	("Mushroom", "Mushroom"),
	("Onion", "Onion"),
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, topping in TOPPINGS:
	Radiobutton(root, text=text, variable=pizza, value=topping, font=("Arial", 12)).pack(anchor=W)

def clicked(value):
	myLabel = Label(root, text=value, font=("Arial", 14, "bold"))
	myLabel.pack()

myButton = Button(root, text="Click Me!", command=lambda: clicked(pizza.get()), bg="orange", fg="white", font=("Arial", 16, "bold"))
myButton.pack(pady=10)

# Centering the window
center_window(root)

mainloop()
