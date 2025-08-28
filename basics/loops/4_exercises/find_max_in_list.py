n=[23,1,55,32,7,49]
max=n[0]
for i in range(len(n)):
    if n[i]>max:
        max=n[i]
print(f"max element in the list {n} is : {max}")        