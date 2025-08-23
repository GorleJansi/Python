basic_salary=float(input("Enter basic Pay:"))
# Allowances
hra = float(input("Enter HRA (House Rent Allowance): "))
ta = float(input("Enter TA (Travel Allowance): "))
# Deductions
tax = float(input("Enter Tax deduction: "))
pf = float(input("Enter PF  deduction: "))
# Step 1: Calculate gross salary (before deductions)
gross_salary=basic_salary+hra+ta
# Step 3: Calculate net salary (after deductions)
net_salary=gross_salary-(tax+pf)

print("\n --- Salary Slip ---")
print(f"Basic Salary:{basic_salary}")
print(f"Gross Salary:{gross_salary}")
print(f"Net Salary:{net_salary}")
