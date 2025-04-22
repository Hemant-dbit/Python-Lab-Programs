# Pattern printing using nested loops

# Number Pattern
print("Number Pattern:")
try:
    n = int(input("Enter the number of rows for number pattern: "))
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
except ValueError:
    print("Invalid input! Please enter a valid integer.")

# Hollow Diamond Star Pattern
print("\nHollow Diamond Star Pattern:")
try:
    n = int(input("Enter odd number of rows: "))
    if n % 2 == 0:
        print("Invalid input. Please enter an odd number for number of rows.")
    else:
        x = n // 2
        i = x + 1

        # Upper half of the diamond
        while i > 0:
            j = i - 1
            while j > 0:
                print(" ", end='')
                j -= 1

            k = 0
            while k < x - i + 2:
                if k + i == x + 1 or k == 0:
                    print("* ", end='')
                else:
                    print("  ", end='')
                k += 1
            print()
            i -= 1

        # Lower half of the diamond
        i = 0
        while i < x:
            j = 0
            while j <= i:
                print(" ", end='')
                j += 1

            k = 0
            while k < x - i:
                if k == 0 or k + i == x - 1:
                    print("* ", end='')
                else:
                    print("  ", end='')
                k += 1
            print()
            i += 1

except ValueError:
    print("Invalid input! Please enter a valid integer.")
