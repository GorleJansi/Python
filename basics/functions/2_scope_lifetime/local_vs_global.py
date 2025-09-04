x = 10  # Global variable

def modify():
    x = 5  # Local variable (inside function)
    print("Inside function:", x)

modify()
print("Outside function:", x)
