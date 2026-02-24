import tkinter as tk

def clear_label():
    label.config(text="")
    clear_button.config(state=tk.DISABLED)
    restore_button.config(state=tk.NORMAL)

def restore_label():
    label.config(text="Python GUI Demo")
    clear_button.config(state=tk.NORMAL)
    restore_button.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Python GUI Demo")
root.geometry("300x150")

label = tk.Label(root, text="Hello", font=("Arial", 16))
label.pack(pady=20)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

clear_button = tk.Button(button_frame, text="Clear", command=clear_label, width=10)
clear_button.pack(side=tk.LEFT, padx=10)

restore_button = tk.Button(button_frame, text="Restore", command=restore_label, state=tk.DISABLED, width=10)
restore_button.pack(side=tk.LEFT, padx=10)


root.mainloop()
