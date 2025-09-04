s = {1, 2, 3}
s.add(10)
print("After add:", s)

s.update([20, 30])   # Add multiple
# update() expects an iterable (list, set, tuple, etc.).
print("After update:", s)

s.remove(2)         # remove,if no value ;KeyError: 4  
print("After remove:", s)

s.discard(4)        # remove,if no value no error   
print("After remove:", s)

