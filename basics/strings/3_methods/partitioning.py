
text2 = "name: Jansi"
print(text2.partition(":"))


# text.partition(":") → splits text into (before, ":", after) at the first colon.

text1 = "a:b:c"

print(text1.split(":"))       # ['a', 'b', 'c']
print(text1.partition(":"))   # ('a', ':', 'b:c')


text3 = "hello world"
print(text3.partition(":"))             #    ('hello world', '', '')

