from tkinter import *

def center_window(root):
    window_width = root.winfo_screenwidth()
    window_height = root.winfo_screenheight()
    x_coordinate = int((window_width / 2) - (root.winfo_reqwidth() / 2))
    y_coordinate = int((window_height / 2) - (root.winfo_reqheight() / 2))
    root.geometry(f"+{x_coordinate}+{y_coordinate}")