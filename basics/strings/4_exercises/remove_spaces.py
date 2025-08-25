text = " p y t h o n "
print(text.replace(" ", ""))  # python
print("".join(text.split()))
print("".join([ch for ch in text if ch != " "]))