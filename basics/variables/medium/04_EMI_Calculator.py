

P = float(input("Enter Loan Amount: "))
R = float(input("Enter Annual Interest Rate (%): "))
T = int(input("Enter Loan Tenure (years): "))
# Convert to monthly rate and months
r = R / (12 * 100)      
# Interest is given in annual percentage (%), but EMI is monthly 
# Divide by 100 → convert percentage to decimal (12% → 0.12).
# Divide by 12 → because EMI is monthly (0.12 / 12 = 0.01).
n = T * 12
# EMI formula
EMI = (P * r * (1 + r)**n) / ((1 + r)**n - 1)

print("\n--- Loan EMI Details ---")
print(f"Loan Amount: {P:.2f}")
print(f"Rate of Interest: {R:.2f}%")
print(f"Tenure: {T} years ({n} months)")
print(f"Monthly EMI: {EMI:.2f}")