# reduce iterable to single value by repetedly apply func
# reduce(function,iterable)
# apply func pairwise

from functools import reduce
nums=[1,2,3,4,5]
product = reduce(lambda a, b: a * b, nums)
print(product)  # 24