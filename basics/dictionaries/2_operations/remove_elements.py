d={"student":"jan","rollnum":23,"class":"1B","Place":"Hyd"}
d.pop("rollnum")           # Removes rollnum
print(d)
d.popitem()                # Removes last inserted key
print(d)
del d["student"]           # Removes specified
print(d)
d.clear()                  # clear dictionary
print(d)
del d                     # delete dict
 #  print(d)                  #  NameError: name 'd' is not defined.
