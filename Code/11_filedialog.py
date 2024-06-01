import tkinter as tk
from tkinter import filedialog
from center_window import center_window

def open_file():
    file_path = filedialog.askopenfilename()
    print("Selected file:", file_path)

def save_file():
    file_path = filedialog.asksaveasfilename()
    print("Saved file:", file_path)

root = tk.Tk()

open_button = tk.Button(root, text="Open File", command=open_file)
open_button.pack()

save_button = tk.Button(root, text="Save File", command=save_file)
save_button.pack()

# Centering the window
center_window(root)

root.mainloop()