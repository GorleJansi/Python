# The Fibonacci sequence is a series of num where each num is the sum of the two before it.
# F(0) = 0
# F(1) = 1
# F(n) = F(n-1) + F(n-2)   for n > 1
# 0,1,1,2,3,5,8,13,21,34,...

n = 7
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a+b