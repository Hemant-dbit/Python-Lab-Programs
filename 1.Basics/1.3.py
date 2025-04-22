# Program to reverse an n-digit number

try:
    num = int(input("Enter an n-digit positive number: "))
    
    if num < 0:
        print("Please enter a positive number.")
    else:
        original = num
        reverse = 0

        # Process each digit
        while num > 0:
            digit = num % 10           # Extract last digit
            reverse = reverse * 10 + digit
            num = num // 10            # Remove last digit

        # Display result
        print("\n--- Reverse Number Report ---")
        print(f"Original Number: {original}")
        print(f"Reversed Number: {reverse}")

except ValueError:
    print("Invalid input! Please enter a valid integer.")
