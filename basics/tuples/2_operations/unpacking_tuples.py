# tuple packing:assigning values to tuple when created is packing
x=(1,2,3)
# tuple unpacking:extract values from tuple to variables
A,B,C=x
print(A,type(A))
print(B,type(B))
print(C,type(C))

print("-----------")
y=(4,5,6,7,8,9)
# var must match val in tuple,else collect *
a,*b=y
c,*d,e=y
f,g,*h=y

print(a,type(a))    # 4
print(b,type(b))    # [5,6,7,8,9]
print(c,type(c))    # 4
print(d,type(d))    # [5,6,7,8]
print(e,type(e))    # 9
print(f,type(f))    # 4
print(g,type(g))    # 5
print(h,type(h))    # [6,7,8,9]
