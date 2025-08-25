text = "Python"
y=text[::-1]
print(y)  

s = "".join(reversed(text))
# reversed(s) → gives a reverse iterator.
# "".join(...) → combines it back into a string.
print(s)   # olleH


# loops
s = "Hello"
reversed_s = ""
for char in s:
    reversed_s = char + reversed_s
print(reversed_s)   # olleH
