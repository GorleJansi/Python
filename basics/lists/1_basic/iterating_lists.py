fruits = ["apple", "banana", "cherry"]
# Value
for i in fruits:
     print(i)      #i is a temporary variable that will hold each element.

# index and value     
for i in range(len(fruits)):
     print(f"{fruits[i]} is at index {i} in {fruits}")   
    # len(fruits)=num of items in list
    # range(len(fruits)) creates a sequence of indices → [0, 1, 2]
    # i takes each index