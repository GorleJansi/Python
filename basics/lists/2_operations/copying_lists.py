n = [1, 2, 3]

copy1 = n                   # alias but same object
# slicing,list(),copy() will make shallow copy (create new outer list)
copy2 = list(n)             
copy3 = n.copy()
copy4 = n[:]

copy1.pop()
n.append(4)
copy1.append(5)

copy2.append(6)

print(n)   # [1, 2, 3, 4]
print(copy1)  # [1, 2, 3]
print(copy2)  # [1, 2, 3]
print(copy3)
print(copy4)