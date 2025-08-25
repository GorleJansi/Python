x=[1,2,3]
a,b,c=x
print(a,b,c)
y=[1,2,3,4,5]
d,e,*rest=y                 # star operator for extra values
print(d,end=" ")
print(rest)
z=[7,8,9,10]
f,*mid,g=z
print(f)
print(mid)
p=[3,4,6,7]
h,*_,i=p                     #_ ignore value *_ ignore multiple  
print(h)
print(i)         

# _, *rest  Ignore the first value
# *rest, _ Ignore the last value: