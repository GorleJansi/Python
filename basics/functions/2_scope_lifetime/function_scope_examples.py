x=10          # global
def fun1():
    x=20     # local
    y=10     # local
    print(f"x value is :{x}")
    print(f"y value is :{y}")
fun1()
print(f"x value is :{x}")
# print(f"y value is :{y}")    NameError: name 'y' is not defined
