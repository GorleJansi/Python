# Q: How can a function return multiple values using tuples?
# In Python, a function can only return one object.
# If we want multiple values, we group them into a single object.
def min_max(nums):
    return min(nums), max(nums)  # tuple packing


result = min_max([5, 2, 9, 1])
print(result)
print(type(result))
min_val, max_val=result             # tuple unpacking
print("Min:", min_val)
print("Max:", max_val)


# Explanation:
# Functions can return multiple values inside a tuple.
