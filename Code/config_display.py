import tkinter as tk
from tkinter import messagebox
import sys
from tkinter import ttk
import json
import os

def config_popup(config):
    """Opens a tkinter window to allow the user to change the configuration options. The new configuration values are saved to the config.json file."""
    # Create the tkinter window
    window = tk.Tk()
    window.title("Config Menu")

    # Calculate the center position of the screen
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    padding = 10  # Padding between elements

    # Calculate the number of config options
    num_options = len(config)

    # Calculate the window width and height based on the number of options
    label_width = 300  # Width of the labels 
    entry_width = 120  # Width of the entry fields 
    window_width = label_width + entry_width + 3 * padding
    window_height = (num_options + 5) * 30  # Assuming each option takes 30 pixels in height

    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    # Set the window position
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Add a title label
    title_label = tk.Label(window, text="Config Window", font=("Arial", 16, "bold"), fg="black")
    title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    # Create labels and dropdown menus for selected config options
    entries = {}
    row = 1  # Start from row 1 to add padding to the top
    for key, value in config.items():
        label = tk.Label(window, text=key)
        label.grid(row=row, column=0, padx=10, pady=5)
        if key in ["test_run", "rerun_pbi", "use_corporate_reference", "override_run_LSOA","Exclude_unknown_gender"]: #This can be automated to find the true/false values but for now its hardcoded
            entry = ttk.Combobox(window, values=["True", "False"], width=40)  # Increase the width of the dropdown menu to 40 characters
            entry.set(str(value))
        else:
            entry = tk.Entry(window, width=40)  # Increase the width of the text box to 40 characters
            entry.insert(0, str(value))
        entry.grid(row=row, column=1, padx=10, pady=5)
        entries[key] = entry
        row += 1

    # Function to handle the continue button click
    def continue_clicked():
        # Update the config options with the values from the dropdown menus
        for key, entry in entries.items():
            if key in ["test_run", "rerun_pbi", "use_corporate_reference", "override_run_LSOA"]:
                config[key] = entry.get() == "True"
            else:
                config[key] = entry.get()
        messagebox.showinfo("Config Menu", "Continuing...")
        window.destroy()  # Destroy the window after showing the message

    # Function to handle the exit button click
    def exit_clicked():
        messagebox.showinfo("Config Menu", "Closing Program...")
        window.destroy()
        return sys.exit()

    # Create the continue and exit buttons
    continue_button = tk.Button(window, text="Continue", command=continue_clicked)
    continue_button.grid(row=row, column=0, columnspan=2, padx=10, pady=5)  # Center the button by using columnspan=2
    row += 1
    exit_button = tk.Button(window, text="Exit", command=exit_clicked)
    exit_button.grid(row=row, column=0, columnspan=2, padx=10, pady=5)  # Center the button by using columnspan=2

    # Start the tkinter event loop
    window.mainloop()

    # Update the config.json file with the new configuration values
    config_file_path = os.path.abspath('config.json')
    with open(config_file_path, 'w') as file:
        json.dump(config, file, indent=4, default=str)

    return config


# with open(".\\config.json") as f:
#     config = json.load(f)

# config_popup(config)