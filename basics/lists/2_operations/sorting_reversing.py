n = [3, 1, 4, 2]
m = [5,2,6,9,1]
n.sort()                        # in-place ascending default
print(n)
m.sort(reverse=True)            # Des order
print(m)
n.reverse()                     #  reverse order
print(n)

# sorted() creates new list
print(sorted(m))   # [9, 6, 5, 2, 1]
print(m)           # original unchanged
