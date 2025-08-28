r=range(1,10,2)
print(r)
print(list(r))                  
print(len(r))                   # length of range
print(r[0])                     # indexing
print(r[1])                     # negative indexing
print(r[-1])
print(3 in r)                   # membership
print(4 not in r)
for i in range(10,20,3):
    print(i,end=" ")
print()                         # print() just outputs a newline character (\n)


for i in range(10, 0, -2):
    print(i, end=" ")    
print()    


x=["hyd","vizag","us","canada"]
for i in range(len(x)):               #  len(fruits) → returns 3  --> range(3)-->0,1,2
    print(i,x[i])