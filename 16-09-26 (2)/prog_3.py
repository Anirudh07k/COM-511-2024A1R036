"""
WAP to input numbers in a list and find the second largest number.
"""

numbers = list(map(int , input("Enter Numbers : ").split()))
numbers.sort()

print("Second Largets Numbers in List :",numbers[-2])
