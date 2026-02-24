import tkinter as tk
from tkinter import messagebox

def perform_calculation(operation):
    try:
        num1 = int(entry1.get())
        num2 = int(entry2.get())

        result = 0

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2

        update_result_field(str(result))

    except ValueError:
        messagebox.showerror("Error", "Please enter valid integers.")
        clear_fields()
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero.")
        entry2.delete(0, tk.END) 

def update_result_field(value):
    result_entry.config(state="normal")
    result_entry.delete(0, tk.END)
    result_entry.insert(0, value)
    result_entry.config(state="readonly")

def clear_fields():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)

root = tk.Tk()
root.title("Simple Arithmetic")
root.geometry("350x300")
root.resizable(False, False)

frame = tk.Frame(root)
frame.pack(pady=20, padx=20)

frame1 = tk.Frame(frame)
frame1.pack(pady=5)
tk.Label(frame1, text="Number 1 (Int):", width=15, anchor="e").pack(side=tk.LEFT, padx=5)
entry1 = tk.Entry(frame1, width=15)
entry1.pack(side=tk.LEFT)

frame2 = tk.Frame(frame)
frame2.pack(pady=5)
tk.Label(frame2, text="Number 2 (Int):", width=15, anchor="e").pack(side=tk.LEFT, padx=5)
entry2 = tk.Entry(frame2, width=15)
entry2.pack(side=tk.LEFT)

button_frame = tk.Frame(frame)
button_frame.pack(pady=20)

tk.Button(button_frame, text="+ Add", width=8, command=lambda: perform_calculation('add')).grid(row=0, column=0, padx=5, pady=5)
tk.Button(button_frame, text="- Sub", width=8, command=lambda: perform_calculation('subtract')).grid(row=0, column=1, padx=5, pady=5)
tk.Button(button_frame, text="x Mul", width=8, command=lambda: perform_calculation('multiply')).grid(row=1, column=0, padx=5, pady=5)
tk.Button(button_frame, text="/ Div", width=8, command=lambda: perform_calculation('divide')).grid(row=1, column=1, padx=5, pady=5)

tk.Frame(frame, height=2, bd=1, relief=tk.SUNKEN).pack(fill=tk.X, pady=10)

result_frame = tk.Frame(frame)
result_frame.pack(pady=5)
tk.Label(result_frame, text="Result:", width=10, anchor="e", font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=5)

result_entry = tk.Entry(result_frame, width=15, state="readonly", font=("Arial", 10))
result_entry.pack(side=tk.LEFT)
root.mainloop()
