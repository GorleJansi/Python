fruits = ["apple", "banana", "orange"]

for index, fruit in enumerate(fruits):
    print(index, fruit)

print("---------------------")

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
    

print("---------------------")

for index,char in enumerate("jansi"):
    print(index,char)

print("---------------------") 

pairs = list(enumerate(fruits))
print(pairs)


# enumerate() is best when you need both index and value while looping. Cleaner than using
# enumerate() is just a wrapper that pairs each item with a counter.
# enumerate() doesn’t create all pairs upfront — it generates them lazily while looping (memory efficient ✅).
