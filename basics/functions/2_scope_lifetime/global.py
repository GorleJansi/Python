x=10
print(f"x value before function:{x}")  
def fun1():
    global x
    x=20
    print(f"x value after global in funtction :{x}")
fun1()
print(f"x value outside function :{x}")    