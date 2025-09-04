# Question: Check if a set of prime numbers {2, 3, 5} is subset of {1,2,3,4,5,6}.
A={2, 3, 5}
B={1,2,3,4,5,6}
print(A.issubset(B))     # True
print(B.issuperset(A))   # True
print(A.isdisjoint({7, 8}))  # True