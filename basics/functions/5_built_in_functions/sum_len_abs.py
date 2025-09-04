nums = [3, -5, 7]
print(sum(nums))   # 5
print(len(nums))   # 3
print(abs(-10))    # 10


print("-------------")
n = [3, -5, 7]
sum=0
for i in n:
    sum+=i
print(sum)    

print("-------------")
n = [3, -5, 7]
count=0
for i in n:
    count+=1
print(count)  

print("-------------")
def my_abs(x):
    if x < 0:
        return -x
    return x

print(my_abs(-10))  # 10

# If the number is negative, it returns -x.
# If the number is positive or zero, it returns the same value.