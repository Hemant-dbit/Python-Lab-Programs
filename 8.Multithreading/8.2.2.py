import threading
import time
from datetime import datetime

# Shared balance and lock
balance = 0
lock = threading.Lock()

# Function to print colored messages
def log(message, color="default"):
    colors = {
        "default": "\033[0m",
        "green": "\033[92m",
        "red": "\033[91m",
        "yellow": "\033[93m",
        "cyan": "\033[96m"
    }
    print(f"{colors.get(color, colors['default'])}[{datetime.now().strftime('%H:%M:%S')}] {message}{colors['default']}")

# Thread function for withdrawal
def withdraw(name, amount):
    global balance
    log(f"{name} is trying to withdraw ₹{amount}...", "cyan")

    with lock:
        if balance >= amount:
            time.sleep(1)  # Simulate processing delay
            balance -= amount
            log(f"{name} successfully withdrew ₹{amount}. Remaining balance: ₹{balance}", "green")
        else:
            log(f"{name} failed to withdraw ₹{amount}. Insufficient balance: ₹{balance}", "red")

# Input Handling
def get_valid_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            log("Please enter a valid integer.", "yellow")

def main():
    global balance
    balance = get_valid_int("Enter initial bank balance: ")
    num_users = get_valid_int("Enter number of users: ")

    users = []
    for i in range(num_users):
        uname = input(f"\nEnter name of user {i+1}: ")
        amt = get_valid_int(f"Enter withdrawal amount for {uname}: ")
        users.append((uname, amt))

    # Start threads
    print("\n--- Running WITH Lock ---\n")
    threads = []
    for uname, amt in users:
        t = threading.Thread(target=withdraw, args=(uname, amt))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    log(f"\nFinal balance in bank: ₹{balance}", "cyan")
    print("\n✅ All transactions processed.\n")

if __name__ == "__main__":
    main()
