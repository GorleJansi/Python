nums = [5, 2, 9, 1]
print(sorted(nums))  # [1, 2, 5, 9]
print(min(nums))     # 1
print(max(nums))     # 9


print("-----------------------")
n = [5, 2, 9, 1]
min=n[0]
for i in n[1:]:
    if i<min:
        min=i
print(min)  

max=n[0]
for i in n[1:]:
    if i>max:
        max=i
print(max) 

