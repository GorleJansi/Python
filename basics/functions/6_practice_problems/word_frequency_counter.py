def word_frequency(text):
    freq = {}
    print(text.split())
    for word in text.split():
        freq[word] = freq.get(word, 0) + 1
    return freq

print(word_frequency("this is a test this is"))
