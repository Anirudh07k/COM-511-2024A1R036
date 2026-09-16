"""
WAP to input marks of 10 students.
Store only valid marks between 0 and 100 in a list. Skip invalid marks.
"""

marks = []

print("Enter Marks: ")
for i in range(10):
    m = int(input())
    if 0 <= m <= 100:
        continue
    marks.append(m)

print("Marks :",marks)

# print("Enter Marks: ")
# for i in range(10):
#     m = int(input())
#     if 0 <= m <= 100:
#         marks.append(m)
#     else:
#         print("Invalid Marks")

# print("Marks :",marks)