def sum_numbers(*args):
    print(args)          # tuple of numbers
    print(type(args))    # <class 'tuple'>
    return sum(args)

print(sum_numbers(1, 2, 3))
print(sum_numbers(10, 20, 30, 40))

# *args
# Collects extra positional arguments.
# Stored as a tuple.
# Used when you don’t know how many values will be passed.
print("--------------------")

def person_info(**kwargs):
    print(kwargs)        # dictionary of key-value pairs
    print(type(kwargs))  # <class 'dict'>
    return kwargs

print(person_info(name="Alice", age=25, country="India"))

# **kwargs
# Collects extra keyword arguments.
# Stored as a dictionary (key-value pairs).
# Used when you don’t know how many named arguments will be passed.