# Membership (in, not in) and Identity (is, is not)
fruits = ["apple", "banana", "orange"]
if "apple" in fruits:
    print("apple present!")
if "banana" not in fruits:
    print("banana not present!")     


a = [1, 2, 3] 
b=a                     # b is alias to a ,same object
c=a[:]
if a is b:
    print("a and b has same object")
if c is not a:
    print("shallow copy ,diff object")
print(id(a))  # e.g., 140472181327104
print(id(b))  # same as a
print(id(c))  # different from a    

     