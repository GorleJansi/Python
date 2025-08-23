# A=P×(1+r/n​)n×t
p=float(input("Enter principal amount:"))
r=float(input("Enter Interest rate in %:"))/100  
t=float(input("Enter the time in years: "))
n = int(input("Enter number of times interest is compounded per year: "))
amount = p* (1 + r/ n) ** (n * t)
compound = amount - p
print("\n--- Compound Interest Calculation ---")
# print(f"Principal: {p:.2f}")             :.2f formats numbers to 2 decimal places
# print(f"Rate: {r * 100:.2f}%")             rate * 100 prints the rate back in % for the user
print(f"Time: {t} years")
print(f"Compounded: {n} times per year")
print(f"Final Amount: {amount:.2f}")
print(f"Compound Interest: {compound:.2f}")