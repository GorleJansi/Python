# # container to store data 
# variable created when a value is assigned and get type from value

name="Jansi"   # varibale of type str
age=24        # varibale of type int
Place="Hyderabad"
# can only concatenate str (not "int") to str
print("My name is " + name + ", " "I am " + str(age) + " years old" ", " "I live in " + Place)



# Use an f-string to easily combine text and variables.
# The 'f' before the string tells Python to format it.
# Put variables inside curly braces {} and Python will automatically
# convert them to strings for you, avoiding errors.
print(f"My name is {name}, I am {age} years old, I live in {Place}")
