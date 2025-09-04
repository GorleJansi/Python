students = {
    "s1": {"name":"jansi","age": 25, "marks": 90},
    "s2": {"name":"munni","age": 24, "marks": 80}
}
Teachers={
    "t1": {"name":"ravi","age": 45},
    "t2": {"name":"priya","age": 53}
}

school={"s":students,"t":Teachers}

print(school["s"])   # All students dictionary
print(school["t"])   # All teachers dictionary
print("---------")
print(school["s"]["s1"])        #   Accessing a specific student/teacher
print(school["s"]["s2"])
print(school["t"]["t1"])
print(school["t"]["t2"])
print("---------")
print(school["s"]["s1"]["name"])   #  Accessing individual fields
print(school["s"]["s2"]["age"])
print(school["t"]["t1"]["name"])
print(school["t"]["t2"]["age"])
print("---------")
print(school["s"].items())
# Print all student names
for sid, details in school["s"].items():
    print(sid, "->", details["name"])

# Print all teacher names
for tid, details in school["t"].items():
    print(tid, "->", details["name"])
