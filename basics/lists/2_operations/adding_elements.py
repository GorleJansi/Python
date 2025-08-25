n=[1,2,"a","b"]
n.append("c") # adds at end
print(n)
n.extend([4,5]) # add iteratble(list,tuple,etc),mutiple
print(n)
n.insert(2,3)   # insert at index
print(n)

a=[1,2]
b=[3,4]
c=[5,6]
a.append(b)    # add list as ele at end 
print(a)
a.extend(c)    #add list ele at end
print(a)