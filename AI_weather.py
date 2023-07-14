import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def submit_name():
    name = name_entry.get()
    if name:
        submit_button.config(state=tk.DISABLED)
        loading_window = tk.Toplevel(root)
        loading_window.title("Loading Progress")
        loading_window.geometry("300x120")

        loading_label = tk.Label(loading_window, text="Loading...")
        loading_label.pack(pady=10)

        loading_bar_frame = tk.Frame(loading_window, width=280, height=20, bd=1, relief=tk.SUNKEN)
        loading_bar_frame.pack()

        loading_bar = ttk.Progressbar(loading_bar_frame, mode="determinate", orient="horizontal", length=280)
        loading_bar.pack(pady=10)

        loading_messages = [
            "Looking up",
            "Huhh! seems cloudy",
            "Hang on",
            "Processed!!",
            "Almost done",
            "Here you go"
        ]

        progress_increment = 100 / len(loading_messages)
        progress_value = 0

        for message in loading_messages:
            loading_label.config(text=message)
            progress_value += progress_increment
            loading_bar["value"] = progress_value
            loading_window.update()
            loading_window.after(1000)

        loading_label.config(text="")
        loading_bar["value"] = 100

        result = tk.Toplevel(root)
        result.title("AI weather assistant")
        result.geometry("200x100")
        result_label = tk.Label(result, text="Idk see outside")
        result_label.pack(pady=10)

        name_entry.delete(0, tk.END)
        submit_button.config(state=tk.NORMAL)



root = tk.Tk()
root.title("AI weather assistant")


name_label = tk.Label(root, text="Enter the location:")
name_label.pack(pady=10)
name_entry = tk.Entry(root)
name_entry.pack(pady=5)

submit_button = tk.Button(root, text="Submit", command=submit_name)
submit_button.pack(pady=10)

root.mainloop()
