s = {10, 20, 30, 40}
print("Set:", s)   # Order not guaranteed due to hash 



# Unordered collection → Sets do not maintain insertion order; elements are placed based on their hash values.
# Hash table storage → Internally, each element goes into a "bucket" determined by hash(element), not by when it was added.
# Iteration order not fixed → When you loop or print a set, the order may look random and can change between runs.
# Duplicates removed → Since sets only store unique elements, insertion order becomes less meaningful.
# Need order? → Use list, tuple, or sorted(set) if you require elements in a predictable sequence.