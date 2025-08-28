# factorial of n n!=n×(n−1)×(n−2)×...×2×1
# 0!=1

n=int(input("enter a number :"))
m=n
if n<0:
    print("Factorial is not defined for negative numbers")
elif n==0:
    print("factorial of 0 is 1")  
else:
    for i in range(1,n):          # range=1,2...n-1
        n=n*i
    print(f"factorial of {m} is {n} ")      
