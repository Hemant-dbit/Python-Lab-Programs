import sqlite3

# DB Setup
conn = sqlite3.connect("user.db")
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT NOT NULL
    )
''')
conn.commit()

def add_user():
    uname = input("Enter username: ")
    pwd = input("Enter password: ")
    try:
        cursor.execute("INSERT INTO users VALUES (?, ?)", (uname, pwd))
        conn.commit()
        print("User added successfully!")
    except sqlite3.IntegrityError:
        print("User already exists.")

def show_users():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    if users:
        for user in users:
            print("Username:", user[0], "| Password:", user[1])
    else:
        print("No users found.")

def delete_user():
    uname = input("Enter username to delete: ")
    cursor.execute("DELETE FROM users WHERE username=?", (uname,))
    conn.commit()
    print("User deleted (if existed).")

def update_user():
    uname = input("Enter username to update: ")
    new_pwd = input("Enter new password: ")
    cursor.execute("UPDATE users SET password=? WHERE username=?", (new_pwd, uname))
    conn.commit()
    print("Password updated (if user exists).")

def search_user():
    uname = input("Enter username to search: ")
    cursor.execute("SELECT * FROM users WHERE username=?", (uname,))
    user = cursor.fetchone()
    if user:
        print("User found -> Username:", user[0], "| Password:", user[1])
    else:
        print("User not found.")

# Menu
while True:
    print("\n--- User Management Menu ---")
    print("1. Add User")
    print("2. Show Users")
    print("3. Delete User")
    print("4. Update Password")
    print("5. Search User")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_user()
    elif choice == '2':
        show_users()
    elif choice == '3':
        delete_user()
    elif choice == '4':
        update_user()
    elif choice == '5':
        search_user()
    elif choice == '6':
        break
    else:
        print("Invalid choice. Try again.")
