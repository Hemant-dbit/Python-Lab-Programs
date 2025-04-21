# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Get input from user with validation
try:
    start = int(input("Enter the starting number: "))
    end = int(input("Enter the ending number: "))

    if start >= end:
        print("Invalid range. Starting number should be less than the ending number.")
    else:
        prime_numbers = []

        for num in range(start, end + 1):
            if is_prime(num):
                prime_numbers.append(num)

        # Display results
        print("\n--- Prime Number Report ---")
        print(f"Range: {start} to {end}")
        print("Prime Numbers:", *prime_numbers)
        print("Total Primes Found:", len(prime_numbers))

except ValueError:
    print("Please enter valid integers only.")
