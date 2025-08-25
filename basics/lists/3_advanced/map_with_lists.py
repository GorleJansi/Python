# aplies a given function to each element of an iterable (like list, tuple, etc.).
# returns a map object (which you usually convert to desired type)
# map(function, iterable)

n1= [1, 2, 3, 4]
n2=[4, 5, 6]
m1 = list(map(lambda x:x**2,n1))
print(m1)

# Multiple Iterables ;function must also accept that many arg
m2=list(map(lambda x,y:x+y,n1,n2))
print(m2)

# apply the same function to every element then use map().

w = ["hello","hi"]

# map with built-in function then better to use than list comprehension
u = list(map(str.upper, words))  
print(u)  

# comprehension version
uppercased = [word.upper() for word in words]