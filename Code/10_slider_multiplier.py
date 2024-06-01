import tkinter as tk
from tkinter import ttk, messagebox

def start_processing():
    process_button.config(state=tk.DISABLED)  # Disable the button while processing
    progress_bar.config(value=0)  # Reset progress bar to 0
    increment = 100 / 150  # Calculate the increment for each update
    value = 0  # Initialize the progress bar value

    def update_progress():
        nonlocal value
        value += increment
        progress_bar.config(value=value)  # Update the progress bar value

        if value < 100:
            root.after(100, update_progress)  # Schedule the next update after 100 milliseconds
        else:
            complete_processing()  # Call the complete_processing function when progress reaches 100

    update_progress()  # Start the progress bar update

def complete_processing():
    value1 = slider1.get()
    value2 = slider2.get()
    result = value1 * value2
    progress_bar.stop()
    messagebox.showinfo("Complete", f"Your answer is: {result}")
    process_button.config(state=tk.NORMAL)  # Enable the button after processing

# Create the main application window
root = tk.Tk()
root.title("Slider App")

# Set window size and position
window_width = 400
window_height = 250

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_position = int((screen_width - window_width) / 2)
y_position = int((screen_height - window_height) / 2)

root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Create two sliders
slider1 = tk.Scale(root, from_=1, to=100, orient="horizontal", label="Slider 1")
slider1.pack(pady=5)

slider2 = tk.Scale(root, from_=1, to=100, orient="horizontal", label="Slider 2")
slider2.pack(pady=5)

# Create a progress bar
progress_bar = ttk.Progressbar(root, orient="horizontal", mode="determinate")  # Change mode to "determinate"
progress_bar.pack(pady=5)
progress_bar.config(value=0)  # Set initial value to 0

# Create a button to start processing
process_button = tk.Button(root, text="Process", command=start_processing)
process_button.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
