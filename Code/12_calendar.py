import tkinter as tk
from tkcalendar import Calendar
from center_window import center_window

def select_date():
    def on_date_selected():
        selected_date.set(cal.get_date())
        top.destroy()

    top = tk.Toplevel(window)
    top.title("Select Date")

    cal = Calendar(top, selectmode='day', year=2024, month=2, day=29)
    cal.pack(padx=10, pady=10)

    ok_button = tk.Button(top, text="OK", command=on_date_selected)
    ok_button.pack(pady=5)

window = tk.Tk()

selected_date = tk.StringVar()

date_label = tk.Label(window, text="Selected Date:")
date_label.pack(pady=5)

selected_date_label = tk.Label(window, textvariable=selected_date)
selected_date_label.pack(pady=5)

date_picker_button = tk.Button(window, text="Select Date", command=select_date)
date_picker_button.pack(pady=5)

# Centering the window
center_window(window)

window.mainloop()