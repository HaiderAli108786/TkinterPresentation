import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage, messagebox
import json
from config_display_upgraded import config_popup

class InteractiveMenu:
    def __init__(self, root, config):
        self.root = root
        self.root.title("POMI Interactive Menu")
        self.root.geometry("700x480")  # Adjusted width and height
        self.config = config
        
        # Set the background color to white
        self.root.configure(bg='#ffffff')

        # Random dishes and descriptions
        self.options = ["Runs Process 1,2 and 3", "Runs Process 2 and 3", "Runs Process 3"]
        self.descriptions = [
            "Sort, verify and clean data and run DQ Loop 1.",
            "Check processed files and run DQ Loop 2.",
            "Creates POMI outputs."
        ]

        # Create a style for buttons and labels
        self.style = ttk.Style()
        self.style.configure('TButton', background='#ffffff', font=('Helvetica', 12), padding=5)
        self.style.configure('TLabel', background='#ffffff', font=('Helvetica', 12), padding=5)

        # Create title label
        self.title_label = ttk.Label(root, text="POMI Interactive Menu", font=('Helvetica', 16, 'bold'), background='#ffffff')
        self.title_label.pack(pady=10)

        # Load the image and resize it
        self.image = PhotoImage(file="images/nhs_logo.png").subsample(4)  # Adjust the subsample factor for resizing

        # Create labels for each option
        self.label1 = ttk.Label(root, text=f"Process 1: {self.options[0]}\nDescription: {self.descriptions[0]}", style='TLabel')
        self.label2 = ttk.Label(root, text=f"Process 2: {self.options[1]}\nDescription: {self.descriptions[1]}", style='TLabel')
        self.label3 = ttk.Label(root, text=f"Process 3: {self.options[2]}\nDescription: {self.descriptions[2]}", style='TLabel')

        # Create buttons for each option
        self.button1 = ttk.Button(root, text="Select Process 1", command=lambda: self.select_option(1), style='TButton')
        self.button2 = ttk.Button(root, text="Select Process 2", command=lambda: self.select_option(2), style='TButton')
        self.button3 = ttk.Button(root, text="Select Process 3", command=lambda: self.select_option(3), style='TButton')
        self.button_exit = ttk.Button(root, text="Exit", command=self.root.destroy, style='TButton')

        # Create a label for the resized image
        self.image_label = ttk.Label(root, image=self.image, style='TLabel')

        # Place labels, buttons, and resized image on the GUI
        self.image_label.place(relx=0.95, rely=0.1, anchor='ne')  # Adjust the position and anchor of the image label
        self.label1.pack(pady=10)
        self.button1.pack(pady=5)
        self.label2.pack(pady=10)
        self.button2.pack(pady=5)
        self.label3.pack(pady=10)
        self.button3.pack(pady=5)
        self.button_exit.pack(pady=10)  # Adjust the placement of the Exit button
        
        menu_bar = tk.Menu(root)
        root.config(menu=menu_bar)
        
        # Create a dropdown menu
        dropdown_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Options", menu=dropdown_menu)

        # Add commands to the dropdown menu
        dropdown_menu.add_command(label="Edit Config", command=lambda: config_popup(self.config))

        # Variable to store the user's choice
        self.user_choice = None

    def select_option(self, option):
        self.user_choice = option
        self.root.destroy()  # Close the Tkinter window after capturing the choice


def open_menu() -> str:
    # Create Tkinter root window
    root = tk.Tk()
    
    with open(".\\config.json") as f:
        config = json.load(f)

    # Create an instance of the InteractiveMenu class
    menu = InteractiveMenu(root, config)
    
    # Start the Tkinter main loop
    root.mainloop()
    
    # After the main loop, continue with the user's choice stored in menu.user_choice
    if menu.user_choice is not None:
        print(f"User selected Option {menu.user_choice}")
        return menu.user_choice
    
    
choice = open_menu()