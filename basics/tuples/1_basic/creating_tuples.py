# Q: How do you create tuples in Python?

# Tuples are defined using () and are immutable,ordered,allow duplicates

t1=()       # empty
t2=(1,)     # single ele tuple use , 
t3=(1,2,3)
t4=(1,"a",1.5,True,[2,3],(4,5))   # tuple can have any datatype
t5=tuple(("b","c"))               # tuple constructor  
t6=tuple([6,7,8])               #tuple from list 
print(t1,t2,t3,t4,t5,t6,sep="\n")

