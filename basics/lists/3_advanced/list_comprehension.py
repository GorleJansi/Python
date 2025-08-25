# # generate new list from existing list
# [expression for item in iterable if condition]
n=[1,2,3,4]

# generate list
m=[item for item in n ]
print(m)

# Basic
a=[x**2 for x in n]
print(f"squares of ele in {n}: {a}")

# With condition
b=[x for x in n if x%2==0]
print(f"even ele in {n} :{b}")

# Nested
matrix = [[1, 2], [3, 4]]
c=[ele for row in matrix for ele in row]
print(c)