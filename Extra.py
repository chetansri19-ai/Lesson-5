Maths=int(input("Enter your Maths marks: "))
Science=int(input("Enter your Science marks: "))
English=int(input("Enter your English marks: "))
Socials=int(input("Enter your Socials marks: "))
Critical_Thinking=int(input("Enter your Critical Thinking marks: "))
total_marks=Maths+Science+English+Socials+Critical_Thinking
percentage=(total_marks/500)*100

#Using the percentage calculate the grade
if percentage>=99:
    grade="A+"
elif percentage>=80:
    grade="A"
elif percentage>=70:
    grade="B"
elif percentage>=60:
    grade="C"
elif percentage>=50:
    grade="D"
else:
    grade="F"
print("Total Marks:", total_marks)
print("Percentage:", percentage)
print("Grade:", grade)
