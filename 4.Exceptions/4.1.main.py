# main.py

import mymodule

def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Factorial")
        print("2. Check Prime")
        print("3. Power")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        try:
            if choice == '1':
                n = int(input("Enter a number: "))
                if n < 0:
                    print("Factorial is not defined for negative numbers.")
                else:
                    print("Factorial:", mymodule.factorial(n))

            elif choice == '2':
                n = int(input("Enter a number: "))
                if mymodule.primeNumber(n):
                    print(n, "is a Prime Number")
                else:
                    print(n, "is Not a Prime Number")

            elif choice == '3':
                base = float(input("Enter base: "))
                exponent = int(input("Enter exponent: "))
                print("Power:", mymodule.powNumber(base, exponent))

            elif choice == '4':
                print("Exiting the program. Goodbye!")
                break

            else:
                print(" Invalid choice. Please select between 1 and 4.")

        except ValueError:
            print(" Invalid input. Please enter numeric values.")

# Run the menu
menu()
