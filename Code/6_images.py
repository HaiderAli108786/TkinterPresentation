from tkinter import *
from PIL import ImageTk,Image #python image library
from center_window import center_window

root = Tk()
root.title('Adding images and icons')
root.iconbitmap('images/mango.ico')


my_img = ImageTk.PhotoImage(Image.open("images/nhs_logo.png"))
my_label = Label(image=my_img)
my_label.pack()
button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

# Centering the window
center_window(root)

root.mainloop()

