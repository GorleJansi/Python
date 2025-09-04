text = "banana"
freq = {}

for ch in text:
    freq[ch] = freq.get(ch, 0) + 1    
# dict.get(key, default) returns  value if the key exists,else returns the default.
# default = 0 :if the character is not in freq, count =0.

print(freq)  # {'b': 1, 'a': 3, 'n': 2}
