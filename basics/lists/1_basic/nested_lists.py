# A nested list is  list inside another list.
n= [[1, 2],[3,4]]
# print("outerlist has 2 elements")
# print(n[0])
# print(n[1])
# print("Elements in innerlist of:",n[0])
# print(n[0][0])
# print(n[0][1])
# print("Elements in innerlist of:",n[1])
# print(n[1][0])
# print(n[1][1])
# print(n[1][2])

for row in n:       # loop through each inner list
    for item in row:     # loop through each element inside inner list
        print(item,end=" ")
    print()      # cursor to the next line.
