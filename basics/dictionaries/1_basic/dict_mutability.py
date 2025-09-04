d = {"a": 1, "b": 2}
print(d)

# Modify value existing
d["a"] = 100
print(d)

# Add new key
d["c"] = 300
print(d)

d.update({"d":400})
print(d)


# Dictionaries are mutable (you can change them in place).