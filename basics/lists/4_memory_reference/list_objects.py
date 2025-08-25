a = [1, 2, 3]

# Assignment
b = a                    # both point to same object
b.append(4)
print(a)                 # [1, 2, 3, 4] (same reference)

# Copy
c = a.copy()             # outer list is copyed shallow copy 
c.append(5)
print(a)  # [1, 2, 3, 4]
print(c)  # [1, 2, 3, 4, 5]

d=a[:]
d.append(6)
print(a) 
print(d) 
