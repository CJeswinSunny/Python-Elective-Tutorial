import tkinter as tk
from tkinter import messagebox

def convert_to_fahrenheit():
    try:
        celsius = float(celsius_entry.get())
        
        fahrenheit = (celsius * 9/5) + 32
        
        result_entry.config(state="normal")
        result_entry.delete(0, tk.END)
        result_entry.insert(0, f"{fahrenheit:.2f}")
        result_entry.config(state="readonly")
        
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for Celsius.")
        
        celsius_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Temperature Converter")
root.geometry("300x200")
root.resizable(False, False)

input_frame = tk.Frame(root)
input_frame.pack(pady=(20, 10))

celsius_label = tk.Label(input_frame, text="Celsius (°C):", font=("Arial", 12))
celsius_label.pack(side=tk.LEFT, padx=(0, 10))

celsius_entry = tk.Entry(input_frame, font=("Arial", 12), width=10)
celsius_entry.pack(side=tk.LEFT)

convert_button = tk.Button(root, text="Convert to Fahrenheit", command=convert_to_fahrenheit, font=("Arial", 10))
convert_button.pack(pady=10)

output_frame = tk.Frame(root)
output_frame.pack(pady=10)

result_label = tk.Label(output_frame, text="Fahrenheit (°F):", font=("Arial", 12))
result_label.pack(side=tk.LEFT, padx=(0, 10))

result_entry = tk.Entry(output_frame, font=("Arial", 12), width=10, state="readonly")
result_entry.pack(side=tk.LEFT)

root.mainloop()
