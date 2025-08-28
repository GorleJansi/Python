n=[23,1,55,32,7,49]
max=n[0]
for i in range(len(n)):         # len(n)-->6 range(6) [0,1,2,3,4,5]
    if n[i]>max:
        max=n[i]
print(f"max element in the list {n} is : {max}")        

