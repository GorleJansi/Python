d={"student":"jan","rollnum":23,"class":"1B","Place":"Hyd"}
print(d)
print(d["student"])
# print(d["Teacher"])              KeyError: 'Teacher'   if key not found
print(d.get("Place"))                 #default value is none 
print(d.get("Teacher"))                  # no error is not found
print(d.get("School","chaitanya"))       # if key not found,default value taken