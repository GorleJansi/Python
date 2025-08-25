sentence = "apple orange apple banana orange apple"
words = sentence.split()

freq = {}
for w in words:
    if w in freq:
        freq[w] += 1
    else:  
        freq[w] = 1

print(freq)  # {'apple': 3, 'orange': 2, 'banana': 1}
