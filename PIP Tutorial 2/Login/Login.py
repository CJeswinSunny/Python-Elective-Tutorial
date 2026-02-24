import tkinter as tk
from tkinter import messagebox

# Dummy credentials to validate against
VALID_USERNAME = "jeswin"
VALID_PASSWORD = "1234"

def attempt_login():
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    # Check for empty fields
    if not username or not password:
        messagebox.showwarning("Incomplete", "Username and password fields cannot be empty!")
        return

    # Check validity of credentials
    if username == VALID_USERNAME and password == VALID_PASSWORD:
        messagebox.showinfo("Success", "Login Successful!")
    else:
        messagebox.showerror("Error", "Invalid username or password.")
        # Clear fields for convenience
        password_entry.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("Login Form")
root.geometry("300x200")
root.resizable(False, False)

# Main frame container
main_frame = tk.Frame(root)
main_frame.pack(pady=30, padx=20)

# Username Label & Entry
username_label = tk.Label(main_frame, text="Username:", font=("Arial", 10))
username_label.grid(row=0, column=0, sticky=tk.E, pady=5)

username_entry = tk.Entry(main_frame, font=("Arial", 10), width=15)
username_entry.grid(row=0, column=1, pady=5, padx=(5, 0))

# Password Label & Entry
password_label = tk.Label(main_frame, text="Password:", font=("Arial", 10))
password_label.grid(row=1, column=0, sticky=tk.E, pady=5)

password_entry = tk.Entry(main_frame, font=("Arial", 10), width=15, show="*")
password_entry.grid(row=1, column=1, pady=5, padx=(5, 0))

# Login Button
login_button = tk.Button(main_frame, text="Login", command=attempt_login, width=10)
login_button.grid(row=2, column=0, columnspan=2, pady=15)

# Start application
root.mainloop()
