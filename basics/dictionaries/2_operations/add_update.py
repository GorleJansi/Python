d={"name":"bob","age":24}
d["place"]="hyd"               # Add new key
d["age"]=25                    # Update existing key
d.update({"company":"cisco"})  # add new item
print(d)
print(d["company"])
print(d["age"])