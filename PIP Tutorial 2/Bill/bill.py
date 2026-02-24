import tkinter as tk
from tkinter import messagebox

def generate_bill():
    try:
        # Get inputs and convert to appropriate types
        price = float(price_entry.get())
        quantity = int(quantity_entry.get())
        
        # Validate for negative inputs
        if price < 0 or quantity < 0:
            messagebox.showerror("Invalid Input", "Price and Quantity cannot be negative.")
            return

        # Calculate initial subtotal
        subtotal = price * quantity
        
        # Apply discount rule if applicable
        discount = 0.0
        if subtotal > 1000:
            discount = subtotal * 0.10
            
        final_amount = subtotal - discount
        
        # Update output
        bill_text = f"Subtotal: ₹{subtotal:.2f}\n"
        if discount > 0:
            bill_text += f"Discount (10%): -₹{discount:.2f}\n"
        bill_text += f"-------------------------\n"
        bill_text += f"Final Amount: ₹{final_amount:.2f}"
        
        result_label.config(text=bill_text)

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.\nPrice (e.g. 500.50), Quantity (e.g. 2)")

# Create Main Window
root = tk.Tk()
root.title("Bill Generator")
root.geometry("300x300")
root.resizable(False, False)

# Main container frame
frame = tk.Frame(root)
frame.pack(pady=20, padx=20)

# Price Input
tk.Label(frame, text="Item Price (₹):", anchor="w").grid(row=0, column=0, sticky="w", pady=5)
price_entry = tk.Entry(frame, width=15)
price_entry.grid(row=0, column=1, pady=5, padx=5)

# Quantity Input
tk.Label(frame, text="Quantity:", anchor="w").grid(row=1, column=0, sticky="w", pady=5)
quantity_entry = tk.Entry(frame, width=15)
quantity_entry.grid(row=1, column=1, pady=5, padx=5)

# Generate Button
generate_btn = tk.Button(frame, text="Generate Bill", command=generate_bill, bg="lightblue", width=15)
generate_btn.grid(row=2, column=0, columnspan=2, pady=20)

# Output Label for Bill
result_label = tk.Label(frame, text="-- Bill Status --\n\nFinal Amount: ₹0.00", 
                        font=("Courier", 10), justify=tk.LEFT, bg="#f0f0f0", width=25, height=5, anchor="nw")
result_label.grid(row=3, column=0, columnspan=2, pady=5)

# Start application
root.mainloop()
