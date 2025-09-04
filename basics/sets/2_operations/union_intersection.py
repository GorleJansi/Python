A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

r1=A | B
print(r1)
r2=A.union(B)
print(r2)
# Union / |, creates a new set containing all elements from A and B

r3=A & B
print(r3)
r4=A.intersection(B)
print(r4)
# intersection / &, creates a new set containing same elements of  A and B

A |= B 
print(A)
A.update(B)
print(A)


# update / |= ,modify the existing set in place with all elements from A and B .
#  |= and .update() return None