# enumerate add index to iterable
# enumerate(iterable,start=0)
n=['a','b','c']
for index,char in enumerate(n,start=1):
    print(f"{index}:{char}")