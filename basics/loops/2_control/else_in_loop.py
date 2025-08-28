for i in range(10):
    print(i, end=" ")
else:   # directly connected to the for loop
    print("\nLoop finished without break")

# else runs only if loop completes normally (not interrupted by break).



for x in range(10,20):
    if x>15:
        print("\nelse runs only if loop completes normally (not interrupted by break)")
        break
    print(x,end=" ")
else:
    print("\nLoop finished without break")    