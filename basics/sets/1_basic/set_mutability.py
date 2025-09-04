# Sets are mutable → can add/remove elements
s={1,2,"a","b"}

s.add(3)
print(s)
print(type(s))

s.add(True)              # no duplicates
print(s)

s.remove("a")            # Error if not found    KeyError: 7
print(s)   
  
s.discard(4)
print(s)                 # no Error if not found 

s.clear()
print(s)

del s                    # NameError: name 's' is not defined