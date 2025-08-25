# tuple packing/unpacking (a.k.a. multiple assignment).

n=[1,2,3,4]
n[0],n[-1]=n[-1],n[0]
print(n)
# python evalutes rhs first n pack into a temporary tuple (n[-1,n[0]])
# Python evalutes lhs n unpack n assigns from the tuple to the targets
# tmp = nums[0]
# nums[0] = nums[-1]
# nums[-1] = tmp

# Generalize
i, j = 1, 2            
n[i], n[j] = n[j], n[i]
print(n)
