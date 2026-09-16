"""
WAP to input marks of n students in a list.
Display the highest marks, lowest marks, average marks, and number of students who passed.
"""

marks = list(map(int, input("Enter marks of Students : ").split()))


print("Highest Marks :",max(marks))
print("Lowest Marks :",min(marks))
print("Average Marks :",sum(marks) / len(marks))
count = 0
for i in marks:
    if i >= 40:
        count += 1
print("Number of Students who Passed :",count)