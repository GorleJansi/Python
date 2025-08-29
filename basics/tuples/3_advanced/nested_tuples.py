# Q: How do nested tuples work?
# Tuples can contain other tuples (nested structure).

t = (1, (2, 3), (4, (5, 6)))
print(t[0])
print("nested tuple")
print(t[1])
print(t[1][0])
print(t[1][1])
print("nested tuple")
print(t[2])
print(t[2][0])
print(t[2][1][0])
print(t[2][1][1])
