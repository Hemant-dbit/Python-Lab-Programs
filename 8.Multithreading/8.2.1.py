import threading
import time

# Shared bank balance
balance = 0

def withdraw(name, amount):
    global balance
    print(f"{name} is trying to withdraw ₹{amount}...")
    if balance >= amount:
        time.sleep(1)  # Simulate processing delay
        balance -= amount
        print(f"{name} successfully withdrew ₹{amount}. Remaining balance: ₹{balance}")
    else:
        print(f"{name} failed to withdraw ₹{amount}. Insufficient balance: ₹{balance}")

# Input
balance = int(input("Enter initial bank balance: "))
num_users = int(input("Enter number of users: "))

users = []
for i in range(num_users):
    uname = input(f"\nEnter name of user {i+1}: ")
    amt = int(input(f"Enter withdrawal amount for {uname}: "))
    users.append((uname, amt))

# Start threads
print("\n--- Running WITHOUT Lock ---")
threads = []
for uname, amt in users:
    t = threading.Thread(target=withdraw, args=(uname, amt))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
