# Employee Salary Program

# Input employee details
name = input("Enter Employee Name: ")
emp_id = int(input("Enter Employee ID: "))
department = input("Enter Department: ")
basic_salary = float(input("Enter Basic Salary: "))

# Salary calculations
da = 0.92 * basic_salary
hra = 0.58 * basic_salary
ta = 0.30 * basic_salary
lic = 500

gross_salary = basic_salary + da + hra + ta
net_salary = gross_salary - lic

# Display output
print("\n----- Employee Salary Details -----")
print("Name        :", name)
print("Employee ID :", emp_id)
print("Department  :", department)
print("Basic Salary:", basic_salary)
print("DA          :", da)
print("HRA         :", hra)
print("TA          :", ta)
print("LIC Deduct  :", lic)
print("Net Salary  :", net_salary)