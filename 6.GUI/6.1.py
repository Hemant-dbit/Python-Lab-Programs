import tkinter as tk
from tkinter import messagebox
import sqlite3

# Database Setup
conn = sqlite3.connect("users.db")
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT NOT NULL
    )
''')
conn.commit()

# Show/Hide Password Function
def toggle_password():
    if var_show_password.get():
        entry_password.config(show="")
    else:
        entry_password.config(show="*")

# Registration Function
def register():
    uname = entry_username.get().strip()
    pwd = entry_password.get().strip()

    if not uname or not pwd:
        messagebox.showwarning("Input Error", "Both fields are required.")
        return
    if len(uname) < 3:
        messagebox.showwarning("Username Error", "Username must be at least 3 characters long.")
        return
    if len(pwd) < 6:
        messagebox.showwarning("Password Error", "Password must be at least 6 characters long.")
        return

    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (uname, pwd))
        conn.commit()
        messagebox.showinfo("Success", "Registration successful!")
        clear_fields()
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Username already exists.")

# Login Function
def login():
    uname = entry_username.get().strip()
    pwd = entry_password.get().strip()

    if not uname or not pwd:
        messagebox.showwarning("Input Error", "Both fields are required.")
        return

    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (uname, pwd))
    result = cursor.fetchone()
    if result:
        messagebox.showinfo("Login Success", f"Welcome {uname}!")
        clear_fields()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

# Clear input fields
def clear_fields():
    entry_username.delete(0, tk.END)
    entry_password.delete(0, tk.END)
    var_show_password.set(0)
    toggle_password()

# GUI Setup
root = tk.Tk()
root.title("Login & Registration")
root.geometry("500x250")
root.resizable(False, False)

# Username
tk.Label(root, text="Username").grid(row=1, column=0, padx=10, pady=10)
entry_username = tk.Entry(root, width=25)
entry_username.grid(row=1, column=1)

# Password

tk.Label(root, text="Password").grid(row=2, column=0, padx=10, pady=10 )
entry_password = tk.Entry(root, width=25, show="*")
entry_password.grid(row=2, column=1)

# Show Password Checkbox
var_show_password = tk.IntVar()
chk_show = tk.Checkbutton(root, text="Show Password", variable=var_show_password, command=toggle_password)
chk_show.grid(row=2, column=2, padx=10, sticky="w", pady=10)

# Register & Login Buttons
tk.Button(root, text="Register", width=15, bg="lightblue", command=register).grid(row=3, column=1, pady=10)
tk.Button(root, text="Login", width=15, bg="lightgreen", command=login).grid(row=3, column=2, pady=10)

root.mainloop()
