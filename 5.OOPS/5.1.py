class Student:
    # Default constructor with default values for name, age, and marks
    def __init__(self, name="Unknown", age=0, marks=None):
        if marks is None:
            marks = []  # Initialize marks as an empty list if no marks provided
        self.name = name
        self.age = age
        self.marks = marks

    # Method to display student details
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
        if self.marks:
            print(f"Marks: {', '.join(map(str, self.marks))}")
        else:
            print("Marks: Not available")

    # Method to calculate the average marks and grade
    def calculate_grade(self):
        if not self.marks:
            return "No marks available"
        
        avg = sum(self.marks) / len(self.marks)
        
        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 50:
            return "C"
        else:
            return "F"
    
    # Method to update marks
    def update_marks(self, new_marks):
        self.marks = new_marks
    
    # Method to update student information
    def update_info(self, name=None, age=None):
        if name:
            self.name = name
        if age:
            self.age = age

# Taking user input for the student details
name = input("Enter student name: ")
age = int(input("Enter student age: "))
num_marks = int(input("Enter number of marks: "))
marks = []

for i in range(num_marks):
    mark = float(input(f"Enter mark {i+1}: "))
    marks.append(mark)

# Create student object with user input
student = Student(name, age, marks)

# Displaying student information
student.display()

# Displaying grade
print(f"Grade: {student.calculate_grade()}")

# Updating student information
update_choice = input("Do you want to update student information? (yes/no): ").lower()
if update_choice == "yes":
    new_name = input("Enter new name (or press Enter to skip): ")
    new_age = input("Enter new age (or press Enter to skip): ")
    
    if new_name:
        student.update_info(name=new_name)
    if new_age:
        student.update_info(age=int(new_age))

    # Display updated details
    student.display()
    print(f"Updated Grade: {student.calculate_grade()}")

# Updating marks
update_marks_choice = input("Do you want to update marks? (yes/no): ").lower()
if update_marks_choice == "yes":
    new_marks = []
    num_new_marks = int(input("Enter number of new marks: "))
    for i in range(num_new_marks):
        new_mark = float(input(f"Enter new mark {i+1}: "))
        new_marks.append(new_mark)
    student.update_marks(new_marks)

    # Display updated marks and grade
    student.display()
    print(f"Updated Grade: {student.calculate_grade()}")
