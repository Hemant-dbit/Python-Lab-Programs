try:
    # Example 1: List of squares
    n = int(input("Enter the range for squares: "))
    squares = [x**2 for x in range(1, n+1)]
    print("List of squares:", squares)

    # Example 2: List of even numbers
    m = int(input("Enter the range for even numbers: "))
    evens = [x for x in range(1, m+1) if x % 2 == 0]
    print("List of even numbers:", evens)

except ValueError:
    print("Please enter a valid integer.")
