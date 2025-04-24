# Single Inheritance Example with user input
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def __str__(self):
        return f"{super().__str__()}, Employee ID: {self.employee_id}"


# Multilevel Inheritance Example with user input
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        print(f"{self.name} barks.")

class GermanShepherd(Dog):
    def __init__(self, name, breed, color):
        super().__init__(name, breed)
        self.color = color

    def display(self):
        print(f"{self.name} is a {self.color} {self.breed}.")


if __name__ == "__main__":

    # Getting input for single inheritance example
    print("Enter details for Employee (Single Inheritance):")
    emp_name = input("Enter name: ")
    emp_age = int(input("Enter age: "))
    emp_id = input("Enter employee ID: ")

    emp = Employee(emp_name, emp_age, emp_id)
    print("\nSingle Inheritance Output:")
    print(emp)


    # Getting input for multilevel inheritance example
    print("\nEnter details for German Shepherd (Multilevel Inheritance):")
    dog_name = input("Enter name: ")
    dog_breed = input("Enter breed: ")
    dog_color = input("Enter color: ")

    gs = GermanShepherd(dog_name, dog_breed, dog_color)
    print("\nMultilevel Inheritance Output:")
    gs.display()
    gs.speak()
