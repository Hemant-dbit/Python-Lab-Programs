def calculate_net_salary(emp_type, monthly_salary=0, hourly_rate=0, days_present=0, bonus=0, tax=0):
    if emp_type.lower() == 'permanent':
        gross = monthly_salary + bonus
        net = gross - tax
        return {
            "type": "Permanent",
            "monthly_salary": monthly_salary,
            "bonus": bonus,
            "tax": tax,
            "gross": gross,
            "net": net
        }
    elif emp_type.lower() == 'temporary':
        working_hours = days_present * 8
        gross = (working_hours * hourly_rate) + bonus
        net = gross - tax
        return {
            "type": "Temporary",
            "hourly_rate": hourly_rate,
            "days_present": days_present,
            "working_hours": working_hours,
            "bonus": bonus,
            "tax": tax,
            "gross": gross,
            "net": net
        }
    else:
        return None

def print_salary_summary(details):
    print("\n========== Salary Summary ==========")
    print(f"Employee Type     : {details['type']}")
    
    if details["type"] == "Permanent":
        print(f"Monthly Salary    : ₹{details['monthly_salary']:.2f}")
    else:
        print(f"Hourly Rate       : ₹{details['hourly_rate']:.2f}")
        print(f"Days Present      : {details['days_present']} days")
        print(f"Total Work Hours  : {details['working_hours']} hours")
    
    print(f"Bonus/Incentives  : ₹{details['bonus']:.2f}")
    print(f"Gross Salary      : ₹{details['gross']:.2f}")
    print(f"Tax Deducted      : ₹{details['tax']:.2f}")
    print(f"Net Salary        : ₹{details['net']:.2f}")
    print("====================================\n")

try:
    print("Welcome to the Employee Salary Calculator\n")
    emp_type = input("Enter employee type (Permanent/Temporary): ").strip()

    if emp_type.lower() == 'permanent':
        salary = float(input("Enter monthly salary (₹): "))
        bonus = float(input("Enter bonus/incentives (₹): "))
        tax = float(input("Enter income tax (₹): "))
        details = calculate_net_salary(emp_type, monthly_salary=salary, bonus=bonus, tax=tax)

    elif emp_type.lower() == 'temporary':
        rate = float(input("Enter hourly rate (₹): "))
        days = int(input("Enter number of days present: "))
        bonus = float(input("Enter incentives (₹): "))
        tax = float(input("Enter tax (₹): "))
        details = calculate_net_salary(emp_type, hourly_rate=rate, days_present=days, bonus=bonus, tax=tax)
    else:
        print(" Invalid employee type entered! Please enter 'Permanent' or 'Temporary'.")
        details = None

    if details is not None:
        print_salary_summary(details)

except ValueError:
    print("\n Invalid input! Please enter numeric values for salary, rate, bonus, days, and tax.")
except Exception as e:
    print(f"\n An unexpected error occurred: {e}")
