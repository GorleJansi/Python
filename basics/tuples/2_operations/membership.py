x=(1,2,3,4,5,"a")
if 1 in x:
    print("exists..!")
if "a" not in x:
    print("not exists..!")   
else:
    print("exists..!")     

print("----------------")

# "how membership internally"

y=("a","b","c","e")
def membership(t,value):
    for element in t:
        if element == value:
            return True
    return False
result=membership(x,"e")
if result:
     print("exists..!")
else:
      print("not exists..!")    
