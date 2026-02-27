# Construct a program to store the information of an employee such as name, employee ID, department and generate the salary as per the following conditions:
# (1) DA is 92% of Basic Salary
# (ii) HRA is 58% of Basic Salary
# (ii) TA is 30% of Basic Salary
# (iv) LIC is deducted: Rs. 500 every month


# Input employee details
name = input("Enter Employee Name: ")
emp_id = input("Enter Employee ID: ")
department = input("Enter Department: ")
basic_salary = float(input("Enter Basic Salary: "))

# Salary components
da = 0.92 * basic_salary   
hra = 0.58 * basic_salary  
ta = 0.30 * basic_salary    
lic = 500                

gross_salary = basic_salary + da + hra + ta
net_salary = gross_salary - lic

# Display output
print("\n--- Employee Salary Details ---")
print("Name:", name)
print("Employee ID:", emp_id)
print("Department:", department)
print("Basic Salary:", basic_salary)
print("DA:", da)
print("HRA:", hra)
print("TA:", ta)
print("LIC Deduction:", lic)
print("Gross Salary:", gross_salary)
print("Net Salary:", net_salary)