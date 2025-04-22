try:
    print(name)  # NameError
    lst = [1, 2, 3]
    print(lst[5])  # IndexError
    x = 5 / 0  # ZeroDivisionError

except NameError:
    print("NameError: Variable is not defined.")

except IndexError:
    print("IndexError: Index out of range.")

except ZeroDivisionError:
    print("ZeroDivisionError: Division by zero is not allowed.")
