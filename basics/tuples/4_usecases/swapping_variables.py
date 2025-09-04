a=[1,2]
b=[3,4]
a,b=b,a 
# rhs=execute packed to temp tuple 
# lhs=unpacks n assign to var
print(a,type(a))
print(b,type(b))
