try:
    n = int(input("Enter the number of elements: "))
    if n <= 0:
        raise ValueError("List must have at least one element.")

    my_list = []

    for i in range(n):
        num = int(input(f"Enter element {i+1}: "))
        my_list.append(num)

    choice = int(input("Press 1 for Ascending order or 2 for Descending order: "))

    if choice == 1:
        my_list.sort()
        print("\nList in Ascending order:", my_list)
    elif choice == 2:
        my_list.sort(reverse=True)
        print("\nList in Descending order:", my_list)
    else:
        print("\nInvalid choice! Please enter 1 or 2.")

except ValueError as ve:
    print(f"\nInput Error: {ve}")
except Exception as e:
    print(f"\nAn unexpected error occurred: {e}")


