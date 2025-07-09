import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate the password
def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showerror("Error", "Password length must be at least 4.")
            return
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")
        return

    # Character sets
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation
    all_chars = upper + lower + digits + symbols

    # Ensure strong password with at least one of each
    password = [
        random.choice(upper),
        random.choice(lower),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the characters
    password += random.choices(all_chars, k=length - 4)
    random.shuffle(password)
    final = ''.join(password)

    # Show in entry
    result_entry.delete(0, tk.END)
    result_entry.insert(0, final)

# Function to copy the result to clipboard
def copy_to_clipboard():
    password = result_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Empty", "No password to copy!")

# GUI Setup
root = tk.Tk()
root.title("🔐 Password Generator")
root.geometry("400x300")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

# Heading
tk.Label(root, text="Password Generator", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=10)

# Password Length
tk.Label(root, text="Enter Password Length:", font=("Arial", 12), bg="#f0f0f0").pack()
length_entry = tk.Entry(root, font=("Arial", 12), justify="center")
length_entry.pack(pady=5)

# Generate Button
tk.Button(root, text="Generate Password", command=generate_password,
          font=("Arial", 12), bg="#4caf50", fg="white").pack(pady=10)

# Result Display
result_entry = tk.Entry(root, font=("Arial", 12), width=30, justify="center")
result_entry.pack(pady=5)

# Copy Button
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard,
          font=("Arial", 11), bg="#2196f3", fg="white").pack(pady=10)

# Run the GUI
root.mainloop()
