def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

try:
    terms = int(input("Enter number of terms: "))
    if terms <= 0:
        print("Please enter a positive integer.")
    else:
        print("Fibonacci Series:")
        for i in range(terms):
            print(fibonacci(i), end=" ")
        print(f"\nTotal terms displayed: {terms}")
except ValueError:
    print("Invalid input! Please enter a valid integer.")
