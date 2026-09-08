"""
WAP to take input marks of 5 students.

for each student, the program should check whether the entered marks are valid or invalid.
Marks are considered valid only if they are between 0 and 100.
If the marks are Invalid, the program should display "Invalid marks skipped" and 
move to the next student without printing those marks.

If the marks are valid, the program should display the marks as valid
"""

for i in range(1, 6):
    marks = int(input("Enter marks : "))

    if marks < 0 or marks >= 100:
        print("Valid Marks")
        continue

    print("Invalid marks skipped",marks)

# for i in range(5):
#     marks = int(input(f"Enter marks of student {i + 1}: "))

#     if 0 <= marks <= 100:
#         print("Valid Marks")
#     else:
#         print("Invalid marks skipped")