text = " p y t h o n "
print(text.replace(" ", ""))                 # python
print("".join(text.split()))                 # splits the string by any whitespace RETURN LIST,"".join(list) joins the elements of the list into a single string
print("".join([ch for ch in text if ch != " "]))

# [ch for ch in text if ch != " "]
# # → ['P', 'y', 't', 'h', 'o', 'n']
# "".join(['P', 'y', 't', 'h', 'o', 'n'])
# # → 'Python'