s1={"a",1,"b",2,"c",3,1.5,False}
print(s1)
print(type(s1))
s2={}            # create dict
print(s2)
print(type(s2))
s3=set()         # create empty set
print(s3)
print(type(s3))

s4=(1,2,"a","b",2.5,False,(3,4))
print(s4)
print(type(s4))

s5={(1,2),[3,4],{5,6}}       #   TypeError: unhashable type: dict/set/list
print(s5)
print(type(s5))

# ✅ Hashable (immutable) → int, float, str, tuple (if its elements are also hashable), frozenset
# ❌ Unhashable (mutable) → list, set, dict