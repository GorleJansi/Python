# # slice list using slice operator :
# list[start:end:step]  end not included;step to move default 1
n=[10,20,30,40,50]
print(n[1:3])               # o/p: [20,30]
print(n[1:])                # [20,30,40,50]
print(n[:4])                # [10,20,30,40]
print(n[:])                 # [10,20,30,40,50]
print(n[::2])               # [10,30,50]
# negative index
print(n[1:-1])              # [20,30,40]
print(n[-3:])               #  [30,40,50]
print(n[::-1])              # Reverse list 