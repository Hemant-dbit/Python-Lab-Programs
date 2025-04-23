class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
        else:
            self.balance += amount
            print(f"Deposited ₹{amount}. New Balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdraw ₹{amount}. New Balance: ₹{self.balance}")

    def show_balance(self):
        print(f"Current Balance: ₹{self.balance}")

    def show_account(self):
        print("Account Details")
        print(f"Account Number : {self.account_number}")
        print(f"Account Holder : {self.account_holder}")
        print(f"Balance        : ₹{self.balance}")

# Menu-driven system
account = None

while True:
    print("\n===== Bank Menu =====")
    print("1. New Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Show Balance")
    print("5. Show Account Details")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        account_number = input("Enter account number: ")
        account_holder = input("Enter account holder name: ")
        account = BankAccount(account_number, account_holder)
        print(" Account created successfully!")

    elif choice == '2':
        if account:
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        else:
            print(" Please create an account first.")

    elif choice == '3':
        if account:
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        else:
            print(" Please create an account first.")

    elif choice == '4':
        if account:
            account.show_balance()
        else:
            print("Please create an account first.")

    elif choice == '5':
        if account:
            account.show_account()
        else:
            print("Please create an account first.")

    elif choice == '6':
        print("Exiting... Thank you for using the bank system.")
        break

    else:
        print(" Invalid choice. Please select from 1 to 6.")
