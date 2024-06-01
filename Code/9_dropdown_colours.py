import tkinter
from center_window import center_window

def change_color(color):
    c.itemconfig(rectangle, fill=color)

root = tkinter.Tk()       # Main window.

c = tkinter.Canvas(root, width=200, height=200)
c.pack()            # Layout
rectangle = c.create_rectangle(0, 0, 200, 200, fill="blue")

def run_red():
    change_color("red")

def run_blue():
    change_color("blue")

def run_green():
    change_color("green")

menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)

# Colour Cascade
colour_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Colour", menu=colour_menu)

# Red Option
colour_menu.add_command(label="Red", command=run_red)

# Blue Option
colour_menu.add_command(label="Blue", command=run_blue)

# Green Option
colour_menu.add_command(label="Green", command=run_green)

# Centering the window
center_window(root)

tkinter.mainloop()