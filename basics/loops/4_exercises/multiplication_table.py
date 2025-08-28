n=int(input("how many tables you want ..!"))
for i in range(1,n+1):
    print(f"{i} table")
    for j in range(1,n+1):
        print(f"{i}*{j}={i*j}")
    print("------")    