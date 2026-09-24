"""
WAP to store one student data as a tuple: name, roll number, and marks.
Display grade based on marks.
"""

name = input("Enter a Name : ")
rollno = int(input("Enter Roll Number : "))
marks = int(input("Enter Marks : "))

stu = (name, rollno, marks)

print(stu)

grade = ""

if 85 <= marks <= 100:
    grade = 'A'
elif 71 <= marks <= 84:
    grade = 'B'
elif 50 <= marks <= 70:
    grade = 'C'
else:
    grade = 'Fail'

print("Name :",stu[0])
print("Roll Number :",stu[1])
print("Marks :",stu[1])
print("Grade :",grade)