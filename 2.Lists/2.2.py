try:
    # Input number of elements
    n = int(input("Enter the number of elements in the list: "))
    
    if n <= 0:
        raise ValueError("List must have at least one element.")
    
    my_list = []

    # Input list elements
    for i in range(n):
        element = input(f"Enter element {i+1}: ")
        my_list.append(element)

    # Input value to search
    value = input("Enter the value to check: ")

    # Count occurrences and find positions
    count = my_list.count(value)
    positions = [i for i, x in enumerate(my_list) if x == value]

    # Display results
    print("\n--- Search Results ---")
    if count > 0:
        print(f"Total count of '{value}': {count}")
        print(f"Positions: {positions}")
    else:
        print(f"'{value}' was not found in the list.")

except ValueError as ve:
    print(f"Input Error: {ve}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


