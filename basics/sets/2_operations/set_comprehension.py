n=int(input("even numbers below : "))
even={x for x in range(n) if x%2==0}
print(f"even numbers: {even}")

squares = {i**2 for i in even}
print("Squares:", squares)