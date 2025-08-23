maths=int(input("Enter marks:"))
science=int(input("Enter marks:"))
social=int(input("Enter marks:"))
total=maths+science+social
avg=total/3
if avg >=90:
    grade="A"
elif avg>=70:
    grade="B"
elif avg>=50:
    grade="C"
else:
    grade="F"
print(f"Grade {grade} with Total marks of {total}")                