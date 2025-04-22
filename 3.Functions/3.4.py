def square_elements(lst, filter_type=None):
    """Returns a list with squares of each element in the input list."""
    if filter_type == "positive":
        lst = [x for x in lst if x > 0]
    elif filter_type == "nonzero":
        lst = [x for x in lst if x != 0]
    return [x**2 for x in lst]

def display_statistics(lst, label):
    print(f"\n--- {label} Statistics ---")
    print(f"Total Elements : {len(lst)}")
    print(f"Maximum Value  : {max(lst):.2f}")
    print(f"Minimum Value  : {min(lst):.2f}")
    print(f"Average Value  : {sum(lst) / len(lst):.2f}" if lst else "Average Value  : N/A")

try:
    print("Square Elements Program with Extended Features \n")
    
    n = int(input("Enter number of elements: "))
    if n <= 0:
        print("Please enter a positive number.")
    else:
        original_list = []
        for i in range(n):
            value = float(input(f"Enter element {i+1}: "))
            original_list.append(value)

        print("\nDo you want to filter elements before squaring?")
        print("1. No filter\n2. Only positive numbers\n3. Exclude zero")
        filter_choice = input("Choose an option (1/2/3): ").strip()
        filter_map = {'1': None, '2': 'positive', '3': 'nonzero'}
        filter_type = filter_map.get(filter_choice, None)

        sort_choice = input("\nDo you want to sort the list before squaring? (yes/no): ").strip().lower()
        if sort_choice == 'yes':
            original_list.sort()

        squared_list = square_elements(original_list, filter_type=filter_type)

        print("\nResults")
        print(f"Original List : {original_list}")
        print(f"Squared List  : {squared_list}")

        display_statistics(original_list, "Original")
        display_statistics(squared_list, "Squared")

except ValueError:
    print("Invalid input! Please enter valid numeric values.")
except Exception as e:
    print(f" An unexpected error occurred: {e}")
