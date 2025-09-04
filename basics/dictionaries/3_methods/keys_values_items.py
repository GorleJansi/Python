d={"student":"jan","rollnum":23,"class":"1B","Place":"Hyd"}


for key in d:
    print(key,end=" ")
print()

print("-------")
print(d.keys())
for i in d.keys():
    print(i,end=" ")
print()

print("-------")
print(d.values())
for j in d.values():
      print(j,end=" ")
print() 

print("-------")
for value in d:
    print(value,end=" ")
print()

print("-------")
print(d.items())
for k in d.items():
     print(k,end=" ")
print()