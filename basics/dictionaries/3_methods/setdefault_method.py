d = {"a": 1}
print(d.setdefault("a", 100))   # 1 (already exists)
print(d.setdefault("b", 200))   # 200 (added)
print(d)                        # {'a': 1, 'b': 200}

# key exists in dict→ return its value (and do nothing).
# key does not exist→ insert the key with default_value and return that value.