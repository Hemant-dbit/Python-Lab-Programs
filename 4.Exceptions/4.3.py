# Define valid credentials
valid_username = 'Hemant22'
valid_password = 'p123'

# Initialize attempt counter
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    try:
        username = input("Enter username: ")
        if username != valid_username:
            raise KeyError("User doesn't exist!")

        password = input("Enter password: ")
        if password != valid_password:
            raise PermissionError("Incorrect password!")

        print("✅ Login successful!")
        break  # Exit loop on success

    except KeyError as ke:
        print("KeyError:", ke)

    except PermissionError as pe:
        print("PermissionError:", pe)

    attempts += 1
    print(f"Attempts remaining: {max_attempts - attempts}\n")

else:
    print("Too many failed attempts! Access denied.")
