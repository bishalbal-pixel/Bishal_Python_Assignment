# Question 4 - Employee Salary System

employees = {
    "E101": {"name": "Ramesh Shrestha", "department": "IT", "salary": 60000},
    "E102": {"name": "Sunita Karki", "department": "HR", "salary": 45000},
    "E103": {"name": "Bikash Thapa", "department": "Finance", "salary": 55000},
    "E104": {"name": "Anjali Gurung", "department": "Marketing", "salary": 50000},
    "E105": {"name": "Prakash Rai", "department": "Sales", "salary": 40000},
}


def find_employee(emp_id):
    """Return the employee dictionary, or raise KeyError if the ID does not exist."""
    return employees[emp_id]


def calculate_yearly_salary(monthly_salary):
    """Return the salary for 12 months."""
    return monthly_salary * 12


def increase_salary(employee, percentage):
    """Increase the salary by the given percentage and return old and new salary."""
    old_salary = employee["salary"]
    new_salary = old_salary + (old_salary * percentage / 100)
    employee["salary"] = new_salary
    return old_salary, new_salary


print("Employee IDs:", ", ".join(employees))
emp_id = input("Enter employee ID: ").strip().upper()

try:
    employee = find_employee(emp_id)
except KeyError:
    print(f"Error: Employee ID '{emp_id}' does not exist.")
else:
    print(f"Employee: {employee['name']} ({employee['department']})")
    try:
        percentage = float(input("Enter salary increase percentage: ").strip().rstrip("%"))
        if percentage < 0:
            raise ValueError
    except ValueError:
        print("Error: Invalid percentage. Please enter a positive number like 10.")
    else:
        old_salary, new_salary = increase_salary(employee, percentage)
        print(f"\nOld Monthly Salary : Rs.{old_salary:,.2f}")
        print(f"New Monthly Salary : Rs.{new_salary:,.2f}")
        print(f"New Yearly Salary  : Rs.{calculate_yearly_salary(new_salary):,.2f}")
