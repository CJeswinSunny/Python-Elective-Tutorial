import tkinter as tk
import string

def check_password_strength():
    password = password_entry.get()
    
    has_length = len(password) >= 8
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    score = 0
    if has_length: score += 1
    if has_digit: score += 1
    if has_special: score += 1

    if score == 0 or score == 1:
        result_label.config(text="Strength: Weak", fg="red")
    elif score == 2:
        result_label.config(text="Strength: Moderate", fg="orange")
    else: 
        result_label.config(text="Strength: Strong", fg="green")

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("350x200")
root.resizable(False, False)

frame = tk.Frame(root)
frame.pack(pady=20)

tk.Label(frame, text="Enter Password:", font=("Arial", 11)).pack(pady=5)

password_entry = tk.Entry(frame, width=25, show="*", font=("Arial", 11))
password_entry.pack(pady=5)

tk.Button(frame, text="Check Strength", command=check_password_strength, width=15).pack(pady=10)

result_label = tk.Label(frame, text="Strength: ", font=("Arial", 12, "bold"))
result_label.pack(pady=5)

root.mainloop()
