nums = [2, 4, 6, 8]
print(all(x%2==0 for x in nums))
print(any(x>5 for x in nums))



# nums = [2, 4, 6, 8]
# result = True   # assume all are True
# for x in nums:
#     if not (x % 2 == 0):   # if any number is odd
#         result = False
#         break              # stop checking further
# print(result)   # True


# nums = [2, 4, 6, 8]

# result = False   # assume none are True
# for x in nums:
#     if x > 5:     # if condition is True
#         result = True
#         break     # stop checking further
# print(result)   # True
