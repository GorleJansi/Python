t1 = (10, 20, 30, 40)

print("slicing")
print(f"all elements : {t1[:]}")
print(f"reverse element : {t1[::-1]}")         #(40,30,20,10) reverse 
print(t1[1:3])          #(20,30) exclude last
print(t1[2:])           #(30,40) include last
print(t1[:-1])          #(10,20,30)
print(t1[-3:-1])        #(20,30)
print(t1[0:3:2])        #(10,30)