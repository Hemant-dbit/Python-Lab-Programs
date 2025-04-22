# Program to calculate and print the grade of a student based on average marks

# Taking input for 5 subjects
maths = int(input("Enter marks for Maths: "))
coa = int(input("Enter marks for COA: "))
python = int(input("Enter marks for Python: "))
os = int(input("Enter marks for OS: "))
cn = int(input("Enter marks for CN: "))

# Calculate average
total = maths + coa + python + os + cn
average = total / 5

# Determine grade
if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B+"
elif average >= 60:
    grade = "B"
elif average >= 50:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "F"

# Display result
print("\n--- Result Summary ---")
print("Total Marks:", total)
print("Average Marks:", average)
print("Grade:", grade)
