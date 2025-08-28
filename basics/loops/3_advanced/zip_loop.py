names = ["Alice", "Bob", "Charlie"]
scores = [90, 85, 88]

for name, score in zip(names, scores):
    print(name, "->", score)

pairs=list(zip(names,scores))
print(pairs)    

print("-------------")

names1 = ["Alice", "Bob", "Charlie"]
scores1 = [90, 85]

print(list(zip(names1, scores1)))
pairs=list(zip(names1,scores1))
print(pairs)    


print("-------------")

pair=[('Alice', 90), ('Bob', 85), ('Charlie', 88)]
x,y=zip(*pairs)
print(x)
print(y)






# zip() combines elements from multiple iterables into tuples.
# Stops at the shortest iterable.
# used for pairing related data (names + scores, keys + values, etc.).
# Can be “unzipped” using zip(*iterable).