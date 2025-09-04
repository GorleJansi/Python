# dict_unpacking.py

# Example 1: Merging dictionaries with unpacking
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}

merged = {**d1, **d2}
print("Merged:", merged)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}


# Example 2: Overwriting keys during unpacking
d3 = {"a": 100, "e": 5}
merged2 = {**d1, **d2, **d3}
print("Merged with overwrite:", merged2)  
# 'a' from d3 overwrites 'a' from d1 → {'a': 100, 'b': 2, 'c': 3, 'd': 4, 'e': 5}


# Example 3: Copying a dictionary with unpacking
copy_dict = {**d1}
print("Copy:", copy_dict)  # {'a': 1, 'b': 2}


# Example 4: Unpacking with literals
new_dict = {**d1, "x": 9, "y": 10}
print("Unpack + new keys:", new_dict)
# {'a': 1, 'b': 2, 'x': 9, 'y': 10}


# Example 5: Mixing with keyword arguments (**kwargs)
def show_details(**kwargs):
    print("Details:", kwargs)

student = {"name": "Jan", "age": 23, "city": "Hyd"}
show_details(**student)
# Output: Details: {'name': 'Jan', 'age': 23, 'city': 'Hyd'}
