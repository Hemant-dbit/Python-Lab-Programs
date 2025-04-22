# Sample list with different data types
my_list = [10, 20.5, "Hello", True, 15, "World", 3.14, False, 25, [1, 2], (1, 2), {'key': 'value'}]

# Initialize an empty dictionary to store type counts
type_count = {}

# Loop through each item in the list and count the data types
for item in my_list:
    item_type = type(item)
    if item_type not in type_count:
        type_count[item_type] = 1
    else:
        type_count[item_type] += 1

# Output the counts for each data type
for item_type, count in type_count.items():
    print(f"{item_type.__name__.capitalize()} count: {count}")
