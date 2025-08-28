# Write a Python program to find the sum of first n natural numbers.
# (Example: if n = 10, result = 1+2+3+...+10 = 55)

n=int(input("sum of first how many natural numbers :"))
total=0
for i in range(1,n+1):
    total+=i
print(f"sum of first {n} natural numbers : {total}")    

