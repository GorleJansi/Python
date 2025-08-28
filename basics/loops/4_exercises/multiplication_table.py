# Write a Python program that takes a number (say n = 5) and
# prints its multiplication table from 1 to 10.

n=int(input("how many tables you want ..!"))
for i in range(1,n+1):
    print(f"{i} table")
    for j in range(1,n+1):
        print(f"{i}*{j}={i*j}")
    print("------")    