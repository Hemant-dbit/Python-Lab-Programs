try:
    # Input for List1
    n1 = int(input("Enter number of elements for List1: "))
    if n1 < 0:
        raise ValueError("Number of elements can't be negative.")
    
    list1 = []
    for i in range(n1):
        element = input(f"Enter element {i+1} for List1: ")
        list1.append(element)

    # Input for List2
    n2 = int(input("Enter number of elements for List2: "))
    if n2 < 0:
        raise ValueError("Number of elements can't be negative.")
    
    list2 = []
    for i in range(n2):
        element = input(f"Enter element {i+1} for List2: ")
        list2.append(element)

    # Merging List2 into List1
    list1.extend(list2)

    # Display updated list
    print("\nUpdated List1 after merging List2:", list1)

except ValueError as ve:
    print(f"\nInput Error: {ve}")
except Exception as e:
    print(f"\nAn unexpected error occurred: {e}")

