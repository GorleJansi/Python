# Q: Can we change elements of a tuple?

# t=(1,2,3,4,5)
# t[0]="a"                # TypeError: 'tuple' object does not support item assignment
# t[1]="b"                # Tuples are immutable, so their values cannot be changed directly.
# print(t)

x=("a","b","c")
y=list(x)
print(x)
print(type(x))
print(type(y))            # convert tuple to list ,change ,convert back to tuple
y[0]=1
y[1]=2
y[2]=3
x=tuple(y)
print(x)
print(type(x))
print(y)
print(type(y))



# but tuple can hold mutable objects (like lists) which can be changed
t1 = (1, [2, 3], 4)
t1[1].append(5)
print(t1)  # (1, [2, 3, 5], 4)


