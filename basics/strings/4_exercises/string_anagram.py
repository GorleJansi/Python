from collections import Counter

str1 = "listen"
str2 = "silent"
# sorted() returns a list of characters, in alphabetical order.
if sorted(str1) == sorted(str2):
    print("Anagram")
else:
    print("Not Anagram")

if Counter(str1) == Counter(str2):
    print("Anagram")
else:
    print("Not Anagram")    