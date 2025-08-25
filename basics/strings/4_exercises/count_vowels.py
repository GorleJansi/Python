text="hyderabad"
vowels="aeiou"
result=sum(1 for ch in text if ch in vowels)
print(result)


count = 0
for ch in text:
    if ch in vowels:
        count += 1

print(count)        