t=(1,2,3,4)
# squares=(x**2 for x in t )    
# o/p <generator object <genexpr> at 0x...>
# () generator object which is iterator ,give ele one at a time
squares=tuple(x**2 for x in t ) 
#  tuple consume generator(one time use) and create a tuple
print(squares)

x=(1)
print(x)