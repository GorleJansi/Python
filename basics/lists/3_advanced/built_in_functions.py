n=[1,11,2,3,12,4,5]
print(len(n))               # length of list
print(min(n))               # min of list
print(max(n))               # max of list
print(sum(n))               # sum of ele in list
print(sorted(n))            # sort asceneding order by default (reverse=True desc)
print(list(reversed(n)))          #reverse the list
# reversed() returns an iterator object,
# printing the object just shows its type & memory location

# n[::-1] → Creates a new reversed list (uses extra memory).
# reversed(n) → Creates a reverse iterator (no copy, just steps backward).