"""
WAP to input a list of numbers and create a new list containing only unique elements.
"""

numbers = list(map(int , input("Enter Numbers : ").split()))

unique = []
for i in numbers:
    if i not in unique:
        unique.append(i)
print("Unique Numbers in List :",unique)

# x = set(numbers)
# print("Unique Numbers in List :",list(x))