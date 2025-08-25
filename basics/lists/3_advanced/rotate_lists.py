n = [1, 2, 3, 4, 5]
# rotate right by 1
r=n[-1:] + n[:-1]              # [5]+[1,2,3,4] =[5,4,3,2,1] lists concatation
print(r)
# rotate left by 1
l=n[1:]+n[:1]                   #[2,3,4,5]+[1]           
print(l)