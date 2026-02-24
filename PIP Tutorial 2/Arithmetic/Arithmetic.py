import tkinter as tk
from tkinter import messagebox

def perform_calculation(operation):
    try:
        # Simulate integer fields by enforcing int() cast
        num1 = int(entry1.get())
        num2 = int(entry2.get())

        result = 0

        # Perform the requested operation
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            # Handle division separately for ZeroDivisionError check naturally
            result = num1 / num2
            
            # Since the requirement specifies Integer fields but division 
            # might result in float, we could conditionally format it.
            # Showing floats for division results is standard behavior.

        update_result_field(str(result))

    except ValueError:
        messagebox.showerror("Error", "Please enter valid integers.")
        clear_fields()
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero.")
        entry2.delete(0, tk.END)  # Only clear the second problematic field

def update_result_field(value):
    # Temporarily enable the readonly field to update the result
    result_entry.config(state="normal")
    result_entry.delete(0, tk.END)
    result_entry.insert(0, value)
    result_entry.config(state="readonly")

def clear_fields():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)

# Create main application window
root = tk.Tk()
root.title("Simple Arithmetic")
root.geometry("350x300")
root.resizable(False, False)

# Main container frame
frame = tk.Frame(root)
frame.pack(pady=20, padx=20)

# Number 1 Input Frame
frame1 = tk.Frame(frame)
frame1.pack(pady=5)
tk.Label(frame1, text="Number 1 (Int):", width=15, anchor="e").pack(side=tk.LEFT, padx=5)
entry1 = tk.Entry(frame1, width=15)
entry1.pack(side=tk.LEFT)

# Number 2 Input Frame
frame2 = tk.Frame(frame)
frame2.pack(pady=5)
tk.Label(frame2, text="Number 2 (Int):", width=15, anchor="e").pack(side=tk.LEFT, padx=5)
entry2 = tk.Entry(frame2, width=15)
entry2.pack(side=tk.LEFT)

# Button Frame containing all operators
button_frame = tk.Frame(frame)
button_frame.pack(pady=20)

tk.Button(button_frame, text="+ Add", width=8, command=lambda: perform_calculation('add')).grid(row=0, column=0, padx=5, pady=5)
tk.Button(button_frame, text="- Sub", width=8, command=lambda: perform_calculation('subtract')).grid(row=0, column=1, padx=5, pady=5)
tk.Button(button_frame, text="x Mul", width=8, command=lambda: perform_calculation('multiply')).grid(row=1, column=0, padx=5, pady=5)
tk.Button(button_frame, text="/ Div", width=8, command=lambda: perform_calculation('divide')).grid(row=1, column=1, padx=5, pady=5)

# Separator and Result display
tk.Frame(frame, height=2, bd=1, relief=tk.SUNKEN).pack(fill=tk.X, pady=10)

result_frame = tk.Frame(frame)
result_frame.pack(pady=5)
tk.Label(result_frame, text="Result:", width=10, anchor="e", font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=5)

# Readonly result field
result_entry = tk.Entry(result_frame, width=15, state="readonly", font=("Arial", 10))
result_entry.pack(side=tk.LEFT)

# Start Application
root.mainloop()
