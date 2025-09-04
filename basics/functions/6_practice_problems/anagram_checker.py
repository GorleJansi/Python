def is_anagram(x,y):
    return sorted(x)==sorted(y)
print(is_anagram("listen", "silent"))  # True
print(is_anagram("hello", "world"))    # False