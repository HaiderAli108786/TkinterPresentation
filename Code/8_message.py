from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from center_window import center_window

root = Tk()
root.title("Pop ups Showcase")
root.geometry("400x300")

# Function to display different types of popups
def popup(popup_type):
	if popup_type == "info":
		messagebox.showinfo("Information", "This is an information popup!")
	elif popup_type == "warning":
		messagebox.showwarning("Warning", "This is a warning popup!")
	elif popup_type == "error":
		messagebox.showerror("Error", "This is an error popup!")
	elif popup_type == "question":
		response = messagebox.askquestion("Question", "Do you like popups?")
		Label(root, text=response).pack()
	elif popup_type == "okcancel":
		response = messagebox.askokcancel("Confirmation", "Are you sure?")
		Label(root, text=response).pack()
	elif popup_type == "yesno":
		response = messagebox.askyesno("Confirmation", "Do you want to proceed?")
		Label(root, text=response).pack()

# Create buttons for different types of popups
Button(root, text="Information", command=lambda: popup("info")).pack()
Button(root, text="Warning", command=lambda: popup("warning")).pack()
Button(root, text="Error", command=lambda: popup("error")).pack()
Button(root, text="Question", command=lambda: popup("question")).pack()
Button(root, text="OK/Cancel", command=lambda: popup("okcancel")).pack()
Button(root, text="Yes/No", command=lambda: popup("yesno")).pack()

# Centering the window
center_window(root)

root.mainloop()