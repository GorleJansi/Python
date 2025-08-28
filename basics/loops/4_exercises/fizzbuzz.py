# Write a Python program that prints the numbers from 1 to 50.
# For multiples of 3, print "Fizz" instead of the number.
# For multiples of 5, print "Buzz".
# For numbers which are multiples of both 3 and 5, print "FizzBuzz".


n=50
for i in range(1,n+1):
    if i%3==0:
        print("Fizz")
    elif i%5==0:  
        print("Buzz") 
    elif i%3==0 & i%5==0:
        print("FizzBuzz")
    else:
        print(i)   
