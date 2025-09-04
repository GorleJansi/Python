import copy

print("===== 1. Assignment (Reference) =====")
d1 = {"x": [1, 2]}
d2 = d1   # assignment → both point to same dict

print("d1:", d1, "| id(d1):", id(d1))
print("d2:", d2, "| id(d2):", id(d2))
print("d1['x'] id:", id(d1["x"]), "| d2['x'] id:", id(d2["x"]))

d2["x"].append(3)  # change through d2
print("After modifying d2:", d1, d2, "\n")


print("===== 2. Shallow Copy =====")
d3 = d1.copy()   # shallow copy → new outer dict, same inner list reference

print("d1:", d1, "| id(d1):", id(d1))
print("d3:", d3, "| id(d3):", id(d3))
print("d1['x'] id:", id(d1["x"]), "| d3['x'] id:", id(d3["x"]))

d3["x"].append(4)  # modifying inner list affects both
print("After modifying d3:", d1, d3, "\n")


print("===== 3. Deep Copy =====")
c = {"x": [1, 2]}
d4 = copy.deepcopy(c)  # deep cop
