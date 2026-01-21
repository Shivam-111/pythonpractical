# Vendor Annual Purchase Program


vendor_name = input("Enter Vendor Name: ")
year_of_association = int(input("Enter Year of Association: "))
contact_number = input("Enter Contact Number: ")
email_id = input("Enter Email ID: ")


monthly_purchases = []
print("\nEnter monthly purchase amounts:")

for i in range(1, 13):
    amount = float(input(f"Month {i}: "))
    monthly_purchases.append(amount)

annual_purchase = sum(monthly_purchases)

print("\n----- Annual Purchase / Billing Report -----")
print("Vendor Name         :", vendor_name)
print("Year of Association :", year_of_association)
print("Contact Number      :", contact_number)
print("Email ID            :", email_id)
print("Annual Purchase     : Rs.", annual_purchase)