d1 = {"a": 1, "b": 2}
d2 = {"b": 200, "c": 3}

merged = {**d1, **d2}
print(merged)   # {'a': 1, 'b': 200, 'c': 3}
