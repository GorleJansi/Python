s1={"a",1,"b",2,"c",3,1.5,False}

# Direct indexing not possible
# Sets are unordered, so no indexing/slicing.
for i in s1:
    print(i)
# print(s1[0])   TypeError: 'set' object is not subscriptable


# membership
if "a" in s1:
    print("True")
if 1 not in s1:
    print("True")
