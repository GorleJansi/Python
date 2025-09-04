d = {"name": "Alice", "age": 25}
print(d)
print(type(d))
print(d["name"])
print(d.get("name"))
print(d["age"])
print(d.get("age"))

# print(d["city"])             # ❌ KeyError
print(d.get("city","hyd"))     # if no value (no error)and print default given