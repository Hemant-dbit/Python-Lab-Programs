from datetime import datetime

def calculate_fine(return_date, due_date, condition):
    days_late = (return_date - due_date).days
    fine = 0

    # ₹2 per late day
    if days_late > 0:
        fine += days_late * 2

    # ₹50 fine if book is damaged
    if condition.lower() == 'damaged':
        fine += 50

    return fine

try:
    # Input section
    due = input("Enter due date (dd-mm-yyyy): ")
    ret = input("Enter return date (dd-mm-yyyy): ")
    condition = input("Enter book condition (Good/Damaged): ")

    # Convert string input to date
    due_date = datetime.strptime(due, "%d-%m-%Y")
    return_date = datetime.strptime(ret, "%d-%m-%Y")

    # Calculate fine
    fine = calculate_fine(return_date, due_date, condition)

    # Output
    print("\n--- Library Fine Summary ---")
    print(f"Due Date       : {due_date.strftime('%d-%m-%Y')}")
    print(f"Return Date    : {return_date.strftime('%d-%m-%Y')}")
    print(f"Book Condition : {condition}")
    print(f"Total Fine     : ₹{fine}")

except ValueError:
    print("Invalid date format! Please enter the date in dd-mm-yyyy format.")
