# Empty frozenset
f = frozenset()
print(f)   # frozenset()
print("-------")

fs = frozenset([1, 2,2, 3])    # DUPLICATES REMOVED
print(fs)
print("-------")

# Operations not allowed
#  fs.add(4)       #   AttributeError: 'frozenset' object has no attribute 'add'
#  fs.remove(1)       #   AttributeError: 'frozenset' object has no attribute 'remove'
#  Immutable → No .add(), .remove(), or .update().

# Operations allowed
A = frozenset([1, 2, 3])
B = frozenset([3, 4, 5])
print("Union:", A | B)
print("Intersection:", A & B)
print("Difference:",A - B) 



# frozenset is set but immutable.
# Once created,you cannot add or remove elements.
# immutable, a frozenset is hashable,can be used as a key in a dictionary or an element of another set (normal set cannot).



