A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
r1=A.difference(B)
r2=B.difference(A)
r3=A.symmetric_difference(B)
# differnce():return new set with uniq items in first set
print("Difference:",A-B,r1,sep=" ")

print("Difference:",B - A,r2,sep=" ")

# Symmetric Difference():return new set with items uniq in both sets
print("Symmetric Difference:",A ^ B,r3,sep=" ")