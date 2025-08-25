sentence = "apple orange apple banana orange apple"
words = sentence.split()          # split() with no arguments splits on any whitespace ['apple','orange','apple','banana','orange','apple']

freq = {}                         # Creates an empty dictionary to hold word → count mappings.
for w in words:
    if w in freq:
        freq[w] += 1
    else:  
        freq[w] = 1

print(freq)  # {'apple': 3, 'orange': 2, 'banana': 1}
