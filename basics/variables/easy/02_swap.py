# 1 Without Temp variable
a=10
b=20
print(f"Before swap a value : {a}")
print(f"Before swap b value : {b}")
a=a+b
b=a-b
a=a-b
print(f"After swap a value : {a}")
print(f"After swap b value : {b}")



# 2 with Temp variable

x=30
y=40
print(f"Before swap x value : {x}")
print(f"Before swap y value : {y}")
Temp=x
x=y
y=Temp
print(f"After swap x value : {x}")
print(f"After swap y value : {y}")


# 3 Tuple unpacking

c = 50
d = 60
print(f"Before swap c value : {c}")
print(f"Before swap d value : {d}")
# Python's a cool trick to swap values without a temporary variable.
# The right side is evaluated first ,It works by creating a 'package tuple' of the values on the right side (b, a)= Tuple Packing
# and then assigning them to the variables on the left side (a, b) all at once= Tuple Unpacking
c, d = d, c
print(f"After swap c value : {c}")
print(f"After swap d value : {d}")